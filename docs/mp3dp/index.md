# MP3DP -Repeat-

![!mp3dp repeat](../img/repeat/Repeats.png)

This is the MP3DP -Repeat- __Milled/Printed 3D Printer "Repeat"__.  This can be a fun project 
to use your new CNC mill for. This is my take on a CoreXY 3D printer, with a CNC mill friendly
frame, or even an 20 series extrusion frame, options! 

The Repeat is a whole new take from the previous two designs and I wanted to get a little 
experimental this time around in a few ways.  
* CoreXY instead of a "bed slinger". After two fun [ZenXY](../zenxy/index.md) designs using 
CoreXY I think I have wrapped my head around the strengths and weaknesses of this geometry. 
* More frame options, instead of just material and thickness, you can not opt to use 80 series 
extrusions instead of milled flat parts.
* Direct Belt Driven Z axis. The resolution is there, quiet, fewer unique parts.
* Hardware bed leveling (true bed leveling), and software (mesh leveling). Takes a bit longer to 
get started but flawless first layers are worth it. Time to make more accurate parts.
* Simple Universal tool plate. Mount any extruder, laser, dragknife, pen, etc... 
* Carbon fiber and linear rails. Quiet, accurate, and light where it is needed. The larger the build
 the more noticeable the weight loss.
* [CAD files are available](https://a360.co/381SaiQ)! Edit it to your hearts content, this is an open design and is licensed 
under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
* Very few unique printed parts, so editing is simple. 11(?), at last count.

# This Printer

If you just want to open a box and have a ready 3D printer there are a few solid options out there, this really is not one of those.
The MP3DP Repeat is a printer for those of you that want to build one, get your hands dirty, and learn a
thing or two! Currently, this is just a guide, not a full set of instructions. If anything is unclear 
let us know and we can add a picture or two. Hopefully nothing is too tricky here.


Questions and comments should be directed to the [V1 Engineering Forums](https://forum.v1engineering.com/c/mostly-printed-3d-printer-mp3dp/10). Asking questions is how these instructions get written. If you don't ask I will assume I don't need to write instructions for it. If you want to help write the instructions please click the little wrench icon in the upper right coner of this document, please.

!!! info "Previous MP3DP versions"
    Version one and two instructions are linked on the main menu [V1](version1.md), [V2](version1.md).
    
## Control Boards

You will need a control board with at least 6 drivers, E-XY-ZZZ. The SKR Pro works well and we have a pre-configured firmware for it, 
[V13RP_SkrPro_2209](../electronics/marlin-firmware.md). Many other boards and firmware will work as well.
       

## Frame Options

You can use extrusions, or Milled parts. This is where I am going to let you know it would be best to refer to the CAD model for this. Flat parts can be adjusted for thickness and joining method, Extrusions will get exact lengths. This printer is pretty easy to make any size you want if you are having issues adjusting the CAD model I will add some notes down below.

details to come...

If you choose a milled frame have fun with it, cut in some flavor, no need to have all that material there, you have a CNC
machine use it!


|QTY |Part Name      |Comments|
|----|---------------|-|
|1   |placeholder       | |


## Specialty Parts

|QTY  |Description             |Comment                      |Link         | 
|-----|------------------------|-----------------------------|-------------|
|1    |Control Board           |6 driver minimum             |[Shop][sh1] – [Amazon][az1]|

[sh1]: https://shop.v1engineering.com/collections/3dprinter-parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3

[az1]: https://amzn.to/3mp6nOk


As an Amazon Associate I earn from qualifying purchases.

## Printed Parts

No Support neeeded. Infill on the parts is not a big deal I use 20%+ will be fine 40% is real nice, but make sure to use 2-3 perimeter walls to
keep the through hole support.

I have the parts available at these hosts if you are not comfotable exporting directly from the CAD model 
[PrusaPrinters](https://www.prusaprinters.org/prints/101182-mp3dp-repeat-), Thingiverse, or Github.

|QTY |Name                    |
|----|------------------------|
|5   |Stepper Mount           |
|4   |Truck Trigger           |
|3   |Z Bed Slider            |
|3   |Z Post                  |
|3   |Z Idler                 |
|2   |Truck Spacer            |
|2   |Belt Tugger             |
|2   |Corner Inner            |
|2   |Corner Outer            |
|1   |Hub                     |
|*   |Optional Parts          |
|2   |Extruder Passthrough    |
|2   |Spool Mount             |
|1   |Filament Guide          |

## Hardware
This is going to be tricky depending on what you make it out of...

|Qty |Name                    |Comment|
|----|------------------------|-------|
|*   |M5x30mm                 |Pan Heads|


## CAD
Notes for making adjustments...Working through CAD errors.


## Initial leveling

 
## Slicer Settings

## Want to see how one guy creates something like this?
Ha, it takes a lot of help from my friends! Check out how we all put our heads together in the [ V1 Forums](https://forum.v1engineering.com/t/new-printer-time/28127).

## Assembly
Probably going to be a new page for this.
