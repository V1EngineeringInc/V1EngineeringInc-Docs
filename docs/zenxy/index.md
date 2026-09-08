# ZenXY v3

COMING SOON

## Pattern Software

**Sandify**

![!Sandify](../img/old/2019/01/screenshot-2019-01-02-1546472560.png){: loading=lazy width="450"}

Amazing patterns are easily possible by using [Sandify.org](https://sandify.org/), the back end is here [Sandify on GitHub](https://github.com/jeffeb3/sandify),
This table would be nothing without this tool! ([feel free to show some appreciation for this amazing free piece of
software](https://liberapay.com/jeffeb3/)).


## Bill of Materials

1- You will need to buy or build a table, usually suited to fit two pieces of tempered glass.

2- A full set of printed parts, buy from the [V1 Shop](https://www.v1e.com/products/zenxy-v3-printed-parts-set), or 3D Print your own [Printables](link).

3- You can buy most of the other specialty parts and hardware here, [V1 Shop](https://www.v1e.com/collections/zenxy){:target="_blank"}

|QTY  |Description             |Comment                                        |Link                        | 
|-----|------------------------|-----------------------------------------------|----------------------------|
|1    |Control Board           | 5 driver minimum, More info below             |[Shop][sh1] – [Elecrow][am1]|
|2    |Extrusions              | Length info below - V-Slot 20/20              |[Shop][sh2] – [Amazon][am2]|
|2    |Steppers                | Nema 17, most any torque will work            |[Shop][sh3] – [Amazon][am3]|
|1    |Power Supply            | 12-24v (board dependant) ~0.5A+               |[Shop][sh4] – [Amazon][am4]|
|3    |V-Wheel Blocks          | 50mm                                          |[Shop][sh5] – [Amazon][am5]|
|2    |Pulleys GT2             | 6mm width, 5mm bore, 16T+                     |[Shop][sh6] – [Amazon][am6]|
|6    |Smooth Idlers GT2       | 6mm width, 3mm bore, 20t                      |[Shop][sh7] – [Amazon][am7]|
|2    |Toothed Idlers GT2      | same as above, or use smooth idlers           |[Shop][sh8] – [Amazon][am8]|
|1    |Belt                    | GT2 6mm, More info below                      |[Shop][sh9] – [Amazon][am9]|
|1    |Magnet                  | 1/2" x 1/2" Neo                               |[Shop][sh10] – [Amazon][am10]|
|1    |Steel Ball              | 1/2"                                          |[Shop][sh11] – [Amazon][am11]|
|8+   |Cable Ties              | 40lb, 3.5mm                                   |[Shop][sh12] – [Amazon][am12]|
|4    |Extrusion Screws        | M5x10                                         |[Shop][sh13] – [Amazon][am13]|
|4    |Extrusion T-Nuts        | Fit 20 Series                                 |[Shop][sh14] – [Amazon][am14]|
|20   |M3x20                   | Phillips Pan Head                             |[Shop][sh15] – [Amazon][am15]|
|7    |M5x25                   | Phillips Pan Head                             |[Shop][sh16] – [Amazon][am16]|
|13   |Attachment screws       | Truss Head, Suited to your build and material |[Shop][sh17] – [Amazon][am17]|
|2    |Optical Endstops        |                                               |[Shop][sh18] – [Amazon][am18]|
|1    |                        |                                               |[Shop][sh19] – [Amazon][am19]|

[sh1]: https://www.v1e.com/products/jackpot3-cnc-controller
[sh2]: 
[sh3]: https://www.v1e.com/products/nema-17-76oz-in-steppers
[sh4]: https://www.v1e.com/products/24v-power-supply
[sh5]: 
[sh6]: 
[sh7]: 
[sh8]: 
[sh9]: 
[sh10]: https://www.v1e.com/products/1-2-x-1-2-magnet
[sh11]: https://www.v1e.com/products/1-2d-steel-ball
[sh12]: 
[sh13]: 
[sh14]: 
[sh15]: 
[sh16]: 
[sh17]: 
[sh18]: https://www.v1e.com/products/optical-endstop
[sh19]: 

[am1]: https://m.elecrow.com/pages/shop/product/details?id=207484&
[am2]: https://amzn.to/4hgWH5l
[am3]: https://amzn.to/3UHJRnX
[am4]: https://amzn.to/4heYojI
[am5]: https://amzn.to/3ULxNC8
[am6]: https://amzn.to/4d2j2RG
[am7]: https://amzn.to/4r1Ycru
[am8]: https://amzn.to/3VjA1J3
[am9]: https://amzn.to/3TkLmIn
[am10]: https://amzn.to/4r9L9Ew
[am11]: https://amzn.to/4hi3iMQ
[am12]: https://amzn.to/3UItYO6
[am13]: https://amzn.to/4xpGNuw
[am14]: https://amzn.to/4xpGNuw
[am15]: https://amzn.to/3VjCkMd
[am16]: https://amzn.to/4qXF51z
[am17]: https://amzn.to/4yp4sMa
[am18]: https://amzn.to/4gRmZJZ
[am19]:

___

## Control Board

There are a lot of options.

Any board with two drivers or more with firmware capable of running CoreXY, and TMC silent stepper drivers are highly recommended.

**[TMC2209 Pen/Laser Controller](https://m.elecrow.com/pages/shop/product/details?id=207484&)** -  by Bart Dring, seems 
to be a perfect match for the Zen. This board has the silent 2209 drivers, and the esp32 has a built-in web interface for wireless
control and file transfer.

### Firmware

This is running CoreXY kinematics and requires homing Y before X, as set in the firmware. All firmware will also need the exact size of your 
build's work area using soft limits to stop from crashing with bad gcode. The only other thing to set is homing and max speeds depending on what you prefer.

Here is an example FluidNC TMC2209 Pen/Laser Controller Firmware config file [Semi Pre-Configured GitHub Repo](https://github.com/V1EngineeringInc/FluidNC_Configs).


## Calculator for Extrusions, Belt, Glass


## Example table

## Assembly

## Wiring

 :smile:.


## Example Starting Gcode

When using Sandify, or any other software you usually need to set the starting or homing Gcode. You can cut and paste what is below and adjust for your specific build if needed. 

For FluidNC/GRBL you can use
```
$HY
$HX
G1 F2000
```

For Marlin it would be
```
G28 Y
G28 X
G1 X1 F2000
```
Here is a Human readable version of that
```
Move the Y axis all the way to the trigger.
Move the X axis until it triggers.
Set the move speed to 2000mm/min (33mm/s). 
```

## ZenXY v2 to ZenXY v3

If you want to use your previous table and retrofit a new machine it is possible. The ZenXY v3 has a slightly smaller footprint so you can use the offset templates when installing the new corner parts to make it easy.

You can use your same control board, steppers, end stops, magnet and ball, the rest of the printed parts and hardware are different.

Parts link - 

Picture - 

## Adding WLED



## License

If you like our work or want to sell sand tables your support is appreciated. Donation links, [Github Sponsor](https://github.com/sponsors/V1EngineeringInc), PayPal(https://www.paypal.com/donate/?hosted_button_id=LAXN6LWJMB3QS) 

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa] 

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
