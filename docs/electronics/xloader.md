# XLoader

!!! note
    If you're looking to flash Marlin Firmware for a V1Engineering machine, start [here](../electronics/marlin-firmware.md).

XLoader is a utility that doesn't compile any code (like [PlatformIO](../learn/platformio.md) does),
but can "flash" or install that code onto a Rambo, Mini-Rambo, or Ramps.

It uses the `firmware.hex` file found in the [Marlin Firmware Precompiled Zip Files](../electronics/marlin-firmware.md).

This does not work with the BigTreeTech Skr boards, or the Archim boards.

## Get XLoader

XLoader is only available in windows and you can download it [Pre-configured here](https://www.hobbytronics.co.uk/arduino-xloader), or [source here](https://github.com/xinabox/xLoader/releases/latest). Look for the latest release and find a XLoader_[version].zip

Once downloaded, you only have to unzip it, and run the `XLoader.exe` on a windows machine.

## Use XLoader

![!XLoader](../img/XLoader.jpeg)

It's pretty simple, really. 

1. Get the `firmware.hex` file from the [Marlin Firmware Precompiled Zip Files](../electronics/marlin-firmware.md).
2. Connect the Rambo, Mini-Rambo, or Ramps arduino to the computer via USB.
3. Connect the 12V Power to the Rambo or Mini-Rambo to power the board.
4. Open `XLoader.exe`, choose Mega(ATMEGA2560) for the Device.
5. Choose the COM port for the board. Baud rate at 115200 (*That's different than the 250,000 that we use with Repetier Host).
6. Hit Upload

It will show progress and tell you when it's done. If you have any problems, ask in the forums.



