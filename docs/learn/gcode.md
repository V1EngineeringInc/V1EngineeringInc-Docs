# G-code 101

## Introduction

G-code may look complicated, but with just a little bit of knowledge, you can inspect the output of
your CAM and be able to spot problems before they get to the machine. You can also write some
custom commands with a little effort and set up your machine faster than the couple of buttons your
controller gives you.

![Gcode Text Message](../img/gcode-sms.png){: loading=lazy width="250"}

### G-Code Files

What is a `.gcode` file?

A `.gcode` file is just a list of individual commands, which will be processed one at a time. That's
it! There is no magic involved. You can rename a .gcode file with a .txt extension and open it in a
text editor (like wordpad). Here are some instructions you might see in a .gcode file:

```gcode
G00 X0.000 Y0.000 Z0.000 F300.00
G01 Z-1.000 F300.00
G01 X10.000 F600.00
```

Each of these lines is one single command. They are read in by the controller one at a time.

If you typed in each of these commands into a console, the machine would work the same as if you
played them from a G-Code sender (except, you couldn't go as fast).

So, if we understand what each of these commands do, then we can understand the whole file.

??? "But, this just looks like gibberish to me!?"
    This "language" is meant to be read by the controller and not by humans. But you don't have to
    be a coder to understand it. In fact, there are really just a few commands that we ever use, so
    it doesn't take long at all to learn.

### First G-Code Command

```
G01 X10.000 F600.00
```

This is a single G-Code command. It starts with the kind of command `G01` and then has two
parameters `X10.000` and `F600.00`.

**`G01`**
:   This is a G1 command, which means it is a movement command. All `G01` does is tell the
controller that the parameters are for a movement command.

**`X10.000`**
:   When there is a movement command, the X tells the controller to move in the X direction. The
number (`10.000`) tells the controller how far to move. In this case, it will move the X axis to the
10mm mark.

**`F600.00`**
:   When there is a movement command, the F tells the controller how fast to move. In this command,
this is 600mm/min, or 10mm/s.

So, put it all together and this tells the controller to move to the X=10mm mark, at 10mm/s.

In a movement command, X, Y, and Z are all possible. So here is some g-code for moving in a square
10mm on a side, at 10mm/s:
```
G01 X0.000  Y0.000  F600
G01 X10.000 Y0.000  F600
G01 X10.000 Y10.000 F600
G01 X0.000  Y10.000 F600
G01 X0.000  Y0.000  F600
```

??? "But wait, there are 4 sides on a square, and this is 5 commands!"
    A movement command only describes where to go **to**. The previous location determines where to
    move **from**. To make a line, you need two movement commands.

### G-Code Variants

G-Code is supposed to be a standard. But, it has a lot of uses, and a lot of ways it can be
expanded. We use Marlin as controller software, so our g-code needs to be compatible with Marlin.
Other CNC machines might use Grbl (which is mostly the same as Marlin) or Mach or LinuxCNC. Each of
these has slight variations in the standard. For that reason it is important to look at the Marlin
documentation for Gcode:

[Marlin G-Code Reference](https://marlinfw.org/meta/gcode/)

Another great g-code reference is the [Rep Rap Reference](https://www.reprap.org/wiki/G-code). Just
beware that Marlin doesn't maintain the Rep Rap reference, so even the Marlin specific information
may be out of date.

### Comments

Since G-Code isn't a human language, it is helpful to add in some comments to let people who are
reading the code understand what you are saying. Machines will ignore the comments, so you can put
anything you want in there.

There are two formats for comments:

1. Anything after a semicolon will be a comment. Ex:

```
G01 X10.000 F600.00 ; This is a comment
; This is also a comment.
```

2. Anything in parenthesis is a comment. Ex:

```
G01 X10.000 F600.00 ( This is a comment )
( This is also a comment. )
```

### G1 vs. G01

`G1` is the same as `G01`. Marlin will ignore the extra 0. This is true for most commands.

### M-codes

Some "G-Codes" start with an `M`. This is just a way to expand the number of commands.

### Capitalization

All the letters should be capitalized. Marlin isn't looking for lowercase letters, and they look
completely different to Marlin, so just use ALL CAPS.

## Specific G-Codes

Here are some G-Codes that we will find very important.

### G0, G1 - Linear Move

[Marlin Reference](https://marlinfw.org/docs/gcode/G000-G001.html)

- If you don't define a speed, the previous speed will be used.

### G2, G3 - Arc Moves

[Marlin Reference](https://marlinfw.org/docs/gcode/G002-G003.html)

- These have had trouble with some versions of the firmware. Sometimes, it is better to configure
    your CAM to not use them, and instead, use linear moves to move around an arc.

### G28 - Home

[Marlin Reference](https://marlinfw.org/docs/gcode/G028.html)

- It is generally only used with a specific axis on the CNC machine. For example:

    ```G28 Z ; Homes the Z axis only```

### G90 - Absolute Positioning.

[Marlin Reference](https://marlinfw.org/docs/gcode/G090.html)

- Most of the time, your movement commands will be in absolute coordinates. So make sure this is at the top
of your gcode files.

### G92 - Set Position

[Marlin Reference](https://marlinfw.org/docs/gcode/G092.html)

### M17 - Enable Steppers

[Marlin Reference](https://marlinfw.org/docs/gcode/M017.html)

### M18, M84 - Disable Steppers

[Marlin Reference](https://marlinfw.org/docs/gcode/M018.html)

## Configuration Codes

Sometimes, it is useful to type on a console directly with the controller to investigate or to set
specific commands. These codes are mostly useful in those cases:

### M115 - Firmware Information

[Marlin Reference](https://marlinfw.org/docs/gcode/M115.html)

### M503 - Report Settings

[Marlin Reference](https://marlinfw.org/docs/gcode/M503.html)

### M500 - Save Settings

[Marlin Reference](https://marlinfw.org/docs/gcode/M500.html)

### M502 - Restore Factory Settings

[Marlin Reference](https://marlinfw.org/docs/gcode/M502.html)

### M122 - TMC Debug Information

[Marlin Reference](https://marlinfw.org/docs/gcode/M122.html)

- Only useful for TMC drivers, and only if you have TMC_DEBUG enabled.
