# Low Rider CNC 4

The LowRider3 is the V1 Engineering version of a CNC router that can handle up to full sheet material! If the MPCNC is not big 
enough for you this picks up where that left off.

![!LR4 Fancy Picture](../img/lr4/LR4Render.png){: loading=lazy width="600"}

### Key Points

 * Most parts can be 3D printed. To save from shipping or printing large parts the machine can be partially assembled to cut them itself.

 * Easily Removable from the table for storage or portability.

 * Inexpensive hardware store conduit is the recommended X rail. Rails ranging from 23.4mm to 25.4mm will work. This saves considerable cost over the LR2.

 * Many tool options, in terms of functionality and brands. Blank DIY mount files are available.

 * Full Y and Z axis squaring, leveling, and Z probing are available for excellent precision and accuracy.

 * Works with any 5 driver board. 4 driver boards can be used but some automation, one axis dual endstops, will be lost.

 * Can be used with Marlin, RepRap firmware, GRBL, FluidNC, or others.

 ![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (2).jpg){: loading=lazy width="600"} 
 
### Geometry

* This CNC router can handle any length (within reason), the Y direction is only bound by your table length.

* The single Y rail keeps the machine properly constrained while maintaining ease of use. Two rails are extremely difficult to 
align, and fully constrained rails do not allow for easy removal of the machine.

* Width (X axis or "Beam") should always be the shorter axis.

* The Z direction (height) is best kept to 80mm. This allows for 1.5" of cutting depth, that is a lot. If you need to cut more than 1.5" deep this is not 
the CNC for you. Now if you need to cut a few millimeters off really thick material (facing a slab), this can be a great machine for that. You want to keep the machine as low as possible and 
make the table surface adjustable by using something like a drop table. This keeps the Material Removal Rate very high. The answer is not making a taller machine.

* This router is most rigid when working near the table surface, opposite of most conventional gantry CNC machines. So the lower the axis the more rigid the machine.

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (3).jpg){: loading=lazy width="600"}
 
### License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

More details to my loosened restrictions can be found here on [the home page](https://www.v1e.com/pages/trademark-and-file-licenses). 

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (4).jpg){: loading=lazy width="600"}

### Files

Printed parts files can be found at the links below:

Printables.com
:   [Printables.com Link](https://www.printables.com/model/204709-lowrider-3-cnc){:target="_blank"}

Thingiverse Printed parts files:
:   [Thingiverse.com Link](https://www.thingiverse.com/thing:5436094){:target="_blank"}

![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (7).jpg){: loading=lazy width="600"}

!!! info Previous build "LR V3"
    Version 3 instructions are [here](../lowrider/lowrider3.md)

## Parts Needed

### Printed Parts

!!! warning 
    NEED INFO

Buy a set here, [V1 Shop](https://www.v1e.com/collections/lowrider-parts/products/lowrider-v4-printed-parts){:target="_blank"}.

Or print your own. No supports needed, keep the default orientation. PLA is recommended for ultimate rigidity, other 
filaments should be evaluated for rigidity. 2-3 walls rectilinear infill. Thicker layers since these are large parts, no 
more than 80% nozzle diameter to keep overhangs working.

|QTY |File Name                   |Infill |Comment                              |Link                                     | 
|----|----------------------------|-------|-------------------------------------|-----------------------------------------|
|1   |LR Core                     |35%    |                                     |                                         |
|1   |X Drive Mount               |30%    |                                     |                                         |
|2   |Y Drive                     |30%    |                                     |                                         |
|2   |Z Drive                     |30%    |                                     |                                         |
|4   |Temporary Strut             |30%    |                                     |                                         |
|1   |Front Rail Roller           |30%    |                                     |                                         |
|1   |Rear Rail Roller            |30%    |                                     |                                         |
|1   |Bearing Wheel Bracket Front |30%    |* See note below - Optional Version  |[Link][Wheels]                           |
|1   |Bearing Wheel Bracket Rear  |30%    |* See note below - Optional Version  |[Link][Wheels]                           |
|1   |Z Stop                      |30%    |                                     |                                         |
|1   |Z Stop M                    |30%    |                                     |                                         |
|6-8 |Brace -Choose one size-     |30-50% |* See Brace Note below               |                                         |
|6-8 |Hose Hanger                 |30%    |Same number as braces, Optional part |                                         |
|1   |X Tensioner                 |30%    |                                     |                                         |
|1   |XZ Plate Left               |70%    |* See XZ note below - Can be milled  |[Shop][xz1] - [DXF](#xz-plates)|
|1   |XZ Plate Right              |70%    |* See XZ note below - Can be milled  |[Shop][xz1] - [DXF](#xz-plates)|
|1   |Front Y Belt Holder         |30%    |                                     |                                         |
|1   |Front Y Belt Base           |30%    |                                     |                                         |
|1   |Front Y Belt Holder Right   |30%    |                                     |                                         |
|1   |Front Y Belt Base Right     |30%    |                                     |                                         |
|1   |Y Tension Block Rear        |30%    |                                     |                                         |
|1   |Y Tension Base Rear         |30%    |                                     |                                         |
|1   |Y Tension Block Rear Right  |30%    |                                     |                                         |
|1   |Y Tension Base Rear Right   |30%    |                                     |                                         |
|8-14|Rail Block -Choose one size-|30%    |* See Rail block note below          |                                         |
|    |Optionally Printed          |       |                                     |                                         |
|2   |YZ Plate                    |50%    |Best as a milled part                |[Shop][yz1] - [DXF](#yz-plates)|

[Wheels]: https://www.printables.com/model/211714-lr3-60mm-wheel-brackets
[xz1]: https://www.v1e.com/products/lowrider-3-metal-xz-plates
[yz1]: https://www.v1e.com/collections/lowrider-parts/products/lowrider-cnc-v3-yz-plates

 * Optional Version- You can use 58-62mm X 25mm urethane wheels with the optional brackets. The urethane wheels might provide for a smoother ride over 
 a rough table or debris with the downside being a bit of "give" and the possibility of the wheels steering a non parallel build. 
 The bearings are preferred, should be more precise and make for a more forgiving build. [Wheels](https://www.v1e.com/collections/lowrider-parts/products/urethane-wheels) 
 [Spacers](https://www.v1e.com/collections/all/products/axle-spacers)

 * Brace note-  Print the two left and right end braces with 50% infill and oriented so you can have the top facing out on each end, and the rest with 30% infill. 2' wide builds need 6 total,
 4 foot versions need 8 total. One every 200mm (8") or less. 
 There are three different brace sizes provided - `Brace 25.3mf`, `Brace 25p4.3mf`, and `Brace 23p4.3mf` which correspond to the diameter of the X rail in millimeters. 
 For US based builds, the recommended X rail size is US 3/4" EMT conduit which has a diameter equal to 23.4mm, so print the `Brace 23p4.3mf` parts for this size X rail. 

 * XZ Note- Can be a flat part. Milled or Purchased. If you do use a flat part you will need to print both `XZ Leadscrew Stub Right.3mf` and `XZ Leadscrew Stub.3mf`. These also need 70% infill.

 * Rail Block note- You want the gap between these to be no larger than 200mm (8") or less. You will need 8 for a 4' build and 14 for a 8' build. There are four different rail block sizes provided - `Rail block 18p1.3mf`, `Rail block 23p4.3mf`, `Rail block 25mm.3mf`, and `Rail block 25p4.3mf` which correspond to the diameter of the Y rail in millimeters. For US based builds, the recommended Y rail size is US 3/4" EMT conduit which has a diameter equal to 23.4mm, so print the `Rail Block 23p4.3mf` parts for this size Y rail.


### Tool Mounts
!!! warning 
    NEED INFO

### Board Boxes

!!! warning 
    NEED INFO

## Flat Parts

#### Strut Plates

!!! warning 
    NEED INFO


#### XZ Plates

!!! warning 
    NEED INFO


### Specialty Parts

You can buy most of the Specialty Parts and hardware here, [V1 Shop](https://www.v1e.com/collections/lowrider-parts/products/lowrider-v3-hardware-kit){:target="_blank"}

|QTY  |Description             |Comment                                        |Link                        | 
|-----|------------------------|-----------------------------------------------|----------------------------|
|1    |Control Board           |5 driver minimum                               |[Shop][sh1] – [Amazon][az1]|
|5    |Steppers, Nema17        |20mm+ shaft length                             |[Shop][sh2] – [Amazon][az2]|
|3    |stepper wire extenders  |                                               |[Shop][sh3] – [Amazon][az3]|
|3    |Pulleys 16T 10mm        |10mm GT2 16 Tooth                              |[Shop][sh4] – [Amazon][az4]|
|6    |Idlers Smooth 20T       |20T Smooth 5mm Bore                            |[Shop][sh5] – [Amazon][az5]|
|8M   |Belt GT2 10mm           |See [Calculator](calculator.md), no steel belt |[Shop][sh6] – [Amazon][az6]|
|5    |Endstops                |                                               |[Shop][sh7] – [Amazon][az7]|
|14   |608-2RS Bearings        |                                               |[Shop][sh8] – [Amazon][az8]|
|2    |T8 Leadscrew & nut      |110mm or larger                                |[Shop][sh9] – [Amazon][az9]|
|2    |Coupler                 |8mm to 5mm                                     |[Shop][sh10] – [Amazon][az10]|
|4    |Linear rails MGN        |MGN12H 150mm                                   |[Shop][sh11] – [Amazon][az11]|
|1    |Power Supply            |12-36V Board dependant 36W+                    |[Shop][sh12] – [Amazon][az12]|
|*    |Thread locker           |Optional for grubs screws                      |[Shop][sh13] – [Amazon][az13]|
|*    |Lube                    |Optional for idlers and linear rails           |[Shop][sh14] – [Amazon][az14]|
|*    |Vac Hose                |Optional any 1.5" OD Vacuum hose should work   | – [Amazon][az15]|

[sh1]: https://www.v1e.com/collections/3dprinter-parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3
[sh2]: https://www.v1e.com/collections/3dprinter-parts/products/nema-17-76oz-in-steppers
[sh3]: https://www.v1e.com/products/wiring-kit-1
[sh4]: https://www.v1e.com/collections/3dprinter-parts/products/pulley-16-tooth-gt2-10mm
[sh5]: https://www.v1e.com/collections/3dprinter-parts/products/20t-idler-gt2-10mm 
[sh6]: https://www.v1e.com/collections/3dprinter-parts/products/gt2-10mm-belt
[sh7]: https://www.v1e.com/collections/parts/products/limit-switch-endstop
[sh8]: https://www.v1e.com/collections/lowrider-parts/products/bearings-608-2rs 
[sh9]: https://www.v1e.com/collections/lowrider-parts/products/110mm-t8-leadscrew-and-nut 
[sh10]: https://www.v1e.com/collections/lowrider-parts/products/5mm-to-8mm-flex-coupler
[sh11]: https://www.v1e.com/products/150mm-mgn12h-linear-guides
[sh12]: https://www.v1e.com/products/24v-power-supply
[sh13]: https://www.v1e.com/collections/3dprinter-parts/products/0-5ml-threadlocker-242
[sh14]: https://www.v1e.com/collections/3dprinter-parts/products/super-lube-silicone-lubricating-grease-with-syncolon-ptfe 

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
[az11]: https://amzn.to/3PyAujr
[az12]: https://amzn.to/3Pe0P6m
[az13]: https://amzn.to/3GhaKmx
[az14]: https://amzn.to/31H7yS6
[az15]: https://amzn.to/38iqA4v

As an Amazon Associate, I earn from qualifying purchases.

### Hardware

This is what is needed for a 4' x 8' (1.2m x 2.4m) build. You will need more or less depending on what size you build.

|QTY  |Description             |US Equivalent                                  | 
|-----|------------------------|-----------------------------------------------|
|14   |M8 x 40mm               |5/16" x 1.5"                                   |
|14   |M8 Nylock nuts          |5/16" Nylock                                   |
|100  |M5 x 30mm               |Machine Screws                                 |
|100  |M5 Nylock               |None                                           |
|44   |M3 x 10mm               |Machine Screws                                 |
|10   |M2.5 x 12mm             |Machine Screws                                 |
|24   |3mm x 12mm Wood/metal   |#4 x 1/2" Wood or Sheet metal screws           |
|*22  |M4 x 12mm+ Wood/metal   |#8 x 1/2"+ Screws to mount things to your table|

* Not included in the hardware kit. 

### LR2 to LR3 hardware differences for updating your build
|QTY  |Description             |US Equivalent                                  | 
|-----|------------------------|-----------------------------------------------|
|14   |M8 x 40mm               |5/16" x 1.5"                                   |
|94   |M5 x 30mm               |None                                           |
|94   |M5 Nylock               |None                                           |
|36   |M3 x 10mm               |None                                           |
|10   |M2.5 x 12mm             |None                                           |
|24   |3mm x 12mm Wood/metal   |#4 x 1/2" Wood or Sheet metal screws           |
|22   |M4 x 12mm+ Wood/metal   |#8 x 1/2"+ Screws to mount things to your table|
|4    |150mm MGN12H Rails      |[Shop Link](https://www.v1e.com/collections/lowrider-parts/products/150mm-mgn12h-linear-guides){:target="_blank"}|
|3    |Wire Extenders          |[Shop Link](https://www.v1e.com/collections/lowrider-parts/products/wiring-kit-1){:target="_blank"}|

### Table

Your table needs only be as fancy as a sheet of wood on a relatively flat, smooth surface. A CNC can self correct many of its own imperfections if needed. Typically, our tables only support the CNC and some material, so nothing heavy duty is typically required.

Any existing table that is large enough is fine. You can use its surface directly, or a more popular option is to add a waste board of some sort that is replaceable as it gets used.

Next would be to build a basic table with any material that is easy to source for you. Accuracy is not super important, but the more square and flat you make it, the better.

If you have a table saw, circular saw with a guide, or a CNC machine, a Torsion Box table is pretty easy to make and can lead to a very stable surface that will last a long time. Here is a basic parametric set of plans that are easily configurable [V1 LR Table](https://forum.v1e.com/t/parametric-table/37698){:target="_blank"}.


![!LR3 Dimensions Picture](../img/lr3/LR3 Dims.jpg){: loading=lazy width="600"}

[Calculator for table, rail, and belt lengths.](calculator.md){:target="_blank"}


## Assembly

### YZ Plate Assemblies

 * Mount Back Whhels
 * Mount Z End Stop
 * Mount Y Stepper
 * Mount Front Wheels
 * Mount Linear Rails and XZ Plates
 * Mount Y Belt, and End Stop
 * Mount Z Axis
 * Mount Rail Rollers
 * Snug Z Endstop
 * Snug steppers (tighten just right)

### Core Assembly
 * X Drive
### Beam Assembly
### X Belt
### Y Rail
### Wire routing
### Y Belt

---

#### Initial Squaring

To square the machine you need to mark 4 points and measure the diagonal. This is how we set the Y axis homing to square the machine relative to the rail. You will probably need to repeat this a couple times to get it under 1mm difference.

You can cable tie a pen to the vacuum mount as shown below, or here is a pen mount that fits on most router bodies. [V1 Printables](https://www.printables.com/model/237997-basic-lr3-pen-mount){:target="_blank"}

You can also automate this process with Jamie's ["Squareness Marks"](https://vector76.github.io/gcode_tpgen/){:target="_blank"} test. 
 * Start with G92 X0 Y0 Z0 - Check this box and where the pen tip is will be 0,0,0. I suggest starting the pen just above the paper.
 * Z level for pen-down - Make this number more negative if you find some of your marks are not hitting the paper, but you want as light a touch as possible.
 * Z level for pen-up - You can go as high as you need to not drag the pen tip.
 * Feedrate - This is set at a safe travel rate.
 * Extents - This is where you set the dimensions of your table. The further apart the marks the more accurate your table will be.

![!LR3 Fancy Picture](../img/lr3/LR3 (81).jpg){: loading=lazy width="400"}

 * I use tape, so I can be sure I am using the correct mark.
 * Home the X and Y axis.
 * Use the Z axis to mark a small dot at 0,0.

![!LR3 Fancy Picture](../img/lr3/LR3 (82).jpg){: loading=lazy width="400"}

 * Now drive the machine to your X axis furthest point (or very close to it).
 * Use the Z to mark the dot.

![!LR3 Fancy Picture](../img/lr3/LR3 (83).jpg){: loading=lazy width="400"}

 * Drive to the Y extreme and repeat the process for the back two corners.

![!LR3 Fancy Picture](../img/lr3/LR3 (84).jpg){: loading=lazy width="400"}

 * Now measure the diagonals to the best of your ability. Note the longer one, and subtract to find the difference. Under 1mm is very good.

If you are over 1mm in difference you can use the terminal on your SKR Pro or a USB 
connection and repetier host to add a homing offset. "M666 Y0.5" will move your Y1 
stepper 0.5mm away from the stop block after it homes. "M666 Y-0.5" will move your 
Y2 stepper away instead. You want to move the longer dimension side away from the 
block. A good first guess is the difference in your measurements (or you can use a 
trig calculator and add a bit because your end stops are further away than the 
dots). Now Use "M500" to save it to the EEPROM. Re-home X and Y and test it again.

---

#### Z Leveling

![!LR3 Fancy Picture](../img/lr3/LR3 (85).jpg){: loading=lazy width="400"}

 * Z leveling is a bit easier than the Y axis if you have a touch plate. You can also use any sort of block or piece of paper as a feeler gauge. 
 * We are only looking for the difference here.

![!LR3 Fancy Picture](../img/lr3/LR3 (86).jpg){: loading=lazy width="400"}

 Steps
 
 1. Home all three of your axis.

 2. Get Readings
   * Touch plate
     * If you are using the touch plate, you probe by using G38.2 Z0. When it gets there, take note of the current Z position (M114). Then move it up and over to your X axis extreme and probe again, taking note of the Z axis position. Take the difference and adjust the side that moved furthest.
     * The way I have started to do this is Home and probe twice on each side. So G28 Z0, G38.2 Z0, M114, G28 Z0, G38.2 Z0, M114, Then move over G0 X1250, G28 Z0, G38.2 Z0, M114, G28 Z0, G38.2 Z0, M114. From there subtract the average of both sides, M666 Z0.5, M500. Then test again. G28 Z0, G38.2 Z0, M114, G28 Z0, G38.2 Z0, M114, Then move over G0 X1250, G28 Z0, G38.2 Z0, M114, G28 Z0, G38.2 Z0, M114.

   * Feeler Gauge
     * You will drive your Z axis down until you just make contact with the touch plate and take note of the current Z axis position. Repeat this for the other end of the X axis. Take the difference and adjust the side that moved furthest.

![!LR3 Fancy Picture](../img/lr3/LR3 (87).jpg){: loading=lazy width="400"}

 3. Make adjustments
   * You adjust by running "M666 Z0.5" the number is in millimeters. These numbers are counting down from 200, so 120 is further away than than 130. Start by adjusting 0.2mm more than your difference.
   * Save with M500 after each adjustment
   * Home all three axis and check your work (go back to Step #2). 

---

#### Making the Strut plates


!!! warning 
   NEED INFO
At this point you should be ready to make some cuts. To be certain it all goes as planned, you can 
make a test cut in high density foam, or simply making an air cut. To make an air cut you, just home 
your machine above the table and run the gcode. This lets you watch that it moves as you would 
expect it to and doesn't snag or have any faults in the code.

[Basic software setup](../software/estlcam-basics.md){:target="_blank"}

[Basic CAM settings](../tools/milling-basics.md){:target="_blank"}

Gcode making - TODO

The three strut plates should be 6.35mm (1/4") or thinner MDF or similarly rigid material.
You will want to cut each plate as close to the side of your build as you can to assure your build has the rigidity to do so.

![!LR3 Fancy Picture](../img/lr3/LR3 (88).jpg){: loading=lazy width="400"}

 * Getting ready to make your first cuts all starts with loading the material.

 * Make sure the edge is behind your Endmill in the Y direction and parallel with the edge in the X direction. 
 
![!LR3 Fancy Picture](../img/lr3/LR3 (89).jpg){: loading=lazy width="400"}

 * Checking the front and back edges relative to the table. (To the rail would be a more proper measurement)

![!LR3 Fancy Picture](../img/lr3/LR3 (90).jpg){: loading=lazy width="400"}

 * Secure the material and make sure your means will not interfere with the core as it passes over. I use screws with large heads.

![!LR3 Fancy Picture](../img/lr3/LR3 (91).jpg){: loading=lazy width="400"}

 * This is what a finished cut looks like. All parts are held in place with small tabs of material that can be cut with a saw or utility knife.
 * Do this two more times.

---

#### Disassembly

![!LR3 Fancy Picture](../img/lr3/LR3 (92).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (93).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (94).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (95).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (96).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (97).jpg){: loading=lazy width="400"}
---

#### Final Assembly

![!LR3 Fancy Picture](../img/lr3/LR3 (98).jpg){: loading=lazy width="400"}

* Measure the heel and toe distances across your machine, make sure they are equal. If not adjust the end clamps. Problems can arrise if your rails are too long after you install the strut plates.

![!LR3 Fancy Picture](../img/lr3/LR3 (99).jpg){: loading=lazy width="400"}
![!LR3 Fancy Picture](../img/lr3/LR3 (100).jpg){: loading=lazy width="400"}
---

### Vacuum
![!LR3 Fancy Picture](../img/lr3/LR3_Fancy (8).jpg){: loading=lazy width="600"}

Size, options, routing, grounding.  *to do

[Quick release coupler](https://www.printables.com/model/168405-vacuum-hose-coupler){:target="_blank"} for 1.5" hose.

### Wiring

Next step is [wiring the steppers](../electronics/steppers.md){:target="_blank"}.

### Using the machine.


### Firmware

Dual endstop LowRider "DualLR" firmware recommended for ultimate accuracy and precision. This requires 
at least a 5 driver control board. This allows you to align the Y axis and Z axis using dual endstops.

The standard MPCNC firmware will work with any board on the LowRider  if you are not using endstops or 
wired in series (using a 4 driver board). You will just use hardstops like the LR2 did.

[Firmware page.](../electronics/marlin-firmware.md){:target="_blank"}

### Build experience poll

[How did it go for you?](https://forum.v1engineering.com/t/lr3-how-many-hours-to-build-lr3/34307/2){:target="_blank"}

## Go get it dirty, be safe, have fun!
