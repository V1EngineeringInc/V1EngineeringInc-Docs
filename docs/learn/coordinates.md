# Coordinates 101

## Introduction

Here is a quote from [the forums](https://forum.v1engineering.com/t/g00-z2-00-why/15097/8):

> Zeroing out your coordinates is like setting the start line in a race. When you turn on the machine,
where ever it starts is the start line. If you use the LCD or computer to move it, you are moving
away from the start point, but the start point is in the same place it was. When you start the race,
you have to return to the start line. Zeroing out your coordinates moves the start line to where you
currently are.

Exactly. Setting the zero, or the "origin" is important so your machine knows where to
start the job. 

Equally important is that the directions you move are going the right way. X, Y, and Z may seem
arbitrary to you, but they are not (but they are a bit flexible). We'll talk about the three axis,
and their directions in [Coordinate Directions](#coordinate-directions).

Coordinates are used with every job, and it is important to set them right.

## Origin

The "Origin" or "Home" or "Zero" is the single place where the X,Y and Z coordinates are equal to
0.000.

This can be anywhere. It is set in your CAM, and then when you set up your job, you will tell the
controller where you want it so the rest of the cut is in the right place.

Here is an example:

1. You design a simple shape, a 10mm square. In CAM, you choose to cut 10mm deep.
1. You set the origin in CAM to be at the top of the workpiece, and the lower left corner of the
design.
1. On your machine, you bolt down your work, install the bit, all that stuff.
1. You then jog to the lower left corner of your work. You adjust the Z so the bit is *just*
touching the top surface of the material.
1. You now **Set the origin to this location**.
1. Start the router, play the g-code file, and the box is cut down 10mm from where you started, and
10mm to the up and right.

!!! error "Warning"
    If you hadn't set the origin. The machine would have just assumed wherever it started was the
    origin. That can lead to the first thing it does is just crash through your workpiece, crash
    through your spoil board, and try to get back to where it started. Not a fun day!

### Origin Locations

Just to make this easier, there are just a few origin locations that make sense.

#### Lower, Left, Top

If you're cutting a flat part out of an oversized piece of material, this is the best way to go. You
just put the origin near the lower left area of the material, and it will cut from that corner. It
won't be easy to center it in the material, but that is OK.

#### Center, Top

If you are carving a logo, or some art, into  the top of an existing workpiece, you might consider
centering the XY location of the origin. For example, if you are carving a logo in a cabinet door.
In this case, center the origin in CAM, and make sure the design is scaled to a size you like. Mark
the center of your door, and set the origin there.

The benefit of this option is that the ultimate carving will stay centered. It is easy to
accidentally go over the edge of material if it is scaled wrong, which is why the LLT origin is
better for new parts.

#### Bottom Z

Setting the origin to the top of the material means you will start at 0, and then move down into the
negative coordinates to reach through the material you are cutting. If that doesn't make sense to
you, you can also set the Z=0 to be the top of your spoil board, and start milling starting at the
top of the workpiece. This isn't very common though, because the spoil board isn't as important
(usually) as your work material, so getting it aligned with the top of the material is more useful.

### Setting the Origin

There are different ways to set the origin. Each way has its own pros/cons.

#### Using LCD

If you have an LCD with your controller, you can use the menus to move the tool to the origin that
you want. Once there, select the "Set Home Position" in the menus.

#### Using Repetier Host

Similar to the LCD method, use Repetier Host's controls to jog to the desired origin location, and
then send a `G92 X0 Y0 Z0` to set the origin. You also need to send a `@isathome` to reset
Repetier's idea of where it is.

#### Using Starting G-Code

If you have your CAM software add in a `G92 X0 Y0 Z0` at the start of the gcode file, then wherever
you start your code will be the origin, because the first thing it will do is set the origin. This
is what is done in the test crown, and it works pretty well, as long as you know it is there.

!!! warning
    Be sure to pay attention to which files have this and which don't. It can be pretty easy to
    assume a file has this command, and forget to set the origin, and then watch it take off
    towards it's starting location. Alternatively, if you set the origin, and forget the gcode has a
    G92, then job somewhere else to start the job, it may be cutting air, and confusing you.

#### Move the Gantry by Hand

On an MPCNC, when the power is off, you can usually move the gantry by just pushing it to where you
want it to go. Once you're at the origin you want, you can just turn on the controller and enable
the steppers.

!!! warning
    Moving the steppers too fast will generate current, which goes back into the controller. If you
    are moving them fast enough for the lights to turn on in the controller, you are in danger of
    turning your controller to smoke.

!!! warning
    This doesn't work with some MPCNCs with large routers or the Low Rider. If the gantry falls on
    its own, then you can't easily set the Z.

!!! info
    You can also use the LCD or Repetier Host to move the gantry under power. When you're there, you
    can just reset the controller to reset the origin.

#### Using XY Endstops (Single or Dual)

##### Option 1
Set the origin in you CAM to be the location of the endstops. Then put your material in the right
place relative to your machine. The Z needs to be set separately.

##### Option 2
Home the X and Y. You can then move to the desired origin by jogging the machine. When you get
there, write down the current coordinates, and Set the home position. If you turn off the machine or
lose your location, you can home again, and then jog to the coordinates you wrote down.

#### Using Z Touch Plate

Using one of the above methods, set your origin, and then jog the Z up. Attach your touch plate and
home the Z. This can be done in these ways:

- Home Z in the LCD menu.
- Home Z button in Repetier-Host.
- `G28 Z` from the console.

!!! info
    You can do this at any X or Y location you'd like. If you're carving, you might want to probe
    near the middle of the workpiece so that you minimize the total error. But make sure you go back
    to X,Y zero before resetting the Z.

Now, you need to remove the offset from the Touch plate. There are a couple of ways to do that too:

!!! warning
    Don't forget to remove the touch plate before continuing.

- Jog the machine down the thickness of the touch plate and set the origin.
- Send a `G92 Z0.5` to set the current position to 0.5mm. If your touch plate is a different
    thickness, use that thickness.

## Coordinate Directions

When you're setting up the machine, you have some power over the coordinate directions. You can plug
the motors into the X, Y, or Z drivers, and you can accidentally or intentionally reverse the plugs
(which makes the motors go the other way).

### Basic Configuration

If you just want to have a machine that works, and you don't care, then test to make sure the
machine moves in this way (relative to you, when standing at the front of the machine):

 - Higher X values go to the right.
 - Higher Y values go away from you.
 - Higher Z values go up (away from the spoil board).

!!! info
    The *best* way to check the coordinates is to just carefully jog in a single direction at a
    time.

If one of the axis moves the wrong direction, you can [reverse the
steppers](../software/reverse-motor.md).

If two of the axis are swapped, you can move the wires to change the driver.

!!! warning
    You can destroy your drivers if the steppers are enabled and you disconnect them. Always turn
    the power off before disconnecting the motors.


So, if you'd rather have the wheeled axis be the X and the tubing axis be the Y on your Low Rider,
that's fine. It is your machine, make it work for you.

### Advanced Configurations

If you want a different coordinate frame, then you can have it. But if you don't want mirrored
parts, then you need to follow these rules:

- The coordinate frame needs to be a "Right Handed" coordinate frame. That is true even if you are
    left handed or one handed. It has nothing to do with your hands. [Here is a
    reference](https://en.wikipedia.org/wiki/Cartesian_coordinate_system#Orientation_and_handedness).
- Z should be the up/down coordinate. Some features, like arcs, assume you are in the XY plane for
    most operations.
    
### Multiple Workspaces
A workspace defines where the operating origin is, and the origin is the point where X, Y and Z = 0.

When you turn your machine on you will be working in a default workspace.

All commands you enter related to coordinates (G92, G0, G1, etc) will set or move you around in the workspace.

Usually you will set the workspace origin to something relative to the stock material you are working on just before running your gcode by jogging your router to your desired origin and running a G92 command (e.g. G92 X0, Y0).

![LR3 Top Down Image Startup](https://user-images.githubusercontent.com/10994647/220621514-693acaa7-da51-4b04-a23a-836540647df6.png)


Multiple workspaces exist (https://marlinfw.org/docs/gcode/G054-G059.html).

For Marlin they are: G54, G55, G56, G57, G58, G59, G59.1, G59.2 and G59.3

To use a different workspace, simply send the workspace code for the workspace you want to operate in (e.g. sending G55 will put the machine in the G55 workspace) then all G92, G0, G1 etc commands will relate to the new workspace coordinates.

Use: This allows you to have multiple jobs set up on your machine at once and not have to reset your origin to switch between jobs. Simply switch workspaces.

![LR3 Top Down Image G54 and G55](https://user-images.githubusercontent.com/10994647/219782606-cc59a7e8-dc3c-4df7-b7c1-42cb0c3d58d8.png)

Note: If you have set an origin with G92 prior to sending a command to change workspaces then all workspaces will start with the origin you set, except for the G53 Native Workspace described below, which will have it's origin reset to the point where the machine started, or where the endstops were used to set the machine boundaries. 

Saving to EEPROM with M500 (https://marlinfw.org/docs/gcode/M500.html) will save the workspace origins so they can be used the next time you turn the machine on.

### Native Workspace and Machine Coordinates
For multiple workspaces to actually work your machine needs to keep track of where it is in something called the Native Workspace.

Coordinates in the Native Workspace are called Machine Coordinates because the origin in the Native Workspace is the location that your machine is sitting at when the steppers are first engaged or after homing operations using endstops have been executed to reset the origin to a physical limit of your machine’s working area.


The origin in the Native Workspace is usually set to a corner of your entire operating space.


This means that the machine always knows where it is relative to a start point, regardless of where it is doing actual work.


G92 will not change the origin in machine coordinates. Only homing operations will change the origin to ensure the machine does not forget its position in real space.

![LR3 Top Down Image G54 and G55 and Native](https://user-images.githubusercontent.com/10994647/219782855-56d04410-186d-499e-a3fb-fed750e434c9.png)

Moving in machine coordinates is done using the G53 modifier (https://marlinfw.org/docs/gcode/G053.html).
E.g. G53 G0 X200 Y300 Z15 moves to X,Y,Z = 200,300,15 in Machine Coordinate space


Use:
This allows you to use real physical distances repeatedly on your machine allowing for “parking” locations or tool change sites that never change their real world positioning.

Note: Setting a location in a workspace coordinate system is actually telling the machine to remember the machine coordinates of that location as a workspace offset. E.g. Homing the machine and then jogging to X=250, Y=320, Z=15 and using G92 X0 Y0 Z0 to set X,Y,Z = 0 in workspace G54 is actually telling the machine to remember the G54 origin as Machine Coordinates X=250, Y=320, Z=15.

