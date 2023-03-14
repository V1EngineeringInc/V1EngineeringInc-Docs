# Auto Square, Dual EndStops

## Basics

The Dual EndStop firmware update enables unprecedented precision more easily than ever before.

![Squaremelons](../img/old/2017/11/Squaremelon.jpg){ loading=lazy width="300" align=right }
The Mostly Printed CNC and LowRider CNC are unique compared to other machines in the fact that two of the axes are independently powered at
each end. Using this fact and the new dual endstop firmware we can now more precisely
and accurately set the position of every single stepper on the machine independently. This should
give you repeatability on the order of your endstops resolution, even after powering off.

Before this new firmware update all the machines in this category relied 100% on the users build
accuracy, or manual measuring. **Now** just a minor offset adjustment from the control panel will correct this.

Here is a look at the very first test of auto squaring. It is even more accurate now, it will square the axis, then do it again slower to account for any initial endstop offsets due to the skew.
<iframe width="560" height="315" src="https://www.youtube.com/embed/F-tw3WuV8jk"
  title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
  clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
___

## Firmware

The dual endstop firmware is on the V1 Engineering [Marlin Builder page](https://docs.v1engineering.com/electronics/marlin-firmware/)
page.
___

## Use

Any of the V1 CNC machines can auto square if you are using independently wired steppers (5 driver control board). 

Users new to the CNC world should not use this at first; this is an intermediate technique. So If you have not used 
your machine before stop here and get it dirty, this is for more precise parts.

You can now use the machine in two ways. Quick one off jobs, setting the tool position by hand, starting with 
`G92 X0 Y0 Z0`, and just running the job, or by starting each job with a `G28` (home and auto square). Using Auto Squaring 
Opens up the options listed below.

- You can use fixtures at a set reference points on the table to do repeat jobs or multiple sided
cuts utilizing CAM based work offsets or scripts.

- Tool changes can be done with multiple gcodes so you can do repeat jobs in order of bit used
instead of per piece depending on if changing the part of the bit is the faster choice.

- Jobs can be restarted in case of power outage, tool breaks, long multi day jobs, apply paint
between cuts, etc.

For more info please see the [Milling Basics](../tools/milling-basics.md) page.
___

## Endstop Testing 

After all the endstops have been connected issuing a `M119` command, in any terminal window, will 
let you see the current status of each endstop. You should check that each endstop registers both an 
open and closed status before proceeding. Open when not touching and closed when they are. You can test them individually
by closing each one by hand and running an `M119`. Also verify the X1 corresponds to the X1 stepper, ETC.

Then verify a positive movement is away from the end stops.

Remember small 1mm moves when initially powering it up, if driving your steppers the wrong way you
can rip your machine apart. If your steppers are moving the wrong direction, **completely power off
your board before flipping the plug over.**

Have a look at the "Control" section of these instructions for board specific diagrams for the endstops.

## Calibration

The unfortunately designated `M666` lets you offset the physical homing location to quickly calibrate your machine.
This means you can tell the machine that after it triggers the homing switch to back up by a specified amount instead of 
trying to physically adjust the machine by a fraction of a millimeter.

Start by locating your endstop stops or endstop blocks as accurate as you can. The smaller the M666 value the better. 
If you do the tests and find your error is more than two millimeters I suggest moving your endstop blocks or even bending
 your endstop metal tabs a bit to lower the error.

1. You can verify how square your axis is by measuring the diagonals of the largest rectangle you can
   mark in your build area. This also works for leveling your LowRider Z axis in relation to your table. The larger
   The rectangle you mark or further apart you measure the Z axis the easier and more accurate this will be.
2. The difference of these measurements is the error in your build exaggerated to make it easier to adjust. So a 2mm error
   does not mean an adjustment of 2mm.
3. The command to offset an error is `M666 X0.72`, This would move the axis 0.72mm away from the stop block. Depending on
   your build this could be an X, Y, or Z value. This value can also be a negative. In this example if a positive value moves
   the X1 stepper back by 0.72mm, a Negative value (-0.72), would move the X2 stepper instead.
4. Test the value you just set. If the error gets worse change the sign of the offset (positive or negative). If the 
   error got better but not enough, increase the value. If the error is now opposite, you overshot. This will take a few tries.
5. When adjusted to your liking you save the settings in your eeprom by running `M500`. These settings will stay after power 
   cycling but will be erased if you update your firmware. It is always best to take note of these settings. You
   can confirm your settings by running `M666` in the terminal to see what is currently saved.
6. If you move your endstops, tension your belts, or change your spoil board these settings can change. Testing them can be quick and easy though.


Care should be taken to use as little pen pressure as possible with the finest tip possible to get
the most accurate results and a pen mount with some give should be used, [example pen
mount](https://www.thingiverse.com/thing:1612207). Or you can use and end mill as shown here.

<iframe width="560" height="315" src="https://www.youtube.com/embed/w5H1AZ40YHk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Auto Squaring runs automatically any time your home your machine or home any axis of your machine. After calibration it is set it and forget it.

For more details see the build instructions for your machine, we have included machine specific instructions near the end of each build.