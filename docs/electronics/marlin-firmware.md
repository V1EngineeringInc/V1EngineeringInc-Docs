!!! warning
    **If you bought a bundle or electronics board from V1Enginering.com, this is already done.**

# Firmware
Firmware is the program or software “embedded/burned” into the electronics board, this is what
translates the gcode into motion in the stepper motors.

## Marlin

![!pic](https://www.v1engineering.com/wp-content/uploads/2015/05/Marlin-Logo-GitHub.png)

The boards sold here are using the [Marlin](https://github.com/MarlinFirmware/Marlin) Firmware, only
minor changes needed to run any machine. Again, if you bought your electronics from here this has
already been done for you no need to continue on.

The firmware is what makes this all possible and was the key for me to quickly make all sorts of
robots. For a while now [Scott – “ThinkyHead”](https://www.patreon.com/thinkyhead/posts) has been the ring leader for all the great developers
working on the Marlin project. He is not the only one but has been a huge factor in getting the
firmware to the place it is now. If you can drop a dollar or more his way to keep this project
advancing click the link above.

??? "Dual Endstops & Auto squaring"
    This is an advanced feature and the information will be kept separately for the time being,
    [Here](../electronics/dual-endstops).

### GitHub Firmware

If you like to be more up to date with the Newest Marlin features, I have all my most recent updates here.

[Github pre-configured.](https://github.com/Allted/Marlin/tree/CHOOSE_VERSION)

**Right now flashing Marlin 2.0 requires the [Arduino IDE 1.8.9 or
higher](https://www.arduino.cc/en/Main/Software). Other than that follow the
directions [below](#how-to-flash).**

### Using GitHub

You will find this on the [V1 Engineering Marlin GitHub](https://github.com/Allted/Marlin) page. 

| In case you have never used GitHub, the first drop down lets you select the firmware version you want. | The next step is download the firmware you selected. Click on “Clone or Download”, then click on “Download Zip”. |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![!pic](https://www.v1engineering.com/wp-content/uploads/2017/11/select-github.jpg){: width="400"}     | ![!pic](https://www.v1engineering.com/wp-content/uploads/2017/11/download-github.jpg){: width="400"}             |

### Naming key

All versions have the full graphic LCD enabled. I can add links to all of these if it is still unclear.

**Machine type_Board_Details**

_Machine type_– MP3DP, V1CNC=MPCNC & LowRider, ZenXY

_Boards_– Mini-Roambo, Full Rambo, Archim1, Archim2, Ramps

_Details_– 16T=16tooth pulley, T8=Leadscrew type, 16/32step=Step rate the firmware is set to, Dual Endstop=MPCNC specific edits, Aero/MK=base extruders they are set to.

### Marlin Change log

1/20/20 - 418, Arcs fixed, more default current fresh start from 2.0.1+

4/27/19 – 401-402, 600+changes (Marlin catch up), enabled eeprom, lowered Z accel (MPCNC/LowRider), driver fixes.

12/17/18 – 303 Archim1 boards only, LCD/USB fix. Thanks Jason&Ultimachine.

11/28/18 – 302

- Added 3 menus, G92 XYZ, Home Z, Home XY. (Maybe I should use “Zero” instead of home or reference :p)
- No easy workaround for the flashing ???’s…The “[right way](https://github.com/MarlinFirmware/Marlin/issues/7342)”
- Dual firmware’s get disable softstop menus.
- 20 minute stepper hold after activation / gcode completion.
- Remember G0, G1, G2…. (might help with poor post processors) Can’t enable the G0 default rapids because we need a separate for the Z axis. If I enable this by default we would be working with the Z max unless otherwise specified in the gcode. Might be a good thing.
- Junction deviation set at smoothie recommended 0.005 for CNC’s (gunna need some testing).
- Enabled S_Curve_deviation.
- LCD timeout set to 45 seconds instead of 15.
- CNC coordinate systems enabled.
- Added a little versioning number to the LCD boot screen or repetier connect info. This will help easily identify what firmware people are using and if there are ever issues we can flag it.

| [![pic](https://www.v1engineering.com/wp-content/uploads/2017/04/IMG_20170411_181548-1080x702.jpg){: width="400"}](../electronics/ultimachine.md) | [![pic](https://www.v1engineering.com/wp-content/uploads/2015/04/IMG_20150418_093541-1080x810.jpg){: width="400"}](../electronics/ramps.md) |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|  [Ultimachine Boards](../electronics/ultimachine.md)                                                                                              | [Ramps](../electronics/ramps.md)                                                                                                            |

## Smoothie

The X and Y steppers are wired in series (or parallel) and wired to a single port. The picture below
is an example of a board running smoothieware. Many other boards are available.

![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/IMG_20170405_184727.jpg){: width="400"}

Here is my Pre-Configured Basic config file.

This is just me getting my feet wet and there are a lot of other options you can add to the file.

**This is for 32nd stepping, 16 Tooth Pulleys and  5/16″ threaded rod.**

Config for smoothie boards..[config](https://www.v1engineering.com/wp-content/uploads/2016/09/config.zip)

[More info here](https://www.v1engineering.com/forum/topic/sbase-smoothieware/)

### Change log

9/15/16- Initial release

## GRBL

The X and Y steppers are wired in series (or parallel) and wired to a single port. The picture below
is an example of a board running GRBL. Many other boards are available. First board I ever
bought…..one of these days…

![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/IMG_20170405_185038.jpg){: width="400"}

Sorry I do not have a config for this yet.

## How to Flash

### How to flash firmware on the Mini-Rambo (or Rambo)

- Install the [Arduino](https://www.arduino.cc/en/Main/Software) software and its drivers **before** you plug in your board.
- You will then need to plug in both **USB and 12V power.**
- Unzip the firmware you need from above
- Open arduino
- Sketch-Include Library-Manage Libraries
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/u81.png){: width="400"}
- Type “U8glib” in the search box, hit enter, select U8glib, select the number with the highest
    version, Install. This has never been easier.
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/u82.png){: width="400"}
- File- Preferences
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram1.png){: width="200"}
- In “additional boards manager url” paste
    `https://raw.githubusercontent.com/ultimachine/ArduinoAddons/master/package_ultimachine_index.json`
    Hit “ok”
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram2.png){: width="200"}
- Tools-Board-Boards Manager
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram3.png){: width="200"}
- Search and install, “rambo”
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram4.png){: width="200"}
- Tools-Board-Rambo
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram5.png){: width="200"}
- Tools- Port (whatever port your board shows up in)
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/port.png){: width="400"}
- Open the firmware folder and select the current Marlin.ino file
![!pic](https://www.v1engineering.com/wp-content/uploads/2018/11/Marlin19.jpg){: width="400"}
- Click on the Upload arrow and watch the progress bar at the bottom
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/upload.png){: width="400"}
- The bottom of the window will say “done uploading” when it is finished done
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/done-e1487436522248.png){: width="400"}
- **If you get a boot loader error, it is okay.**

### How to flash firmware on the Ramps 1.4

- Install the [Arduino](https://www.arduino.cc/en/Main/Software) software and its drivers **before** you plug in your board.
- Unzip the firmware you need from above
- Open Arduino
- Sketch-Include Library-Manage Libraries
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/u81.png){: width="400"}
- Type “U8glib” in the search box, hit enter, select U8glib, select the number with the highest
    version, Install. This has never been easier.
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/u82.png){: width="400"}
- Tools-Board-Mega 2560
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/board.png){: width="400"}
- Tools-Processor
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/proc.png){: width="400"}
- Tools- Port (whatever port your board shows up in)
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/port.png){: width="400"}
- Open the firmware folder and select the current Marlin.ino file
![!pic](https://www.v1engineering.com/wp-content/uploads/2018/11/Marlin19.jpg){: width="400"}
- Click on the Upload arrow and watch the progress bar at the bottom
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/upload.png){: width="400"}
- The bottom of the window will say “done uploading” when it is finished done
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/done-e1487436522248.png){: width="400"}

### How to flash firmware on the Archim

- Install the [Arduino](https://www.arduino.cc/en/Main/Software) software and its drivers **before** you plug in your board.
- You will then need to plug in both **USB and 12V power.**
- Unzip the firmware you need from above
-**Make sure you do not have U8glib in your Arduino Library folder**
- File- Preferences
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram1.png){: width="200"}
- In “additional boards manager url” paste
    `https://raw.githubusercontent.com/ultimachine/ArduinoAddons/master/package_ultimachine_index.json`
    Hit “ok”
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram2.png){: width="200"}
- Tools-Board-Boards Manager
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram3.png){: width="200"}
- Search and install, “archim”
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram4.png){: width="200"}
- Tools-Board-archim
![!pic](https://www.v1engineering.com/wp-content/uploads/2016/12/ram5.png){: width="200"}
- Tools- Port (whatever port your board shows up in)
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/port.png){: width="400"}
- Open the firmware folder and select the current Marlin.ino file
![!pic](https://www.v1engineering.com/wp-content/uploads/2018/11/Marlin19.jpg){: width="400"}
- Click on the Upload arrow and watch the progress bar at the bottom
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/upload.png){: width="400"}
- The bottom of the window will say “done uploading” when it is finished done
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/12/done-e1487436522248.png){: width="400"}



