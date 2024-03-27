# MP3DP v5 CoreXY

This is the 3rd CoreXY version for me, 5th printer design overall. This printer was a group effort and a direct result of everyone’s input, [Forum Thread](https://forum.v1e.com/t/help-develop-the-next-mp3dp/41947)

This is a CoreXY with easily machinable plates for ultimate rigidity where it counts but 3D printed parts where it does not matter to save from complicated multi-sided milling.

Belted Z axis, with free floating bed to allow for physical tilt correction as well as mesh correction, and possible non-planer printer in the future. Electronic brakes provide easy drop protection for the bed.

![!mp3dp v5](../img/mp3dpv5/printer.jpeg){: width="600"}

This first build of mine has a 300x300x200 build area, running Klipper, **Costs about $800**. [Forum Thread](https://forum.v1e.com/t/v5-1-the-plated-printer/42809).**


!!! Warning
    ### **Note for potential builders**

    If you are thinking about building a printer… a V1 Engineering CNC is an easy to intermediate build, a 3D printer is an advanced to expert build. A lot of personal build decisions need to be made, wiring is on the advanced end, firmware edits are required, CAD reference and possible edits are required, and overall build precision is higher.

    Because the builds vary, so wildly, instructions might not exist for the exact combination of hardware and electronics you choose. As always you can come here for help but if you chose random parts we might not have enough experience with them to help. If you are on the fence and want to tackle this, it would be best to follow my build exactly.


## Parametric Options

If you want a printer that is different than the standard build size, or has a custom extruder/hot end, you'll need to edit some parameters in the CAD file to generate the correct part sizes for your build.

[CAD link - Fusion](https://myhub.autodesk360.com/ue29a24ab/g/shares/SH512d4QTec90decfa6e972762faaa11c772).

This is how you adjust the model. Open the modify menu, Change parameters Menu.
![!Open Parameters](../img/mp3dpv5/Parameters%20-%20open.png){: width="600"}


### Build Size

!!! Note
    The Three Bed cut parts (Bed A-C) are the only parts that are size dependent. Make sure to set the correct build size before cutting these parts. 300X x 300Y is the default included size.

These three settings are how you adjust the size of the build. Z is not exact as it depends on the hotend you chose but it should be close.

![!Parameters - Usable](../img/mp3dpv5/Parameters%20-%20UsableSize.png){: width="600"}

**Note: The CAD will fail if you go up and down in size. Make one edit and it should be fine. If you have an issue, start fresh.**

### Optional hole size

This lets you adjust the hole size for the Plates to frame.

 I was asked to allow for M5 hardware. This is where you do that. You will need to export new DXF files for the corners and tensioner parts.

![!Parameters - Hole Size](../img/mp3dpv5/Parameters%20-%20AdjustableHoleSize.png){: width="600"}

### Belt Grip

If you want to make the Belt have a tighter or looser grip on the core bottom or Z top pieces, you can change it here.

![!Parameters - Belt Grip](../img/mp3dpv5/Parameters%20-%20BeltGrip.png){: width="600"}

## CAD Help

### Exporting DXFs

If you want to export your own DXF’s this is where you find them.

![!DXF Export](../img/mp3dpv5/DXF%20Export.png){: width="600"}

## BOM

### Flat Parts

The flat parts are designed for you to be able to mill them yourself with your MPCNC or LowRider out of 3/16" (4.7mm) aluminum. 

!!! Note
    The Three Bed cut parts (Bed A-C) are the only parts that are size dependent. Make sure to set the correct build size before cutting these parts. 300X x 300Y is the default included size.

|QTY |File Name                   |Comment                              |Link                                     | 
|----|----------------------------|-------------------------------------|-----------------------------------------|
|2   |Corner Top                  |                                     |                                         |
|2   |Corner Stepper              |                                     |                                         |
|2   |Truck Rail                  |                                     |                                         |
|2   |Truck Top                   |                                     |                                         |
|3   |Z Front                     |                                     |                                         |
|3   |Z Back                      |                                     |                                         |
|4   |Tensioner                   |                                     |                                         |
|1   |Bed A                       |                                     |                                         |
|1   |Bed B                       |                                     |                                         |
|1   |Bed C                       |                                     |                                         |

### Printed Parts

No supports needed, keep the default orientation. 
PLA is recommended for ultimate rigidity, other filaments should be evaluated for rigidity.
2-3 walls 
rectilinear infill. 


|QTY |File Name                   |Infill |Comment                              |Link                                     | 
|----|----------------------------|-------|-------------------------------------|-----------------------------------------|
|1   |Core Top*                   |55%    |                                     |                                         |
|1   |Core Bottom*                |55%    |                                     |                                         |
|3   |Z Belt Lower                |40%    |                                     |                                         |
|3   |Z Belt Upper                |40%    |                                     |                                         |
|3   |Z Stepper - Z Bearing Mount |40%    |                                     |                                         |
|6   |Z Stepper - Z spacer        |40%    |                                     |                                         |
|3   |Z Stepper - Bed Mount       |40%    |                                     |                                         |
|2   |Y Truck                     |40%    |                                     |                                         |
|4   |Y Truck - spacer            |40%    |                                     |                                         |
|2   |X Rail - Nut holder         |40%    |                                     |                                         |
|4   |Rear Spacer                 |40%    |                                     |                                         |
|1   |Smoother                    |40%    |                                     |                                         |
|2   |Front Spacer                |40%    |                                     |                                         |

### Frame

The frame is built with 2020 extrusion.

Cuts should be planned carefully to reduce waste. A site like [Opticutter](https://www.opticutter.com/linear-cut-list-calculator) can be used to verify the amount necessary for your printer size.

**It is highly recommended that you calculate this before ordering your extrusion to reduce potential extra cost**

#### Extrusion List

There are 20 total pieces of extrusion that need to be cut

|QTY |Name                   |
|----|----------------------------|
|6   |Y Rails                     |
|5   |X Rails                     |
|4   |Z Uprights                  |
|3   |Z Linear Rail Mount         |
|1   |Bed Support 1               |
|1   |Bed Support 2               |

*Cut all extrusions 2-3mm short. This lets you have not perfect cuts and still build an extremely accurate frame.

### Bed Parts

### Extruder


### Frame

2020 Extrusion - [Amazon](https://amzn.to/3P7TBCl)

### Electronics

### Hardware

## Assembly

### Frame

The process is very similar for a corner bracket frame. Panels are easier to build but harder to make.

Building on a very flat and solid surface will make this part easier.

Frame parts and tools. We will start with the back panel.

![!image](../img/mp3dpv5/FrameAssembly1.jpeg){: width="600"}


Load up the t-nuts. It's important at this stage to insert all t-nuts that will be necessary if you are using the trapped t-nuts instead of twist-ins. I only use twist in’s when I forget to load one in.

![!image](../img/mp3dpv5/FrameAssembly2.jpeg){: width="600"}

Slide the extrusion on. Going to use this same process a lot.

![!image](../img/mp3dpv5/FrameAssembly3.jpeg){: width="600"}

Top and bottom

![!image](../img/mp3dpv5/FrameAssembly4.jpeg){: width="600"}

Load in the trapped Tnuts (if you are not using twist in’s).

![!image](../img/mp3dpv5/FrameAssembly5.jpeg){: width="600"}

Add the other rails, load in more trapped T nuts. Remember top and bottoms as well.

![!image](../img/mp3dpv5/FrameAssembly6.jpeg){: width="600"}

Add last rear rail. Verify all dimensions, Diagonals are very important as well (cut ends are not accurate to measure from so inside corner to inside corner works best).

![!image](../img/mp3dpv5/FrameAssembly7.jpeg){: width="600"}

Verify Z rail location to the CAD dimensions. Do yourself a favor and get them all very accurate.

![!image](../img/mp3dpv5/FrameAssembly8.jpeg){: width="600"}

![!image](../img/mp3dpv5/FrameAssembly9.jpeg){: width="600"}

Build out the side panels, stop at this point to load in trapped T Nuts.

![!image](../img/mp3dpv5/FrameAssembly10.jpeg){: width="600"}

![!image](../img/mp3dpv5/FrameAssembly11.jpeg){: width="600"}

Verify verify dims

![!image](../img/mp3dpv5/FrameAssembly12.jpeg){: width="600"}

Load in the Nuts for attaching the sides

![!image](../img/mp3dpv5/FrameAssembly13.jpeg){: width="600"}

![!image](../img/mp3dpv5/FrameAssembly14.jpeg){: width="600"}

You can slide the sides in to get ready for the bottom.

![!image](../img/mp3dpv5/FrameAssembly15.jpeg){: width="600"}

Add the front bottom rail to the bottom panel.

![!image](../img/mp3dpv5/FrameAssembly16.jpeg){: width="600"}

Attach the bottom and check all the dimensions again, snug up the screws. Check every diagonal you can.
I stop here to add the hardware in while it is easy to reach in. If you are building a corner bracket frame feel free to build the whole cube.

![!image](../img/mp3dpv5/FrameAssembly17.jpeg){: width="600"}

### XY Gantry
