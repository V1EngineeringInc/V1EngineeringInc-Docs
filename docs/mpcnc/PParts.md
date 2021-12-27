# MPCNC Primo Parts

## Printed Parts Sizes
There are 3 different sets of printed parts C-23.5mm, F-25mm, or J-25.4mm (1 inch). The measurement is for the **Outside Diameter** of the conduit/rails/tubing. Please measure your rails before printing! 23.5mm fits ¾″ EMT conduit in the US. Anywhere else you must physically measure first. Some things are sold as Inside Dimension (ID) (conduit), or Outside Dimension (OD) (tubing).

Hardware store steel EMT conduit works well and is inexpensive; an upgrade would be .065” (max is 0.120") wall thickness stainless steel tubing or DOM. Stainless steel tubing is more rigid and smooth, but also much more expensive, Dom is less expensive than Stainless but requires some coating to prevent rust.

## Recommendations
Recommended Print Settings: PLA for dimensional accuracy (PETG is also acceptable, if your dimensions are verified good and you are willing to sacrifice some rigidity). Two or more perimeters for through hole strength. There are some steep walls so no more than 75% layer height to nozzle diameter. 
**No support should be needed for any part I have designed.**

!!!Note
     If your 3D printer is of questionable quality it is best to run a quick [basic frame test](https://www.prusaprinters.org/prints/36412-xy-size-and-square-calibration-print) to make sure the parts will print as intended.  If the test indicates that your frame is not square, then carefully check the frame and adjust, and retest.  If you have to square the frame, then you might also consider printing the [Advanced frame test](https://www.prusaprinters.org/prints/38846-zx-and-zy-printer-frame-test). Investing time on this up front is much better than printing parts for four days and then finding that your calibration or frame is off. 

| Files can be found at                                    |                                                                           |                                                         |
|----------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------|
| [GitHub](https://github.com/V1EngineeringInc/MPCNC_Primo) | [PrusaPrinters](https://www.prusaprinters.org/social/47417-ryan-z/prints) | [Thingiverse](https://www.thingiverse.com/allted/about) |

## Primo Printed Parts List

| QTY | Part Name              | Infill | Color |
|----:|------------------------|--------|-------|
|     | **Corner**             |        |       |
|   2 | Corner Bottom          | 45%+   |   B   |
|   2 | Corner Bottom Mirrored | 45%+   |   B   |
|   2 | Corner Top             | 45%+   |   A   |
|   2 | Corner Top Mirrored    | 45%+   |   A   |
|   2 | Lower Belt             | 45%+   |   A   |
|   2 | Lower Belt Mirrored    | 45%+   |   A   |
|   2 | Upper Belt             | 45%+   |   B   |
|   2 | Upper Belt Mirrored    | 45%+   |   B   |
|   4 | Corner Leg Lock        | 45%+   |   B   |
|   4 | Feet                   | 45%+   |   A   |
|   2 | Wire Darryl            | 45%+   |   A   |
|   4 | Stop Block (Dual only) | 45%+   |   A   |
|     | **Trucks**             |        |       |
|   2 | Truck                  | 45%+   |   A   |
|   2 | Truck Mirrored         | 45%+   |   A   |
|   4 | Truck Clamp            | 45%+   |   B   |
|     | **Z-Axis**             |        |       |
|   1 | Z Motor                | 45%+   |   A   |
|   1 | Z Coupler              | 45%+   |   A   |
|   2 | Nut Trap               | 45%+   |   A   |
|   1 | Upper Tool Plate       | 45%+   |   A   |
|   1 | Lower Tool Plate       | 45%+   |   A   |
|     | **Center Assembly**    |        |       |
|   2 | Core Z Clamp 1         | 45%+   |   A   |
|   2 | Core Z Clamp 2         | 45%+   |   A   |
|   3 | Core Clamp             | 45%+   |   A   |
|   1 | Core ClampY            | 45%+   |   A   |
|   1 | Core                   | 70%    |   B   |

A tool mount is also needed for your specific tool. A list of mounts I have designed are [below](#spindle-options). You can also find user designed mounts on PrusaPrinters and Thingiverse by searching "MPCNC Primo" and your tool name.

Color is the default color scheme I use to print the kits. Color `A` is one color of filament, and
`B` is the second color of filament.

!!! Note
     The core can be printed with variable infill to save time and plastic. 70%/30%/70% split at 24mm and 116mm.

Total weight in PLA is approximately 2.2kg.

#### Print time
Print times have varied from 65hrs (0.5mm nozzle @38mm/s), to 120hrs (0.4mm @60+mm/s), and 160hrs (0.4mm nozzle @35mm/s).
___

## Hardware

The kits in the [V1 Shop](https://shop.v1engineering.com/collections/parts) contain all of the following hardware. Currently it is not available separately.

| Hardware     | Type  | Alternative | QTY |
|--------------|-------|-------------|-----|
| 5/16x1.5"    | Bolt  | M8x40mm     | 44  |
| 5/16 locknut |       | M8 locknut  | 44  |
| M5x30mm      | Screw |             | 60  |
| M5 locknut   |       |             | 60  |
| M3x10mm      | Screw |             | 22  |
| M2.5x12mm    | Screw | #3x1/2"     | 8   |

This version uses both sizes of hardware equally well. No issues with metric bolts whatsoever.

!!!Note
     Bolts need to be hex head, screws pan head. If you choose to use cap head you will need washers and perhaps a little extra length.

___

## Components

The kits in the [V1 Shop](https://shop.v1engineering.com/collections/parts) contain all of the following components.
Some of these are affiliate links, you can buy from these links or just use them for information.

!!! note
    I try to keep the Amazon links up to date, but they can sometimes change products without
    changing the item number. So be careful when looking at these links to compare against
    the offerings in the shop. If you're not sure, drop a question in the forums.

| Part                | QTY | V1 Link                                                                                                                              | Other Link                                                |
|---------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Nema 17 50OZ/in+    | 5   | [Shop](https://shop.v1engineering.com/collections/parts/products/nema-17-76oz-in-steppers)                                           | [Amazon](https://amzn.to/3hQKILc)                         |
| * Belt GT2 10mm     | 4   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/gt2-10mm-belt)                                             | [Amazon](https://amzn.to/2V5pfo8)                         |
| Pulley 16t gt2 10mm (5mm bore) | 4   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/pulley-16-tooth-gt2-10mm)                                  | [Amazon](https://amzn.to/2VmDWTR)                         |
| Idler 20t gt2 10mm  (5mm bore)| 8   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/20t-idler-gt2-10mm)                                        | [Amazon](https://amzn.to/37TNJWh)                         |
| Power Supply        | 1   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/12v-6a-power-supply)                                       | [Amazon](https://amzn.to/2Cwlp0M)                         |
| Wiring kit          | 1   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/wiring-kit-1)                                              | Custom Made for V1                                        |
| Bearings            | 45  | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/bearings-608-2rs)                                          | [Amazon](https://amzn.to/2Cxe7tJ)                         |
| leadscrew/nut       | 1   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/300mm-leadscrew-and-nut)                                   | [Amazon](https://amzn.to/2V7wUSK)                         |
| 5mm to 8mm Coupler  | 1   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/5mm-to-8mm-flex-coupler)                                   | [Amazon](https://amzn.to/2APIifi)                         |
| Lube                | 1   | [Shop](https://shop.v1engineering.com/collections/lowrider-parts/products/super-lube-silicone-lubricating-grease-with-syncolon-ptfe) | [Amazon](https://amzn.to/2BzXbC7)                         |
| Control Board       | 1   | [Shop](https://shop.v1engineering.com/collections/parts)                                                                             | [Ultimachine](https://ultimachine.com/products/rambo-1-4) |

* Use the [calculator](calculator.md) to determine belt length.

As an Amazon Associate I earn from qualifying purchases.

!!!Caution
     Do not use Steel reinforced belts, they will fail 100% of the time. Fiber reinforced only.
___

## Spindle Options

Currently I have made mounts for the preferred [Makita RT701c](https://amzn.to/2ZA9Lde) (it mounts a bit closer, a bit more power, and has a built in speed control), or the less expensive [Dewalt 660](https://amzn.to/2Z3yaHC).

Other options would be the [55mm spindle](https://amzn.to/2BsxX8S) (57mm caps), the least attractive option is the [52mm spindle](https://amzn.to/2BtIFvO).

Internationally there are many options with lots of user submitted mounts, take a look at the file links below or ask for a local suggestion in the forums.


| Mount Files can be found at                                           |                                                                           |                                                         |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------|
| [GitHub](https://github.com/V1EngineeringInc/MPCNC_Primo_Tool_Mounts) | [PrusaPrinters](https://www.prusaprinters.org/social/47417-ryan-z/collections/26592) | [Thingiverse](https://www.thingiverse.com/allted/about) |


More to come.

___

## Tool Mounts

You are able to use tool mounts originally designed for the Burly MPCNC, you just need to use the Burly tool mount and nut traps.

* Blank tool mount, [HERE](https://github.com/V1EngineeringInc/MPCNC_Primo_Tool_Mounts/tree/master/Blank%20Mounts), to design your own.

!!! Note
    The blank tool mount needs details.

___

### Update from Burly to Primo

Kits are available in the [V1 Shop](https://shop.v1engineering.com/products/mpcnc-burly-to-primo-hardware-kit).

| Part                               | QTY |
|------------------------------------|-----|
| 10mm GT2 Pulleys                   | 4   |
| 10mm GT2 20T Idlers                | 8   |
| 5/16"x1.5" Bolts (M8x40mm)         | 46  |
| 5/16" Nylock (M8)                  | 1   |
| M5x30mm Phillips Pan Head Screws   | 64  |
| M5 Nylocks                         | 64  |
| M2.5x12mm Phillips Pan Head Screws | 10  |
| *10mm GT2 belt.                    | ?M  |

*While you can use your 6mm belt, I suggest you upgrade to 10mm belt. Use the [calculator](calculator.md) for the amount you need.
