# Low Rider CNC 3

The LowRider3 CNC is the V1 Engineering version of a CNC router that can handle full sheet material! Of
course you can go smaller. If the MPCNC is not big enough for you this picks up where that left off.

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (6).jpg){: loading=lazy width="600"}

### Key Points

 * Most parts can be 3D printed. To save from shipping or printing large parts the machine can be partially assembled to cut them itself.

 * Easily Removable from the table for storage or portability.

 * Inexpensive Hardware Store Conduit is the recommended rail. Rails ranging from 23.4mm to 25.4mm will work.

 * Many tool options, in terms of functionality and brands. Blank DIY mount files are available.

 * Full Y and Z axis squaring, leveling, and Z probing are available for excellent precision and accuracy.

 * Works with any 5 driver board.

 * Can be used with Marlin, RepRap firmware, GRBL, FluidNC, or others.

 ![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (2).jpg){: loading=lazy width="600"} 
 
### Geometry

* This CNC router can handle any length (within reason), the Y direction is only bound by your table length.

* Width (X axis or "Beam") should always be the shorter axis.

* The Z direction (height) is best kept to 80mm with that being said, you can edit the files to make the Z length as much as you want.

* This router is most rigid when working near the table surface, opposite of most conventional gantry CNC machines.

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (3).jpg){: loading=lazy width="600"}
 
### License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

More details to my loosened restrictions can be found here on [the home page](https://www.v1engineering.com/license/). 

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (4).jpg){: loading=lazy width="600"}

### Files can be found at the links below

Printables.com
:   [Printables.com Link](https://www.printables.com/model/204709-lowrider-3-cnc)

Thingiverse Printed parts files:
:   [Thingiverse.com Link](https://)

!!! info Previous build "LR V2"
    Version two instructions are [here](../lowrider/lrv2/indexv2.md)

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (5).jpg){: loading=lazy width="600"}
![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (7).jpg){: loading=lazy width="600"}
![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (8).jpg){: loading=lazy width="600"}

## Hardware list

### Printed Parts

|QTY  |File Name                   |Infill |Comment                                |Link                        | 
|-----|----------------------------|-------|---------------------------------------|----------------------------|
|1    |LR Core                     |35%    |                                       |                            |
|1    |X Drive Mount               |30%    |                                       |                            |
|2    |Y Drive                     |30%    |                                       |                            |
|2    |Z Drive                     |30%    |                                       |                            |
|4    |Temporary Strut             |30%    |                                       |                            |
|1    |Front Rail Roller           |30%    |                                       |                            |
|1    |Rear Rail Roller            |30%    |                                       |                            |
|1    |Bearing Wheel Bracket Front |30%    |Optional Wheeled Version available     |[Info](link)                |
|1    |Bearing Wheel Bracket Rear  |30%    |Optional Wheeled Version available     |[Info](link)                |
|1    |Z Stop                      |30%    |                                       |                            |
|1    |Z Stop M                    |30%    |                                       |                            |
|6-8  |Brace -Choose one size-     |30-50% |* See Brace Note below                 |                            |
|6-8  |Hose Hanger                 |30%    |Same number as braces, Optional part   |                            |
|1    |X Tensioner                 |30%    |                                       |                            |
|1    |XZ Plate Left               |70%    |* See XZ note below - Can be milled    |[Shop](link) [DXF](link)    |
|1    |XZ Plate Right              |70%    |* See XZ note below - Can be milled    |[Shop](link) [DXF](link)    |
|1    |Front Y Belt Holder         |30%    |                                       |                            |
|1    |Front Y Belt Base           |30%    |                                       |                            |
|1    |Front Y Belt Holder Right   |30%    |                                       |                            |
|1    |Front Y Belt Base Right     |30%    |                                       |                            |
|1    |Y Tension Block Rear        |30%    |                                       |                            |
|1    |Y Tension Base Rear         |30%    |                                       |                            |
|1    |Y Tension Block Rear Right  |30%    |                                       |                            |
|1    |Y Tension Base Rear Right   |30%    |                                       |                            |
|8-14 |Rail Block -Choose one size-|30%    |* See Rail block note below            |                            |
|     |Optional                    |       |                                       |                            |
|2    |YZ Plate                    |50%    |Best as a milled part                  |[Shop](link) [DXF](link)    |

 * Brace note-  Print the end two braces with 50% infill and the rest with 30%. 2' wide builds need 6 total,
 4 foot versions need 8 total. Recommended US 3/4" EMT = 23.4mm = Brace 23p4 That is the suggested size for US based builds.

 * XZ Note- Can be a flat part. Milled or Purchased. If you do use a flat part you will need to print both "XZ Leadscrew Stub Right" and "XZ Leadscrew Stub".

 * Rail Block note- You want these with no larger than an 8" gap between them. Recommended US 1/2" EMT = 18.1mm = Rail Block 18p1.3mf


### Tool Mounts
Include CAD


### Board Boxes
Include CAD

## Flat parts

DXF
CAD


### Specialty Parts

|QTY  |Description             |Comment                                        |Link                        | 
|-----|------------------------|-----------------------------------------------|----------------------------|
|1    |Control Board           |5 driver minimum                               |[Shop][sh1] – [Amazon][az1]|
|5    |Steppers, Nema17        |20mm+ shaft length                             |[Shop][sh2] – [Amazon][az2]|
|3    |stepper wire extenders  |                                               |[Shop][sh3] – [Amazon][az3]|
|3    |Pulleys 16T 10mm        |10mm GT2 16 Tooth                              |[Shop][sh4] – [Amazon][az4]|
|6    |Idlers Smooth 20T       |20T Smooth 5mm Bore                            |[Shop][sh5] – [Amazon][az5]|
|8M   |Belt GT2 10mm           |See [Calculator](calculator.md), no steel belt |[Shop][sh6] – [Amazon][az6]|
|5    |Endstops                |                                               |[Shop][sh7] – [Amazon][az7]|
|14   |6082rs Bearings         |                                               |[Shop][sh8] – [Amazon][az8]|
|2    |T8 Leadscrew & nut      |110mm or larger                                |[Shop][sh9] – [Amazon][az9]|
|2    |Coupler                 |8mm to 5mm                                     |[Shop][sh10] – [Amazon][az10]|
|4    |Linear rails MGN        |MGN12H 150mm                                   |[Shop][sh11] – [Amazon][az11]|
|1    |Power Supply            |12-36V Board dependant 36W+                    |[Shop][sh12] – [Amazon][az12]|
|*    |Thread locker           |Optional for grubs screws                      |[Shop][sh13] – [Amazon][az13]|
|*    |Lube                    |Optional for idlers and linear rails           |[Shop][sh14] – [Amazon][az14]|
|*    |Vac Hose                |Optional any 1.5" OD Vacuum hose should work   |[Shop][sh15] – [Amazon][az15]|

[sh1]: https://shop.v1engineering.com/collections/3dprinter-parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3
[sh2]: https://shop.v1engineering.com/collections/3dprinter-parts/products/nema-17-76oz-in-steppers
[sh3]: https://shop.v1engineering.com/products/wiring-kit-1
[sh4]: https://shop.v1engineering.com/collections/3dprinter-parts/products/pulley-16-tooth-gt2-10mm
[sh5]: https://shop.v1engineering.com/collections/3dprinter-parts/products/20t-idler-gt2-10mm 
[sh6]: https://shop.v1engineering.com/collections/3dprinter-parts/products/gt2-10mm-belt
[sh7]: https://shop.v1engineering.com/collections/parts/products/limit-switch-endstop
[sh8]: https://shop.v1engineering.com/collections/lowrider-parts/products/bearings-608-2rs 
[sh9]:  
[sh10]: https://shop.v1engineering.com/collections/lowrider-parts/products/5mm-to-8mm-flex-coupler
[sh11]: 
[sh12]: https://shop.v1engineering.com/collections/lowrider-parts/products/12v-6a-power-supply
[sh13]: https://shop.v1engineering.com/collections/3dprinter-parts/products/0-5ml-threadlocker-242
[sh14]: https://shop.v1engineering.com/collections/3dprinter-parts/products/super-lube-silicone-lubricating-grease-with-syncolon-ptfe
[sh15]: 

[az1]: https://amzn.to/3mp6nOk
[az2]: https://amzn.to/3FcxGlE
[az3]: https://amzn.to/39DSW9I
[az4]: https://amzn.to/3n9mUGM
[az5]: https://amzn.to/3JXAXJi 
[az6]: https://amzn.to/3u5imW6
[az7]: https://amzn.to/396oRzi
[az8]: https://amzn.to/3FDI8EI 
[az9]: https://amzn.to/3wnjvrI 
[az10]: https://amzn.to/3yoet0D 
[az11]: https://amzn.to/3N26PwR
[az12]: https://amzn.to/3Pe0P6m
[az13]: https://amzn.to/3GhaKmx
[az14]: https://amzn.to/31H7yS6
[az15]: https://amzn.to/38iqA4v

As an Amazon Associate I earn from qualifying purchases.

### Hardware

This is what is needed for a 4' x 8' (1.2M x 2.4M) build. You will need more or less depending on what size you build.

|QTY  |Description             |US Equivalent                                  | 
|-----|------------------------|-----------------------------------------------|
|14   |M8 x 40mm               |5/16" x 1.5"                                   |
|14   |M8 Nylock nuts          |5/16" Nylock                                   |
|100  |M5 x 30mm               |None                                           |
|100  |M5 Nylock               |None                                           |
|40   |M3 x 10mm               |None                                           |
|10   |M2.5 x 12mm             |None                                           |
|24   |3mm x 12mm Wood/metal   |#4 x 1/2" Wood or Sheet metal screws           |
|*22  |M4 x 12mm+ Wood/metal   |#8 x 1/2"+ Screws to mount things to your table|

* Not included in the hardware kit. 

### LR2 to LR3 hardware differnces for updating your build
|QTY  |Description             |US Equivalent                                  | 
|-----|------------------------|-----------------------------------------------|
|14   |M8 x 40mm               |5/16" x 1.5"                                   |
|94   |M5 x 30mm               |None                                           |
|94   |M5 Nylock               |None                                           |
|36   |M3 x 10mm               |None                                           |
|10   |M2.5 x 12mm             |None                                           |
|24   |3mm x 12mm Wood/metal   |#4 x 1/2" Wood or Sheet metal screws           |
|22  |M4 x 12mm+ Wood/metal   |#8 x 1/2"+ Screws to mount things to your table|

### Table

Any flat surface you can screw into will work great. Basic torsion box tables can 
be a step up in terms of long term stability with not all that much added complexity.
 A Removable section that can be easily replaced comes in handy as well.

footprint
rail position
Belt block positions

[Calculator for table, rail, and belt lengths.](calculator.md)


## Assembly


### Core Assembly

![!LR3 Fancy Picture](../img/lr3/LR3 (1).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (2).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (3).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (4).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (5).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (6).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (7).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (8).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (9).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (10).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (11).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (12).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (13).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (14).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (15).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (16).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (17).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (18).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (19).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (20).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (21).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (22).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (23).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (24).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (25).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (26).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (27).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (28).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (29).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (30).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (31).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (32).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (33).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (34).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (35).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (36).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (37).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (38).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (39).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (40).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (41).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (42).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (43).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (44).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (45).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (46).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (47).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (48).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (49).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (50).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (51).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (52).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (53).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (54).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (55).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (56).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (57).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (58).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (59).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (60).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (61).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (62).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (63).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (64).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (65).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (66).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (67).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (68).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (69).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (70).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (71).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (72).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (73).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (74).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (75).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (76).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (77).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (78).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (79).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (80).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (81).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (82).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (83).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (84).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (85).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (86).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (87).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (88).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (89).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (90).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (91).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (92).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (93).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (94).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (95).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (96).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (97).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (98).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (99).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (100).jpg){: loading=lazy width="400"}

---
### Side Plate Assemblies


## Firmware

Dual endstop LowRider "DualLR" firmware reccomended for ultimate accuracy and precision. This requires 
at least a 5 driver control board. This allows you to align the Y axis and Z axis using dual endstops.

The standard MPCNC firmware will work with any board on the LowRider  if you are not using endstops or 
wired in series (using a 4 driver board). You will just use hardstops like the LR2 did.

[Firmware page.](../electronics/marlin-firmware.md)


### Vaccuum Hose

Size, options, routing.

## Getting Started, cutting your strut plates

test move
level
square
cut strut plates

## final assembly

### Using the machine.

## Go get it dirty, be safe, have fun!
![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (1).jpg){: loading=lazy width="600"}