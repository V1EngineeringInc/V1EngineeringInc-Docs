
# Dual Endstops on a Low Rider

!!! info
    This is a WIP. Please ask questions in the [forums](https://forums.v1engineering.com) if this
    doesn't make sense. There are some very helpful people who would like you to succeed, and this
    document won't do that for everyone.

    Also, feel free to edit this document with improvements. There is a little pencil in the upper
    right, and we review each change before publishing it.

There are 5 motors on a Low Rider. One on each Z axis, one on the router plate, and two on the other
axis.

This article is about the wiring needed to set up the Low Rider so that each motor has its own
driver, and each driver has its own endstop, while also allowing the Z probe for fine carving
operations.

## Do I need this?

First off. You should realize that there are hundreds of Low Riders wired with the series wiring.
In many ways, series wiring is simpler. Endstops aren't needed at all, really.

Here are some things you may not know about series wiring and endstops:
 
 - Series wiring provides the same amount of power to each motor.
 - Endstops aren't needed in CNC. The origin is determined by the workpiece (unlike in 3D printing).
 - In series or dual endstop configurations, the mirrored motors move exactly in lock step after
     homing.
 - Homing isn't needed in CNC. You can just define where the origin is.
 - If you start the machine square and keep the motors engaged, the machine will stay square.
     Getting a 5 foot gantry square isn't that difficult. The large size makes it easier than on an
     MPCNC.

Here are the advantages of a Dual Endstop configuration:

1. Auto squaring. If you home a dual endstop machine, each motor will move until it reaches its own
endstop. Because of this, you can start the machine out of square, home, and be confident the
machine will stay square.
1. If you have your work set up in a known location, you can split the work into multiple files, and
continue the next day after homing.
1. You can home to move the gantry up all the way, giving you room to work.

## What do I need to do this?

1. A control board with at least 5 drivers. The Full sized Rambo has 5. The Skr Pro has 6. These two
boards have configurations preconfigured in the MarlinBuilder.
1. If you're using a board with removable drivers, you need to have 5 drivers. For example, on the
Skr Pro, you could use series wiring with 3 drivers, but this needs 5.
1. A wire for each motor.
1. And endstop for each motor. These should be the dumb switches with 3 pins (C, NC, NO). Not the
ones with the little circuit board attached. Those only cause trouble.
1. The Y axis needs to be the belt and wheel axis. The X axis needs to be the belt and tube axis. If
you have this reversed, then you will need to edit the preconfigured firmware.
1. A computer you can control it with, or at least the TFT screen is really helpful. This is an
advanced setup, and it requires some specific testing that can't be done over the LCD Rep Rap Full
Discount Display.

## Wiring

!!! note
    These instructions are for the preconfigured firmware from MarlinBuilder. They assume you have
    2xY and 1xX motors.

!!! note "Rambo and SKR users"
    Read these instructions, but also read specific instructions for the
    [Rambo](../ultimachine#rambo-13-14) and [Skr Pro](skrpro.md)
    boards.

Here is where we are trying to get to:

| Motor | Driver | Endstop  |
|-------|--------|----------|
| X     | X      | Xmin     |
| Y1    | Y      | Ymin     |
| Y2    | E0     | Ymax     |
| Z1    | Z      | Zmax     |
| Z2    | **E1** | **Xmax** |

!!! warning
    Pay special attention to the Z2. This is a bit different.
    Pay special attention to the Z1 endstop, this is in the Zmax port.

#### Motor Drivers

The motors should be wired directly to the board. Most steppers come wired AABB, meaning the first
two wires are one coil, and the next two wires are the second coil. Since there are 5 drivers, each
motor goes straight to a single driver.

There are two motor ports on the Z driver. Don't use the second and leave it blank.

( A picture here sure would be nice ).

The Second Y motor goes to the E0 port and the second Z motor goes to the E1 port.

#### Endstops

Match up each endstop with the appropriate motor. 

!!! warning
    All endstops should be wired between the Ground (-) and the Signal (s). Don't use the Positive
    (+). All the endstops should also be wired to the Common (C) and Normally Closed (NC) connectors
    on the switches.

The X endstop goes in the Xmin port and needs to be mounted on the negative X axis.

The Y1 endstop goes in the Ymin port, needs to be on the negative Y side, and needs to be on the
side with the motor that is plugged into the Y port.

The Y2 endstop goes in the Ymax port, needs to be on the negative Y side, and needs to be on the
side with the motor that is plugged into the **E0** port.

!!! note
    The Z homes up. Why? so we can still use a Z min probe to probe the workpiece.
    Be very careful though, if you home up and miss the endstops, you will take apart your low
    rider. Not cool.

The Z1 endstop goes in the Zmax port, needs to be on the positive Z side, and needs to be on the
side with the motor that is plugged into the Z port.

The Z2 endstop goes in the **Xmax** (that is X, not Z) port, needs to be on the positive Z side, and
needs to be on the side with the motor that is plugged into the **E1** port.

!!! info
    Be sure you [test](#testing) the endstops with M119 and confirm the direction of all motors before trying to
    home anything.

#### Z probe

The Z probe will help you measure the top of the workpiece you are about to make a mess with. This
isn't needed in most cases, because you can just jog the machine to the top and set the Z=0 with
`G92 Z0`. But it can be really helpful for tool changes, and it can take out some of the guess work
of carving.

The wiring of the Z probe is the same as with an MPCNC or a serial wiring Low Rider.

The touch plate connects to the Ground (-) pin on Zmin.

The Signal pin (s) of the Zmin connects to the bit. You can use an alligator clip, or a magnet to connect the
bit electrically.

When the bit touches the plate, it looks like a closed switch, and it should trigger Marlin to stop
the Z axis. 

**Test the functionality of the plate before probing. Use M119 and make sure it reports zmin_probe
is `open` when the bit isn't touching the plate, and `TRIGGERED` when the bit is touching the
plate.**

The normal "Home Z" will lift the gantry, and not probe down. To probe down, you need to use a
different command. That is `G38.2 Z0`. This command will search downward for the touch plate with
the bit. 

!!! warning 
    If you miss, it may stretch out the couplers, causing damage.

Example gcode script for probe:

```
M0 Attach probe ; Remind the user to attach the probe
G38.2 Z0 ; Home down for the touchplate
G92 Z0.5 ; Sets the offset for the touchplate, if the touchplate is 0.5mm thick
G1 Z10 F300 ; lifts the Z out of the way
M0 Remove probe ; Remind the user to remove the probe
```

### Wiring for Rambo

(A picture or two would be really nice)

Pay attention to the endstop pin definitions. They flip direction for the max ports.

### Skr Pro

(A picture or two would be really nice)

The endstops are connected through the board to the sensorless homing pins on the TMC2209s.
Currently, you need to bend, cut, or desolder the sensorless homing endstop pin.

The second Z port comes with two little jumpers. Those need to remain installed.

## Testing

Don't go crazy and expect everything to be set up correctly right away. There are a lot of places
where a wire can get loose, or something could be wrong with the configuration (we do our best, but
mistakes happen). Build up confidence in the different parts one step at a time, and you will end up
with smaller areas to search for problems.

!!! note
    For simplicity, I am going to assume you are doing this checkout with a computer attached to the
    USB port, and have it connected using Repetier Host.

If you get in trouble, don't get frustrated, these instructions aren't perfect. Go ask for help in
the [forums](https://forums.v1engineering.com).

### Motors

1. Check the motors are moving the right way, and the mirrored motors are moving together.
  - For the preconfigured Dual LR files, the Y axis is the axis on wheels and the X axis is the axis
      on tubes/bearings.
  - Higher Z values should raise the gantry up.
  - Higher X values should move to the right.
  - Higher Y values should move away from you.
  - You may have to change which side of the table you stand on to make that true. When using CAM,
      understand that this is the side of the table you have to imagine standing on.

1. Check the distance the motors move. If you command a 10mm movement, it should move 10mm. If it
moves 20mm, or 5mm, there is a problem. If it is 10.1mm, worry about it later, that passed this
test.

1. Run the test crown pattern. Post the result to the forums, and some pics of your machine. You
should really consider taking a break and making a mess. This machine is in great shape now, and it
can easily handle making a coaster to help you with the next steps.

### Endstops

Before doing any homing, you want to make sure the motors are working. You already drew the crown,
right?

Here's how you check your endstops:

1. Send M119 (Send GCode, and then look at the console for the response).
2. The correct endstop should show "open" when the switch isn't pressed and "TRIGGERED" when it is
pressed. Pay attention to match the correct motor to the correct endstop. Check the table above for
the correct order.
3. The Z probe should show "open" when the bit isn't touching the plate, and "TRIGGERED" when the
bit is touching the plate. Be sure to test on the actual router, in the same situation you'll use
for setting up a job (as best you can). Sometimes just having the router plugged into AC can affect
the probe.
4. Double check that reducing the X and Y cause the machine to go towards the endstops.
5. Double check that increasing the Z causes the machine to go towards the endstops.

### Homing/Probing

OK. One you're ready to try your first home.

To Home X, you can press the Home X button or send `G28 X` in the Send Gcode.

You can do the same with Y and Z. 

To test the probe, get the plate, the bit, and everything ready and send G38.2 Z0. The bit should go
down, and feel free to touch it early. If something goes wrong, you're going to want to pull the
power immediately. You can stretch the Z couplers if it plows into the table.
