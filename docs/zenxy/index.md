# ZenXY v2

![!FirstZenXY](https://www.v1engineering.com/wp-content/uploads/2017/07/IMG_20170717_103443.jpg){: width="450"}

Inspired by the awesome Sisyphus Table by Bruce Shapiro, [http://www.sisyphus-industries.com/](http://www.sisyphus-industries.com/), Zen gardens that my mom loves, and the crazy CoreXY belting system.

This is my second attempt at an automated Zen Garden.

![!ZenXY v2 Render](https://www.v1engineering.com/wp-content/uploads/2021/03/XZXY-V2F-squarer.jpg){: width="450"}

## Software

CircleCI test edit

### Sandify
![!Sandify](https://www.v1engineering.com/wp-content/uploads/2019/01/screenshot-2019-01-02-1546472560.png){: width="450"}

Amazing patterns are easily possible by using [Sandify.org](https://sandify.org/), the back end is here [Sandify on GitHub](https://github.com/jeffeb3/sandify),
This table would be nothing without this tool! ([feel free to show some appreciation for this amazing free piece of
software](https://liberapay.com/jeffeb3/)).

### Karl’s EstlEgg-ify
Karl’s way allows for some custom vector graphics to be easily drawn. Here in the [Forum](https://www.v1engineering.com/forum/topic/artistic-designs-with-inkscape-eggbot-tools-and-estlcam/).


## Firmware

This is running CoreXY belting and requires homing Y before X, as set in the firmware. The stepper with the endstops on the same block gets plugged into the "X" port on the control board. If it does not move correctly, power down unplug and flip them both over, or flip just one over. It is more confusing then the regular Cartesian troubleshooting. Guess and check is the best way.

[Firmware link](https://github.com/Allted/Marlin/tree/CHOOSE_VERSION)
