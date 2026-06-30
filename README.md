# cmd-palette-grabber

Requires: 
  + python3+
  + python-pillow

## Usage

`python cmd_palette_grabber.py [image fp]`

Slow on large images*

## How it works

The code starts with some basic colours of a terminal: black, blue, cyan, green, magenta, red and white. The bright colours of these are also included. The colours are assigned as target values and then the code searches through the image to find the closest colour it can for each target colour. It then displays the alacritty colour configuration which can be pasted into `~/.config/alacritty/alacritty.toml` or any related file.

## Example

![example image](cmd_palette_grabber_demo.png)

`python cmd_palette_grabber.py reze.png`

```
[colors.primary]
foreground = "#FFFFFF"
background = "#01060C"
dim_foreground = "#F0F0F0"
bright_foreground = "#FFFFFF"

[colors.normal]
black = "#01060C"
blue = "#0F5D8D"
cyan = "#42A5BC"
green = "#447D76"
magenta = "#D57C7E"
red = "#B44E42"
white = "#F0F0F0"

[colors.bright]
black = "#536F72"
red = "#C45E50"
blue = "#95C2DF"
cyan = "#B3E9F3"
green = "#4E9398"
magenta = "#C3C9E9"
white = "#FFFFFF"
```



