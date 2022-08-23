# This is an Inexpensive CNC Platform
![!MPCNC Render](https://www.v1engineering.com/wp-content/uploads/2020/06/Primo-scaled.jpg){: loading=lazy width="450"}
 
## The Mostly Printed CNC

The Mostly Printed CNC (MPCNC) is a platform to precisely control motion. This can easily be a milling machine, 3D router, 3D printer, laser cutter, vinyl cutter, CNC plasma cutter, you name it.

## Cost

All components are easily sourced, or you can buy the parts from this site. Here is a price breakdown.

* The [Bundle](https://shop.v1engineering.com/collections/parts/products/mostly-printed-cnc-parts-bundle-primo-version) has all the hardware, electronics, and control board, everything except the [conduit/rails](https://docs.v1engineering.com/mpcnc/calculator/) which are cheaper to source locally than to ship – $353 + shipping if international.
* 20′ of [Conduit](https://docs.v1engineering.com/mpcnc/calculator/) **≈\$12** (or stainless-steel tubing or DOM Tubing for a little more ≈\$65) .
* Plastic parts, filament, less than 2 spools **≈\$35** if you own a 3D printer. If not, buy the printed parts from [here](https://shop.v1engineering.com/collections/parts) for $165.
* Tool. Either a [Dewalt](https://amzn.to/1MoBSQq), [import spindle](https://amzn.to/3dkKgl0) or an [extruder](https://amzn.to/37ZjygN) (3D Printer) $63, or anything else you might want to bolt on, [laser](https://amzn.to/37OcdQK), [drag knife](https://shop.v1engineering.com/collections/parts/products/drag-knife-vinyl-cutter), foam cutting needle (awesome), etc.

Total Cost… if you have a 3D printer Under $465, $595 if you buy the printed parts from here.


I would like to drive that price home one more time. You can have a CNC router for precision work ([here](https://forum.v1engineering.com/t/mrrf-2018-ideas/7112/55), [here](https://forum.v1engineering.com/t/pcb-examples/4015/27) all the way up to [aluminum milling](https://forum.v1engineering.com/t/lionkevs-aluminum-attempts/6047/101?u=vicious1) and [plasma cutting](https://forum.v1engineering.com/t/plasma-build/5662) steel for under $600. That is all you need to spend, throw in a few endmills and you are still under $620.  **There is no other machine more versatile than the Mostly Printed CNC at any price point.**


## Specs…

Not easy to make a specs page when it can have almost any specs you want. The idea behind this is to be extremely adaptable and inexpensive. Why buy a single use machine when you can have one that does it all for less than the cost of any single function machine. No proprietary hardware or software, build it any size and shape you want (more on this later), buy it from this site or source it all yourself, helpful forums, low cost, and capable. What more could you ask for?

<iframe width="560" height="315" src="https://www.youtube.com/embed/qJfYTv88YvI"
  title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
  clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  
This machine can easily do many things, how about making some coffee with Apach…(not me but I think he is my new hero).

 
## Size

- All axes can be any length you prefer, anything over 3 1/2′ (1M) would require small mid-span supports to increase rigidity, of course smaller is better.  The kit comes with enough belt for up to 48″ of total outer X and Y axis dimensions (eg 24″x24″, 36″x12″ or any other combination).

- The smaller you make this the faster you can move it and the more rigid/accurate it will be, and more importantly the easier it will be to get the desired accuracy.

- The linear motion is ball bearings on electrical conduit (or stainless steel)… seriously, easy to use and source. More information on this [here](https://www.v1engineering.com/assembly/machine-size/). If this machine isn’t big enough I have also designed the [LowRider CNC](../lowrider/index.md), all the same specs and resolution just designed to be bigger!
 
## Power

- X and Y axis are powered by 2 stepper motors each, and a single stepper for the Z axis. The standard would be NEMA 17 in any torque preferably 42 OZ/in and above (the kit comes with 76 OZ/in). No need for NEMA 23’s or their required larger drivers,  torque is not one of this machines issues.

- Belts are used for their accuracy and price. Small belts are used because each axis has two of them. Ball screws are expensive, require tuning, and periodic maintenance / adjustments.

 
## Control

- This is all controlled by any control board you like. The UltiMachine boards are recommended for the improved design and robust safety features. You can still use the common Ramps 1.4 or any other boards as well. There are other [Marlin](https://github.com/MarlinFirmware/Marlin) based boards, [GRBL](https://github.com/grbl/grbl), and regular CNC boards as well.

 
## Software

- There are plenty of free or really inexpensive software options available for 3D printing, CAM, and CAD. I suggest [Fusion 360](http://www.autodesk.com/products/fusion-360/overview), [Repetier-host](http://www.repetier.com/), [ESTLCam](http://www.estlcam.com/), etc.

 
## DIY

- Besides using either common imperial or metric hardware, the rest of the machine is easily 3D
    printable, RepRap style! A full list of required hardware can be found [here](PParts.md#hardware), and the files for the printed
    parts can be had [here](PParts.md).

- All of these things can be easily assembled with basic hand tools, no specialty tools, power tools, or precision cuts required.

![!Simple MPCNC](https://www.v1engineering.com/wp-content/uploads/2015/07/IMG_20150802_16352001.jpg){: loading=lazy width="450"}
![!Fancy MPCNC](https://www.v1engineering.com/wp-content/uploads/2018/04/IMG_20180409_184626.jpg){: loading=lazy width="450"}
[Build Thread](https://forum.v1engineering.com/t/red-black-and-wheels/7303)

## More info

To see some of the capabilities, and some interesting builds check out some [videos](https://www.v1engineering.com/videos/), or the user galleries, [MPCNC gallery](https://forum.v1engineering.com/tag/gallery-mpcnc), [LowRider CNC gallery](https://forum.v1engineering.com/tag/gallery-lowrider-cnc).
