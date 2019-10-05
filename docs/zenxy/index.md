# ZenXY

!!! warning
    These documents are not yet the official documents. Please go to v1engineering.com for the up to date and accurate
    instructions.

[at v1engineering.com](https://www.v1engineering.com/zenxy/)

Inspired by the awesome Sisyphus Table by Bruce Shapiro, [http://www.sisyphus-industries.com/](http://www.sisyphus-industries.com/), Zen gardens that my mom used to love, and the crazy CoreXY belting system.

This is my attempt at an easily sourced automated Zen Table.

## Software

### Sandify
Amazing patterns are easily possible by using Sandify, [Sandify on GitHub](https://github.com/jeffeb3/sandify), This table would be nothing without this tool! (feel free to show some appreciation for this amazing free piece of software).

### Karl’s EstlEgg-ify
Karl’s way allows for some custom vector graphics to be easily drawn. Here in the [Forum](https://www.v1engineering.com/forum/topic/artistic-designs-with-inkscape-eggbot-tools-and-estlcam/).


## Parts

### Printed Parts

STL Files found here,

[23.5mm OD](https://www.thingiverse.com/thing:2477901) (Common US 3/4″ Conduit) 

[25mm OD](https://www.thingiverse.com/thing:2867147)

[25.4mm OD](https://www.thingiverse.com/thing:2867134) (1″ Not common in the US) 

Print with 10% infill or higher, 3 perimeters.

| QTY.              | Printed Part Name |
|-------------------|-------------------|
|                   |                   |
| 1                 | ZXY Motor R       |
| 1                 | ZXY Motor L       |
| 1                 | ZXY Corner R      |
| 1                 | ZXY Corner L      |
| 1                 | ZXY Roller R      |
| 1                 | ZXY Roller L      |
| 1                 | ZXY Center        |
| 1                 | ZXY Belt Clamp    |
| 1                 | ZXY Stop Block    |

### Specialized Parts

### Hardware


## Rail Lengths

Since every table will be a different size a cut calculator is a bit difficult.

1- Y Rails. I suggest putting the outer corners into your build and measure the distance from the outer clamp loop, that gives you your Y rails lengths.

2- Y rails Square. Once you have the Y rails in place assemble the rollers and make sure the bolts heads do not hit the table as they move. Once you have this clearance established and you get the rails installed squarely by measuring the diagonals and making sure they are as equal as possible.

3- X rails. The X rails are 1/8″ shorter than the distance between the Y rails measured at the closest point.


## Table

## Assembly

## Firmware

This is running coreXY belting and requires homing Y before X, as set in the firmware. You need two endstops wired Normally Closed on the X and Y. If you are facing the two steppers and looking down at them, the left one should be plugged into X the right one into Y, both plugs facing the same direction, if it does not move correctly, power down unplug and flip them both over. It is more confusing then the regular Cartesian troubleshooting.

Firmware link

## More Info
