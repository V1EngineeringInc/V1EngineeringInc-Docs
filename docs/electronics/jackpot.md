# Jackpot CNC Controller

## Basics

The Jackpot CNC Controller is a 32bit dual-core 240mhz board, WiFi, Bluetooth, or hardwired capable (esp32). It has 6x TMC2209 driver ports, 7 inputs, 2x 5V outputs, 2x input level outputs, one expansion module socket.
MicroSD card slot. The board runs FluidNC which is fully GRBL compatible with extended features and easier configuration.

**Want to buy one?**

[Jackpot CNC Controller is available here in the shop.](https://www.v1e.com/products/jackpot-cnc-controller)

![!Jackpot CNC controller](../img/jackpot/jp7.jpg){: width="800"}

## Thanks

First and foremost, thank you, Bart Dring for the amazing design and custom firmware required to make this happen. This is based off the [6 Pack Universal CNC Controller Development Board](https://www.tindie.com/products/33366583/6-pack-universal-cnc-controller/) and changes were made to accommodate all the use cases I have seen with the V1 CNC Machines except for 3D printing. Also, many thanks for GRBL-ESP32 and now [FluidNC](https://github.com/bdring/FluidNC).

Mitch Bradley deserves a lot of thanks for handling the day to day of FluidNC and providing a ton of chat based support on Discord.

## Specifications

+ ESP32-wroom-32 Based control board
    * 32bit dual-core 2450mhz board.
    * WiFi, Bluetooth (rarely used), or USB Direct connection
    * Onboard or external antenna
    * Socket based for easy swapping if anything were to ever go wrong
    * 38 pin - [ESP32-DevKitC CP2102 - MicroUSB](https://amzn.to/4766q7B), These seem to be the most reliable.
    * 25.4mm header width
    
+ 9-24VDC
    * Current required is a minimum of 19W (24Vx0.8A).
    * If you plan on using the high current outputs adjust accordingly.

+ 6x Stepper driver sockets
    * This controller is designed for use with TMC2209 drivers in UART control mode only
    * Typically, TMC2209 drivers are limited to 4 addresses. This controller uses a CS (chip select) pin for 3 of the drivers to allow 6 drivers to be individually controlled.
    * The sockets are labeled XYZABC, but you can use any socket for any axis or motor number. The letters are just for reference only.
    * **No Stallguard**

+ 7x Inputs
    * All switch inputs are active low, the LED goes on when ground is connected to the pin.
    * They have a 10k pullup external to the ESP32. The signal pin (S) should be connected to the ground pin (G) to activate the switch. 
    * The 5V is optional and is used for external switches that require 5V. 
    * Define the pins in the config file like this...
    * Define an N.O. switch like this. gpio.xx.low
    * Define an N.C. switch like this. gpio.xx

+ 2x Line level outputs
    * PWM Capable
    * The MOSFETs switch to ground. You can use any voltage up to the VMot max as the positive, as long as it uses the same ground reference.
    * Can be used to drive 2.5A continuously before they overheat. You can use them intermittently up to 3.5A. If using above 2.5A you should test to see if they start to overheat.
    * They can be used with inductive loads (solenoids, relays, DC fans)

+ 2x 5V outputs
    * PWM Capable
    * These will source and sink about 25mA each.
    * See the "Spindle" section of the FluidNC wiki for common uses.

+ 1x Expansion Module socket
    * [6 PACK expansion module source](https://oshwlab.com/bdring?tab=project&page=1)
    * [Buy Them](https://www.tindie.com/stores/33366583/)
    * This should be able to use any CNC I/O module. Use an 11mm standoff or a 3D printed support in the mounting hole provided.
    * These Modules can be just about anything you need, more inputs, outputs, relays, spindle, VFD, Servo, OLED...

+ 1x MicroSD card slot
    * larger than 2gb needed
    * Fat32
    * 30 character or less file names, 100 character or less file location

+ Firmware
    * [FluidNC](https://github.com/bdring/FluidNC)
    * Text based config file for simple firmware edits.
    * No compiling to flash a board or change the configuration.
    * ~100% GRBL compatible
    * Custom ESP3D-UI which includes a tablet mode with Gcode viewer.
    

+ Dimensions
    * 80mmx100mm Board footprint
    * [CAD/Step link](https://a360.co/3KchBBL)
    * [Dimensions](../img/jackpot/Jackpot_2023-07-08 Drawing.pdf)
![!Jackpot dims](../img/jackpot/drawingsample.png){: loading=lazy width="400"}
    * ISO
![!Jackpot iso](../img/jackpot/StepISO.png){: loading=lazy width="400"}

## Initial Setup

### Initial "flashing"

There is no need for compiling or any of the previous steps need to "flash" a marlin based board.

There are three basic steps, Firmware, GUI, Config. It is probably best to follow these steps.

[FluidNC WIKI Install](http://wiki.fluidnc.com/en/installation#using-pre-compiled-files)

Some tips, run erase.bat (unless you are purposely updating only one part), install-wifi.bat, then install-fs.bat.

From here you can load the Config files in one of two ways. 

**Preferred** - FluidTerm from that same folder and hit ctrl+u to select the config.yaml for your machine (linked below), hit enter to accept the name. After that is done uploading, you can hit ctrl+r to reset. The Fluid term is a crazy good tool If you ever have any issues, this is how we will check it. When you are all wired and powered up, I suggest using it to reset the board and check to see everything is working (except the one driver we do not typically use). A web based version of this whole process is coming very soon.

You can also load the preferences.json, and macrocfg.json files using CTRL+U. After you log in you can more quickly load the "macro**.g" files

**OTA** - Or you can sign into your board over wifi (SSID- FluidNC PASS - 12345678) and upload the config.yaml and other files directly with the FluincNC settings/files Tab.

#### Wiring

Pictures coming when the final boards show up.

The steppers and endstops plug in in this order
MPCNC = X, Y, Z, X2, Y2

LR = X, Y, Z, Y2, Z2

The touchplate plugs into the last port (gpoi.36), on both boards.

#### Test endstops led/terminal

The onboard LED's test the wiring connections. Our Normally Closed (NC) endstop wiring will have a lit LED when not triggered and not lit when triggered. The Probe is the opposite, lit when triggered.

You can test the firmware by running "$Limits", this will show a real time trigger display. "!" to exit that mode.

## Configurations

[Github link](https://github.com/V1EngineeringInc/FluidNC_Configs) 
You can sign up for notifications of any updates if you would like.

## Updating

If you ever want or need to update the actual firmware or GUI you can do it with the FluidTerm or OTA. [FluidNC Wiki - Update](http://wiki.fluidnc.com/en/installation#upgrading-firmware) This is as easy as uploading a file and reseting with USB or WiFi. Very easy, no compiling. You can also do it from the WebUI in the file section.

## Common Gcode Scripts

$H - Equivalent to Marlin's "Home All" or G28. $HX, $HY, $HZ for individual axes.

$MD - Disables the steppers, power them down.

$CD=config.yaml - saves any config changes you make to the file. To allow it to be there after a reboot.

$S - This shows all the values, the config file does not contain them all only changes from default.

## Laser tips

For the fastest raster etching, the most reasource intensive thing we can do. Either use AP mode with a microSD card, or turn off the wifi and use only the USB (with [Lightburn](https://lightburnsoftware.com/)).

$Wifi/Mode=off - if you are using the USB connection to Lightburn to use some of the built-in tools use this command to turn off the radio. It will come back after a power cycle. 

If you have a laser defined in the config you are always in "laser" mode. So you can either leave it defined and use M5 (turn off laser mode) in your starting gcode for non-laser CNC use, or just comment out the laser in the config (like I ship it).

Raster speed depends on dot size, for a 0.19mm resolution I am getting 70-120mm/s depending on the type of raster.

## Detailed FluidNC info

The [FluidNC Wiki](http://wiki.fluidnc.com/) has all the details of this firmware, with an excellent search bar. If you still get stuck you can of course turn to the [V1E.com forum](https://forum.v1e.com/) or there are links to a FluidNC specific discord in the wiki.

!!! Note
    save for later 

## Cases

## Estlcam

This section is for setting up estlcam for GRBL/FluiNC

![!Jackpot estlcam basics](../img/jackpot/esbasicsettings.jpg){: width="400"}
Change the basic settings to GRBL.

[Config file](../img/jackpot/FluidNC.pp), to install this file open EstlCAM, setup, CNC Programs, open settings at the bottom. This will import all the settings, starting, toolchange, and endding gcode sections. Everything in one file.


Some screen shots needed here.


## Changelog

V1 - 8/10/23 - Just a graphics change from RC2.

RC2- 
:   Power and output headers, smaller holes for cleaner assembly
:   Logo change on the back
:   Stepper header label change

RC1- 
:   Initial release

## License
Link
