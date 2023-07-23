# Jackpot CNC Controller

## Basics

The Jackpot CNC Controller is a 32bit dual-core 2450mhz board, WiFi, Bluetooth, or hardwired capable (esp32). It has 6xTMC2209 drivers, 7 inputs, 2x 5V outputs, 2x input level outputs, one expansion module socket.
MicroSD card slot. The board runs FluidNC which is fully GRBL compatible with extended features and easier configuration.

**Want to buy one?**

[Jackpot CNC Controller is available here in the shop.](https://www.v1e.com/products/jackpot-cnc-controller)

![!Jackpot CNC controller](../img/jackpot/jp7.jpg){: width="800"}

## Thanks

First and foremost, thank you, Bart Dring for the amazing design and custom firmware required to make this happen. This is based off the [6 Pack Universal CNC Controller Development Board](https://www.tindie.com/products/33366583/6-pack-universal-cnc-controller/) and changes were made to accommodate all the use cases I have seen with the V1 CNC Machines except for 3D printing. Also, many thanks for GRBL-ESP32 and now [FluidNC](https://github.com/bdring/FluidNC).

Mitch Bradley deserves a lot of thanks for handling the day to day of FluidNC and providing a ton of chat based support on Discord.

## Specifications

**ESP32-wroom-32 Based control board**
:   32bit dual-core 2450mhz board.
:   WiFi, Bluetooth, or USB Direct connection
:   Onboard or external antenna
:   Socket based for easy swapping if anything were to ever go wrong
:   38 pin
:   25.4mm header width
    
**9-24VDC**

**Current - Variable depending on use but...**

**6- Stepper driver sockets**
:   This controller is designed for use with TMC2209 drivers in UART control mode only
:   Typically, TMC2209 drivers are limited to 4 addresses. This controller uses a CS (chip select) pin for 3 of the drivers to allow 6 drivers to be individually controlled.
:   The sockets are labeled XYZABC, but you can use any socket for any axis or motor number. The letters are just for reference only.
:   **No Stallguard**

**7- Inputs**
:   All switch inputs are active low, the LED goes on when ground is connected to the pin.
:   They have a 10k pullup external to the ESP32. The signal pin (S) should be connected to the ground pin (G) to activate the switch. 
:   The 5V is optional and is used for external switches that require 5V. 
:   Define the pins in the config file like this...
:   Define an N.O. switch like this. gpio.xx.low
:   Define an N.C. switch like this. gpio.xx

**2- Line level out**
:   PWM Capable
:   The MOSFETs switch to ground. You can use any voltage up to the VMot max as the positive, as long as it uses the same ground reference.
:   They can be used to drive 2.5A continuously before they overheat. You can use them intermittently up to 3.5A. If using above 2.5A you should test to see if they start to overheat.
:   They can be used with inductive loads (solenoids, relays, DC fans)

**2- 5V out**
:   PWM Capable
:   These will source and sink about 25mA each.
:   See the "Spindle" section of the FluidNC wiki for common uses.

**1- Expansion Module socket**
:   [6 PACK expansion module source](https://oshwlab.com/bdring?tab=project&page=1)
:   [Buy Them](https://www.tindie.com/stores/33366583/)
:   This should be able to use any CNC I/O module. Use an 11mm standoff or a 3D printed support in the mounting hole provided.
:   These Modules can be just about anything you need, more inputs, outputs, relays, spindle, VFD, Servo, OLED...

**1- MicroSD card slot**
:   larger than 2gb needed
:   Fat32
:   30 character or less file names, 100 character or less file location

**Firmware-**
:   [FluidNC](https://github.com/bdring/FluidNC)
:   Text based config file for simple firmware edits.
:   No compiling to flash a board or change the configuration.
:   ~100% GRBL compatible
:   Custom ESD3D-UI which includes a tablet mode with Gcode viewer.
    

**80mmx100mm Dimensions**
:   [CAD/Step link](https://a360.co/3KchBBL)
:   [Dimensions](../img/jackpot/Jackpot_2023-07-08 Drawing.pdf)
![!Jackpot dims](../img/jackpot/drawingsample.png){: loading=lazy width="400"}
:   ISO
![!Jackpot iso](../img/jackpot/StepISO.png){: loading=lazy width="400"}

## Initial Setup

Intial "flashing"

Wiring

Test endstops led/terminal

## Configurations

## Updating

## Common Gcode Scripts

## Laser tips

## Detailed FluidNC info

The [FluidNC Wiki](http://wiki.fluidnc.com/) has all the details of this firmware, with an excellent search bar. If you still get stuck you can of course turn to the [V1E.com forum](https://forum.v1e.com/) or there are links to a FluidNC specific discord in the wiki.

!!! Note
    save for later 

## Cases


## Changelog
RC1- 
:   Initial release

RC2- 
:   Power and output headers, smaller holes for cleaner assembly
:   Logo change on the back
:   Stepper header label change

## License
Link
