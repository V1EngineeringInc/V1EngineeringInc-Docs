# SKR Pro V1.1 & V1.2


## Basics

The SKR Pro is a 32bit 6 driver board with 6 easily controllable ports running at 12-24V. Beyond the
basics there are loads of extra pins, options for two different power supplies at two different
voltages, WiFi Ports, future expansion port for USB, and the Trinamic TMC series of drivers are all
pre wired into the board so there are no extra wires needed.

**Want to Buy one?**

[SKR Pro Bundle is available here in the shop.](https://shop.v1engineering.com/collections/parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3)

There are many options involved here. To offer the best experience for most users and I have settled
on the TMC2209 drivers, and the TFT35 V3 E3 screen.

![!SKR Bundle](https://www.v1engineering.com/wp-content/uploads/2020/07/srkbundle.jpg){: width="400"}

## 2209 Drivers

The Trinamic 2209 V1.2 drivers offer UART communication for dynamic control, 2A RMS with a 2.8A
peak. We will be operating far under these values. The Trinamic drivers have many advanced features.
For a CNC Machine, the main features we use are digital current control and dynamically lowering the
hold current so we can also keep stepper and driver heat down while operating at slightly higher
than usual stepper power!

### Disable Sensorless Pin

Sensorless homing is not currently as accurate as mechanical end stops. All the pre-compiled
firmware has this disabled so you will need to bend the pins out of the way.

![!2209 bend](https://www.v1engineering.com/wp-content/uploads/2020/07/sensorles-bend.jpg){: width="400"}

Bend this pin on each driver to allow mechanical switches to be used on the SKR board.

### UART

For the firmware to be able to control the current and receive feedback from each driver the board
needs to be set for UART communication. To do this you remove the 4 jumpers from each port and place
one jumper on the black (UART) pins. **There is no need to monkey with the tiny potentiometers!**

![!Highlighted uart pins](https://www.v1engineering.com/wp-content/uploads/2020/07/uart2-Arrows.jpg){: width="400"}

The completed board looks like this. Notice there are no jumpers under the drivers.

![!Uart pins](https://www.v1engineering.com/wp-content/uploads/2020/07/Uart-scaled.jpg){: width="400"}

At this point you can add the heat sinks being careful not to short any of the pins and only stick
them to the copper pads on the top.

## Wiring Steppers

We have a few options for how the steppers get connected to this board. Here are the three most
common ways we might use it.

### Series

The standard LowRider and MPCNC options are to use series wiring. This combines two steppers on the
same driver. This increases the voltage demand and not the current. We have an abundance of
available voltage. The board is labeled and we will be using X, Y, and Z.

![!Series](https://www.v1engineering.com/wp-content/uploads/2020/07/Series-skr-labels-scaled.jpg){: width="400"}

### Dual End Stops (EXTRUDERS=0)

If the firmware is set for EXTRUDERS=0 then E0 becomes X2 and E1 becomes Y2. (or LR would be E0=Y2
E1=Z2)

![!dual 0](https://www.v1engineering.com/wp-content/uploads/2020/07/dual2-scaled.jpg){: width="400"}

### Dual End Stops (EXTRUDERS=1)

For EXTRUDERS=1 E0 is used and then E1 becomes X2 and E2 become Y2. (or LR would be E1=Y2 and E2=Z2)

![!dual 1](https://www.v1engineering.com/wp-content/uploads/2020/07/Dual-Ex-1-scaled.jpg){: width="400"}

### Reversing a stepper

If your stepper is moving the wrong way you can power down and flip the plug over to change the
direction of rotation. If you are using the series wiring harness flipping the board end changes
both stepper, or changing one stepper in the chain reverse that one only.

![!flip 1](https://www.v1engineering.com/wp-content/uploads/2020/07/flip1-scaled.jpg){: width="400"}
![!flip 2](https://www.v1engineering.com/wp-content/uploads/2020/07/flip2-scaled.jpg){: width="400"}

## Screen TFT35 V3 E3

This screen was chosen because it had a knob (great for dirty environments). We can use it from both
Touchscreen mode and Classic mode, simultaneously. **Switching between modes is as easy as pressing
the knob in for 3 seconds.**

![!screen](https://www.v1engineering.com/wp-content/uploads/2021/01/lcd-touch-Labels-scaled-1.jpg){: width="400"}

You do not need to use both, pay attention to the direction the wires are facing when connecting
them.

## Touch plate

All the V1 firmware is ready for a touch plate. Easy as plugging into the Z min port.

![!Probe](https://www.v1engineering.com/wp-content/uploads/2020/07/Z-probe-scaled.jpg){: width="400"}

## Dual End Stops, End Stops

If you are running the dual endstop firmware you will need to have your endstops wired in Normally
Closed (NC). You will plug into the Signal and Ground pins, **Do not use the + pins.**

![!endstops](https://www.v1engineering.com/wp-content/uploads/2020/07/endstops-scaled.jpg){: width="400"}

!!! note
    Do not use the + (positive) pins or you will ruin your SKR Pro board.

## Firmware

The SKR Pro and TFT screen both can use a bin file to re-flash the firmware. This is as simple as
placing some files directly on the memory card and rebooting them.

### SKR Bin

You have three options of firmware for the exact board, driver, screen package as sold in the V1 store.

* V1CNC_SkrPro_2209-****** Ready for series wiring on any CNC build.
* V1CNC_SkrPro_Dual_2209-****** Ready for dual end stops on an MPCNC (X & Y axes).
* V1CNC_SkrPro_DualLR_2209-****** Ready for dual end stops on a LowRider CNC (Y & Z axes).

When you unzip the file you have a .bin file. Rename to FIRMWARE.bin, and save it to the MicroSD for the SKR Pro board. Make sure to unplug both grey exp1/2 cables for the screen before proceeding. Insert the MicroSD back into the control board, reset, and the board will flash a few green LED's for a second or two. The board now has new firmware (seriously that easy). 

![!SKR file](https://www.v1engineering.com/wp-content/uploads/2020/08/SKR_Bin.jpg){: width="400"}

The file will change extensions when a successful flash happens.


Current release bin files, [V1 Engineering pre-configured firmware](https://github.com/V1EngineeringInc/MarlinBuilder/releases).

You also have the option to get the full Marlin source and edit and compile yourself using [Platformio Docs](../learn/platformio.md).


### TFT Files

Flashing the screen takes a .bin file, the config file, and usually the TFT35 folder (unzipped) on the root of the screens SD card.

You can get these file from the link at the end of this section below. OR here is a [zip file](https://github.com/V1EngineeringInc/BIGTREETECH-TouchScreenFirmware/blob/master/TFT_E3V3_1_7_21.zip), make sure to unzip it first.

BIGTREE_TFT35_V3.0_E3.****.bin
config.ini
TFT35 (folder) you do not need the folder present for minor updates it is just for graphics and languages.

![!TFT files](https://www.v1engineering.com/wp-content/uploads/2020/08/TFT35_bin.jpg){: width="400"}

Now reset the screen (or board) and watch the screen update itself. You can double check and the files will have a new extension after a successful flash.

The V1 Engineering CNC version of the TFT firmware is in this [release](https://github.com/V1EngineeringInc/BIGTREETECH-TouchScreenFirmware/releases/tag/V1-Vx.x.26)

#### TFT Touch reset

If you somehow mess up the touch calibration placing and empty reset.txt file on the card and resetting will trigger a re-calibration.

## Compile your own (source)

If you want to make any changes you will need to compile form the source files using Platform.io.
Here is a basic walk through, [Platformio Docs](../learn/platformio.md).

The V1 Engineering version of the SKR Pro firmware can be found on
[github](https://github.com/V1EngineeringInc/MarlinBuilder/releases), there are two versions, series and MPCNC dual endstop.

The V1 Engineering generic version of the TFT firmware is in this [github
repo](https://github.com/V1EngineeringInc/BIGTREETECH-TouchScreenFirmware)

## Cases

### Flyfisher604 SKR Pro v1.2 and TFT E3 v3.0 Case

A three-part case (lower box, top lid, and sloped TFT screen) that includes:

- Ventilation on two sides of the lower box
- Two fan mounts with integrated grates on the back of the sloped TFT screen
- Built in standoffs for the SKR Pro board and TFT screen
- Opening on TFT sloped screen mount exposing to expose the SD card slot
- Openings for DB25 and DB15 connectors (with mounting hole) to interface internal wiring to MPCNC (or use these as pass throughs)

Available [here](https://www.thingiverse.com/thing:4678675) on Thingiverse.

![!Flyflisher604 SKR Pro Case](img/Flyfisher604_SKR_Pro_v1.2_and_TFT_E3_v3.0_Case.jpg){: width="400"}

![!Flyflisher604 SKR Pro Case Inside](img/Flyfisher604_SKR_Pro_v1.2_and_TFT_E3_v3.0_Case_Inside.jpg){: width="400"}

