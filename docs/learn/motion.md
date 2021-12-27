# Motion 101

## Introduction

Try to explain a CNC machine to a 5 year old, and you'll probably say something like, "It moves a
tool around to cut out shapes". Motion is the critical task we ask of our machines. Mostly, we don't
worry too much about it, because it just works, but a little bit of understanding can go a long way
if you've got any issues with your motion.

So let's talk about motion!

## Motion Background

- A `G00` command is meant to indicate a travel move, or a move where there is no cutting involved.
- A `G01` command is meant to indicate a cutting move.

!!! info
    Marlin's main goal is 3D printing, and that makes it a little murky. In 3D printing, any move that
    doesn't extrude plastic is a travel move. By default, it doesn't see a distinction between `G00`
    and `G01`.

- Marlin has its own rules for maximum speed, and acceleration.
- Marlin also supports "jerk" setting, but this isn't the derivative of the acceleration. You can
    also set the "Junction Deviation" which replaces jerk.
- Each command has a "Feedrate". If you don't define one, it will just use the previous one.

## G-Code Feedrate

### Example G-Code

Look at these commands (for more detail, look at the [g-code tutorial](gcode.md)):

```
G00 X0.00 Y0.00 Z0.00
G00 X10.00
G01 Z-0.1 F300.00
G01 X100.00 F600
G01 Y100.00
```

At first, it looks fine. But there is a problem. The first two commands don't have a feedrate
defined. So whatever speed the last command was at, is what is going to be used.

At the 3rd line, we finally set a feedrate. On the 4th, it is changed to something new, and on the
last line, there is no feedrate, so the 600 is used again.

### Details

The feed rates in gcode describe the speed to travel along the line. So, for example, if you were at
0,0 and you were travelling to 100mm,100mm, and the feedrate was set to 100mm/s, it would travel at
a speed of 100mm/s, but have 140mm to travel, so it would take about 1.4s to get there. If you sent
the same command with a feedrate of 140mm/s, then it would take 1 second to finish that move.

The limits on the speeds in Marlin are axis based. So if you set the max speed rate in X to 50mm/s
and the max feedrate in Y to 50mm/s, Marlin will slow down this move to not exceed that speed on
either axis. So the speed would end up being 70mm/s, and finish in about 2 seconds.

So I use these terms in this document:

Feedrate
:   The maximum speed along the straight line in gcode.

Max Speed
:   The maximum speed along a single axis.

!!! note
    In the past, some versions of Marlin have not protected against speeds higher than their max.
    All indications are the current Marlin (V1Engineering 418+) are responding well to adjustments
    in the max feedrate.

Those total timing numbers aren't completely right. Because Marlin also doesn't go from a full stop
to top speed instantly. It will use the acceleration values to decide how quickly to ramp up the
speed to its top speed. So this move that takes 2s and maxes out at 50mm/s in each direction will
actually take a bit longer, because it will start out slower, and work its way up to 50mm/s. Then at
the end, it will slow down before the end of the 100mm, and stop smoothly. You can really see the
effect if you drop your accelerations very slow. Movements are smoother, but they sometimes take
a lot longer. The accelerations are also applied on a per axis basis, so on a high speed move, the X
axis will be accelerating at its max acceleration and the Y will be accelerating at its max
acceleration. The total acceleration on a compound move will be higher along the line.

Jerk, or Junction Deviation are used because even on the corner of a square, you don't want to stop
completely. That will just slow things down more than necessary. These other parameters consider how
fast to take a turn.

## Adjusting Max Speed

You can easily change the max speeds and accelerations because they are stored in the
EEPROM, and they are read in every time you start (or boot) Marlin. You can change these at any
time, but remember to save your changes by writing out to the EEPROM.

`M203 X30 Y30 Z10`
:   This will set the X and Y speeds to 30mm/s (notice this is in mm/s, whereas feed rates are in
mm/min) and the Z to 10mm/s.

`M500`
:   This will save all the value to the EEPROM.

[Marlin Reference](https://marlinfw.org/docs/gcode/M203.html)

Generally, the defaults in the V1Engineering firmware are conservative enough for these machines.
If you want to go faster and know the consequences, then by all means, change them. If you installed
a high steps/mm Z and you need to slow down your Z, then this is a good way to do it.

Here is the general rule of thumb for speeds. You shouldn't allow the machine to go so fast that it
skips steps when not cutting material. Friction in the machine, or loss of torque at high speeds can
contribute to lost steps at higher speeds, so you'll want to test at high speeds, and then reduce
the parameter to stay away from trouble.

## Adjusting Max Accelerations

You can change the accelerations similarly to the speeds, just use
[`M204`](https://marlinfw.org/docs/gcode/M204.html) instead.

Again, the V1Engineering accelerations should be a good start for almost everyone. If you have a lot
of steps/mm, the acceleration doesn't need to be changed. The acceleration is more based on the
amount of mass you are moving and rigidity of the machine.

You will want to test your accelerations by sending a large move command at max speed. For example,
an X move of 100mm at 1000mm/s. The Acceleration and speeds will be maxed out, and if you skip any
steps, then you need to go way lower. Some people prefer a much smaller acceleration, because it
makes the machine seem more gentle or smart.

## Configuring Separate Travel Speeds

By default, Marlin treats `G00` commands as though they were just `G01` commands. But many of the
CNC friendly G-Code Senders and CAM use `G00` to just move the machine as fast as possible.

**Because of this default treatment in Marlin, the last feedrate requested in a `G01` command will be
used in a `G00` command.**

If you don't want that behavior, and you want `G00` to just move as fast as possible, you can use this
option in the Configuration_adv.h:

```C
// Enable and set a (default) feedrate for all G0 moves
//#define G0_FEEDRATE 3000 // (mm/m)
#ifdef G0_FEEDRATE
    //#define VARIABLE_G0_FEEDRATE // The G0 feedrate is set by F in G0 motion mode
#endif
```

If you define `G0_FEEDRATE`, then that will always get used for `G0` commands (and still be subject to
the max speeds and accelerations).

If you define that and `VARIABLE_G0_FEEDRATE`, then any feedrate defined on a `G0` command will stick
and any future `G0` commands will use that speed (unless they define their own).

One useful configuration might be to set your max speeds and accelerations to something that will
never skip (in air) and then set the `G0_FEEDRATE` to something high. All travel moves will be as fast
as possible after that.
