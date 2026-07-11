from PIL import Image 
import sys 



class Color:
    def __init__(self, color, name="", target=None, distance=-1):
        self.color = color
        self.target = target
        self.name = name
        if self.target is None: self.target = self.color
        self.distance = distance

    def compare_color(self, rhs):
        new_distance = pow(self.target[0] - rhs[0], 2) + pow(self.target[1] - rhs[1], 2) + pow(self.target[2] - rhs[2], 2)
        if self.distance == -1 or new_distance < self.distance:
            self.color = rhs
            self.distance = new_distance

    def get_hex(self):
        return "".join(['{0:0{1}X}'.format(i,2) for i in self.color])

    def __str__(self):
        return f"{self.name}\t- {self.color}\t - {self.get_hex()}"


def alacritty_config():
    print("\n\n################################")
    print("########## alacritty ###########")
    print("################################")
    print("[colors.normal]")
    for color in palette:
        print(f"{color.name} = \"#{color.get_hex()}\"")
    print("\n[colors.bright]")
    for color in bright_palette:
        print(f"{color.name} = \"#{color.get_hex()}\"")
    print("\n[colors.primary]")
    for color in grounds_palette:
        print(f"{color.name} = \"#{color.get_hex()}\"")

def i3wm_config():
    print("\n\n################################")
    print("############## i3 ##############")
    print("################################")
    print("# Normal Colors")
    for color in palette:
        print(f"set ${color.name} #{color.get_hex()}")
    print("\n# Bright Colors")
    for color in bright_palette:
        print(f"set $bright_{color.name} #{color.get_hex()}")
    print("\n# Background/Foreground colors")
    for color in grounds_palette:
        print(f"set ${color.name} #{color.get_hex()}")

def rofi_config():
    print("Warning! Not Implemented")

if __name__=="__main__":
    args = sys.argv 
    valid_configs = ["--alacritty", "--rofi", "--i3"]
    if len(args) < 3: 
        print("python cmd_palette_grabber.py [image path] [opt]")
        for i in valid_configs:
            print(f"\t{i}")
        sys.exit()

    fp = args[1]
    

    for i in args[2:]:
        if i not in valid_configs:
            print(f"Unkown flag: {i}")
            sys.exit()

    im = Image.open(fp)
    pix = im.load()
    size = im.size

    palette = [
    Color((0,0,0), "black"),
    Color((0,0,255), "blue"),
    Color((0,255,255), "cyan"),
    Color((0,255,0), "green"),
    Color((255,0,255), "magenta"),
    Color((255,0,0), "red"),
    Color((240,240,240), "white")
    ]

    bright_palette = [
    Color((84, 112, 112), "black"),
    Color((238,75,43), "red"),
    Color((141, 186, 253), "blue"),
    Color((172, 255, 252), "cyan"),
    Color((45, 254, 84), "green"),
    Color((213, 175, 249), "magenta"),
    Color((255, 255, 255), "white")
    ]

    grounds_palette = [
    Color((45,45,48), "background"),
    Color((200, 200, 200), "foreground"),
    Color((180, 180, 180), "dim_foreground"),
    Color((255, 255, 255), "bright_foreground")
    ]

    #extras = [
    #    Color((), "orange"),
    #    Color((), "yellow"),
    #    Color((), "bright_orange"),
    #    Color((), "bright_yellow"),
    #]

    for x in range(size[0]):
        for y in range(size[1]):
            color = pix[x,y]
            color = (color[0], color[1], color[2])
            for prev in palette:
                prev.compare_color(color)
            for prev in bright_palette:
                prev.compare_color(color)
            for prev in grounds_palette:
                prev.compare_color(color)
    
    if "--alacritty" in args:
        alacritty_config()
    if "--rofi" in args:
        rofi_config()
    if "--i3" in args:
        i3wm_config()

