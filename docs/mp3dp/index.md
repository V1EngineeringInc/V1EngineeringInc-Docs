# MP3DP -Repeat-

![!mp3dp repeat](../img/repeat/Repeats.png)

**Updated version nearing completion, [forum thread](https://forum.v1engineering.com/t/repeat-v2/33330/55).**

This is the MP3DP -Repeat- __Milled/Printed 3D Printer "Repeat"__.  This can be a fun project 
to use your new CNC mill for. This is my take on a CoreXY 3D printer, with a CNC mill friendly
frame, or even a 20 series extrusion frame, options! 

The Repeat is a whole new take from the previous two designs, and I wanted to get a little 
experimental this time around in a few ways.  

 - CoreXY instead of a "bed slinger". After two fun [ZenXY](../zenxy/index.md) designs using 
CoreXY I think I have wrapped my head around the strengths and weaknesses of this geometry.

 - More frame options, instead of just material and thickness, you cannot opt to use 80 series 
extrusions instead of milled flat parts.

 - Direct Belt Driven Z axis. The resolution is there, quiet, fewer unique parts.

 - Hardware bed leveling (true bed leveling), and software (mesh leveling). Takes a bit longer to 
get started but flawless first layers are worth it. Time to make more accurate parts.

 - Simple Universal tool plate. Mount any extruder, laser, drag knife, pen, etc... 
 - 
 - Carbon fiber and linear rails. Quiet, accurate, and light where it is needed. The larger the build
 the more noticeable the weight loss.
 
 - [CAD files are available](https://a360.co/381SaiQ)! Edit it to your hearts content, this is an open design and is licensed 
under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

 - Very few unique printed parts, so editing is simple. 11(?), at last count.

## This Printer

If you just want to open a box and have a ready 3D printer there are a few solid options out there, this really is not one of those.
The MP3DP Repeat is a printer for those of you that want to build one, get your hands dirty, and learn a
thing or two! Currently, this is just a guide, not a full set of instructions. If anything is unclear 
let us know and we can add a picture or two. Hopefully nothing is too tricky here.


Questions and comments should be directed to the [V1 Engineering Forums](https://forum.v1engineering.com/c/mostly-printed-3d-printer-mp3dp/10). Asking questions is how these instructions get written. If you don't ask I will assume I don't need to write instructions for it. If you want to help write the instructions please click the little wrench icon in the upper right corner of this document, please.

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

|QTY  |Description             |Comment                          |Link                        | 
|-----|------------------------|---------------------------------|----------------------------|
|1    |Control Board           |6 driver minimum                 |[Shop][sh1] – [Amazon][az1]|
|5    |Steppers, Nema17        |20mm+ shaft length               |[Shop][sh2] – [Amazon][az2]|
|1    |Extuder or other tool   |Hemera,example, match voltage    |[Fila][sh3] – [Amazon][az3]|
|5    |Pulleys 16T 10mm        |10mm GT2 16 Tooth                |[Shop][sh4] – [Amazon][az4]|
|9    |Idlers w/Teeth 20T      |20T w/Teeth 5mm Bore             |[Shop][sh5] – [Amazon][az5]|
|2    |Idlers Smooth 20T       |20T Smooth 5mm Bore              |[Shop][sh6] – [Amazon][az6]|
|x    |Belt GT2 10mm           |See Calculator, no steel belt    |[Shop][sh7] – [Amazon][az7]|
|5    |Endstop Optical         |Must use this exact style        |[Shop][sh8] – [Amazon][az8]|
|6    |Wheels                  |POM V wheel 5mm bore 15.3mm OD   |[Shop][sh9] – [Amazon][az9]|
|1    |Heated Bed              |Style and Size will vary         |[Shop][sh10] – [Amazon][az10]|
|3-4  |Springs                 |For bed, silicon tube will work  |[Shop][sh11] – [Amazon][az11]|
|5    |Linear rails MGN        |2-XY+3-Z From CAD      MGN12H    |[Fila][sh12] – [Amazon][az12]|
|1    |CF Square Tube          |length from CAD 20mmx20mm        |[King][sh13] – [Amazon][az13]|
|1    |Power Supply            |Match voltage                    |[Fila][sh14] – [Amazon][az14]|
|*    |Thread locker           |Optional for grubs screws        |[Shop][sh15] – [Amazon][az15]|
|*    |Lube                    |Optional for idlers              |[Shop][sh16] – [Amazon][az16]|
|*    |PTFE Tube               |Optional Extruder to filament    |[Shop][sh17] – [Amazon][az17]|
|*    |Print Fan               |Optional fits hemera mount       |[Shop][sh18] – [Amazon][az18]|

[sh1]: https://shop.v1engineering.com/collections/3dprinter-parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3
[sh2]: https://shop.v1engineering.com/collections/3dprinter-parts/products/nema-17-76oz-in-steppers
[sh3]: https://www.filastruder.com/collections/e3d-hemera/products/e3d-hemera?variant=39486550507591
[sh4]: https://shop.v1engineering.com/collections/3dprinter-parts/products/pulley-16-tooth-gt2-10mm
[sh5]: https://shop.v1engineering.com/products/idler-10mm-20t-5mm-bore
[sh6]: https://shop.v1engineering.com/collections/3dprinter-parts/products/20t-idler-gt2-10mm
[sh7]: https://shop.v1engineering.com/collections/3dprinter-parts/products/gt2-10mm-belt
[sh8]: https://shop.v1engineering.com/collections/3dprinter-parts/products/optical-endstop
[sh9]: https://shop.v1engineering.com/collections/zenxy/products/v-wheel
[sh10]: https://shop.v1engineering.com/collections/3dprinter-parts/products/mk3-aluminum-heated-bed
[sh11]: https://shop.v1engineering.com/collections/3dprinter-parts/products/spring
[sh12]: https://www.filastruder.com/products/ldo-linear-rails?variant=31796304150599
[sh13]: https://hobbyking.com/en_us/carbon-fibre-square-tube-20-x-20-x-800mm.html
[sh14]: https://www.filastruder.com/products/meanwell-lrs-350-24-psu?_pos=3&_sid=4a733ffaa&_ss=r
[sh15]: https://shop.v1engineering.com/collections/3dprinter-parts/products/0-5ml-threadlocker-242
[sh16]: https://shop.v1engineering.com/collections/3dprinter-parts/products/super-lube-silicone-lubricating-grease-with-syncolon-ptfe
[sh17]: https://shop.v1engineering.com/collections/3dprinter-parts/products/ptfe-liner?variant=39521587331187
[sh18]: https://shop.v1engineering.com/collections/3dprinter-parts/products/5015-12v-fan-blower

[az1]: https://amzn.to/3mp6nOk
[az2]: https://amzn.to/3FcxGlE
[az3]: https://amzn.to/3tdtnE9
[az4]: https://amzn.to/3n9mUGM
[az5]: https://amzn.to/31HTnwa
[az6]: https://amzn.to/3JXAXJi
[az7]: https://amzn.to/3u5imW6
[az8]: https://amzn.to/3zHAKFf
[az9]: https://amzn.to/33WT0yo
[az10]: https://amzn.to/3FgVRPM
[az11]: https://amzn.to/3G9HFcG
[az12]: https://amzn.to/3HLM85I
[az13]: https://amzn.to/34HCnHL
[az14]: https://amzn.to/31OsAOY
[az15]: https://amzn.to/3GhaKmx
[az16]: https://amzn.to/31H7yS6
[az17]: https://amzn.to/3f5Ml7E
[az17]: https://amzn.to/3Fq3Vy1


As an Amazon Associate I earn from qualifying purchases.

## Printed Parts

No Support needed. Infill on the parts is not a big deal I use 20%+ will be fine 40% is really nice, but make sure to use 2-3 perimeter walls to
keep the through hole support.

I have the parts available at these hosts if you are not comfortable exporting directly from the CAD model 
[PrusaPrinters](https://www.prusaprinters.org/prints/101182-mp3dp-repeat-), Thingiverse, or [GitHub](https://github.com/V1EngineeringInc/MP3DP-Repeat).

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
### Needed for all types of build
|Qty |Name                    |Comment|
|----|------------------------|-------|
|29  |M5x30mm                 |Pan Heads|
|29  |M5 Nylock               |         |
|52  |M3x10mm                 |Pan Heads|


### Components to box wall
This is going to be tricky depending on what you make it out of...

|Qty |Name                    |Comment|
|----|------------------------|-------|
|41  |Wall screws             |       |

You will need *at least* 41 more screws. That counts 3 per linear rail.

For a wood or plastic build using inserts this can easily be M3x10mm screws. Other options are #4 or equivalent screws suitable for your material.
For an extrusion build these will be M3x8mm screws.

You will alaso need hardware to build your box out of your chosen material. Extrusion based builds will need a lot of inserts and screws. 
Figure at least 41 plus 4-5 per corner joint, plus corner pieces of whatever style you prefer.

### Tool mount

You will also need whatever hardware is specified for your tool/extruder you choose.


## CAD

The Fusion360 CAD files can be found here, [at this link](https://a360.co/381SaiQ). Please consider these files under 
this license for now [Creative Commons License](http://creativecommons.org/licenses/by-sa/4.0/). This work is licensed 
under a Creative Commons Attribution-ShareAlike 4.0 International License. For now. 

**I learned Fusion360 for this project so you can have the actual CAD to edit. Please be nice, I know I made a lot of 
mistakes early on but it does work. As I progress and edit files I am fixing any early mistakes I made.**

Notes for making adjustments...and working through any subsequent CAD errors.
- How to resize X axis ... 
- How to resize Y axis ...
- How to resize Z axis ...

## Extruder Options

This can really print fast if you use a remote drive or bowden system, but it is plenty robust to handle a direct drive extruder.

The Hemera is a solid option for a direct drive extruder, here is one I desgned and use, along with the CAD files.
[Hemera Mount on Prusa Printers](https://www.prusaprinters.org/prints/99754-mp3dp-repeat-hemera-mount-bl-touch-and-fan-duct),
[Thingiverse](https://www.thingiverse.com/thing:5170332)- Uses a 5015 fan and the BL Touch.

[CAD files in Fusion 360](https://a360.co/3AAP0yA)


## Initial leveling

 
## Slicer Settings

## Want to see how one guy creates something like this?
Ha, it takes a lot of help from my friends! Check out how we all put our heads together in the [ V1 Forums](https://forum.v1engineering.com/t/new-printer-time/28127).

## Assembly
Assembly starts on the next [page](../mp3dp/repeatassm.md).
