# Import Extruder

## Assembly

Assembly of my all metal version of the Mk8 import extruder

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20170917_123047.jpg){: loading=lazy width="400"}

I ship these partially assembled. These are not assembled by me so a few extra minutes starting from
scratch can save a lot of headaches in the end.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1239562.jpg){: loading=lazy width="400"}

Start by screwing the base plate to the stepper with the M3x6 screw. I prefer to have the wires oriented up.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1241262.jpg){: loading=lazy width="400"}

On the Tension arm add the bearing and broad headed screw. If the bearing does not spin freely, flip
it over. One side is slightly offset. Make sure the bearing spins free and smoothly.

Some sets include a washer, use it if you have it. Thread locker is a good idea as well.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1242252.jpg){: loading=lazy width="400"}

Add the tension arm and bolt. Make sure the arm swivels smoothly. If the arm binds you can loosen
the screw a bit. Thread locker is a good idea here as well.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1243102.jpg){: loading=lazy width="400"}

Add the pulley next. Usually the set/grub screws are positioned closer to the motor but not always.
Center the teeth on the idler pulley and make certain the pulley does not hit the heat sink that
gets installed later.

Tighten the set screw on the stepper’s flat spot if it has one, the second screw.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1244192.jpg){: loading=lazy width="400"}

Double check the feed pulley to be sure the teeth are inline with the idler and the pulley does not
hit the heat sink.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1245002.jpg){: loading=lazy width="400"}

Add the MicroSwiss throat and lock nut. This throat does not contain PTFE so it can handle higher
temperatures and should not need any maintenance. To help with heat dissipation the lock nut is
positioned on the inside of the bracket.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1246002.jpg){: loading=lazy width="400"}

Thread the throat is as far as it can go. Do not let the throat make contact with the idler or
pulley. The smaller this gap the better soft and flexible filaments will print and the better the
heat will dissipate from the throat when printing PLA slowly.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1247242.jpg){: loading=lazy width="400"}

Next up is the tension stack. The bottom screw helps to retain the spring (and is not always
necessary). This should be the shorter of the two screws. If this screw is too long the arm will not
open enough to insert filament. If that is the case don’t use the screw or find a shorter one.

The top screw controls the filament pinch tension, tighter is not better, you want just enough to
feed without slipping.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1248282.jpg){: loading=lazy width="400"}

Tension stack completed. Start with little to no tension and only increase it if your filament
slips.

Double check the throat is not hitting the idler or pulley.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1249192.jpg){: loading=lazy width="400"}

The cooling stack. the screws may or may not have washers. Position the fan wires appropriately.
Tighten with moderate tension. This is where a majority of the unwanted heat gets dissipated so
tension is good for heat transfer but too much will ruin the fan, so balance…

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1250572.jpg){: loading=lazy width="400"}

The cooling stack completed. 

!!! warning 
    **If your heat sink has open fins on the bottom it is best to tape off
    the bottom vents so the fan does not blow air on your prints only up and out.**

When installing the heat block position the set screw facing down so you can change the heater
without a complete tear down if necessary.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20181229_1251582.jpg){: loading=lazy width="400"}

Add the heater cartridge and guide the thermistor into the small hole. Ensure it is fully inserted.
Gently snug the heater cartridge set screw, careful not to damage the heater. Make sure not to move
the fragile wires excessively and ensure they are not twisted and sorting out.

The nozzle is what locks the block in place. Make sure the nozzle is not locking onto the block but
is instead making tight contact with the throat.

!!! warning
    After the assembly is complete heat up the extrude to a few degrees above your intended use temp
    and snug up the nozzle before running any filament through.

---

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/IMG_20170917_124847.jpg){: loading=lazy width="400"}

Secure the wires to the top fan hole, and your done with assembly.

---

## Plug it in

[More detail here.](../electronics/ramps.md)

You will need power to both sides of the green plug, you can just add a short jumper wire from one
side to the other. The polarity is marked on the board, double check to make sure this is correct.
The fan on the heat sink needs to always run, this gets plugged directly into the green power plug,
polarity matters. Extruder to port D8, polarity does not matter. Optional print fan plugs in to port
D9 polarity matters.

## Marlin edits

Very few edits required. Any firmware I release after this post will most likely already be set for
this extruder by default. I will put the info here for you adventurous types.

[Pre-set Firmware](../electronics/marlin-firmware.md)

All of these that I have gotten have used the marlin #11 thermistor, and at 32nd stepping I use 200
steps for the e value.

```C
#define TEMP_SENSOR_0 11
```
and

```C
#define DEFAULT_AXIS_STEPS_PER_UNIT   {200,200,4535.44,200}
```

Even after running the PID auto tune I get a huge overshoot in temp so limiting the max current
might help with this, I will update it when I get a chance to test it.

```C
// Comment the following line to disable PID and enable bang-bang.
#define PIDTEMP
#define BANG_MAX 255 // limits current to nozzle while in bang-bang mode; 255=full current
#define PID_MAX BANG_MAX // limits current to nozzle while PID is active (see PID_FUNCTIONAL_RANGE below); 255=full current
#ifdef PIDTEMP
```

## Slicer edits

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/cgcode.png){: loading=lazy width="400"}

Delete the beginning gcode, you don’t want it to home.

Change the end gcode to look like this

```
G91
G1 E-5 ;retract
G1 Z5 ;lift up 5mm
G90
M104 S0 ; turn off temperature
M84 ; disable motors
```

## Not using endstops

![!picture](https://www.v1engineering.com/wp-content/uploads/2015/08/position.png){: loading=lazy width="400"}

Position you parts on the lower corner (0,0,0), before you slice them. This will start your prints
where ever your head is. So position the nozzle touching the bed and exactly where you want it to
start. When the print begins it should lift up the correct amount and print. You can manually adjust
the height during the skirt print to fine tune it.

That’s it print away. The printed parts I am shipping are starting to get printed on this cnc, and they look amazing.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nVKHlX3NaTA"
  title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
  clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Recommended beginning slic3r settings.

![!slicer1](https://www.v1engineering.com/wp-content/uploads/2015/10/sl1.png){: loading=lazy width="400"}
![!slicer2](https://www.v1engineering.com/wp-content/uploads/2015/10/sl2.png){: loading=lazy width="400"}
![!slicer3](https://www.v1engineering.com/wp-content/uploads/2015/10/sl3.png){: loading=lazy width="400"}
![!slicer4](https://www.v1engineering.com/wp-content/uploads/2015/10/sl4.png){: loading=lazy width="400"}
![!slicer5](https://www.v1engineering.com/wp-content/uploads/2015/10/sl5.png){: loading=lazy width="400"}
![!slicer6](https://www.v1engineering.com/wp-content/uploads/2015/10/sl6.png){: loading=lazy width="400"}
![!slicer7](https://www.v1engineering.com/wp-content/uploads/2015/10/sl7.png){: loading=lazy width="400"}
![!slicer8](https://www.v1engineering.com/wp-content/uploads/2015/10/sl8.png){: loading=lazy width="400"}
![!slicer9](https://www.v1engineering.com/wp-content/uploads/2015/10/sl9.png){: loading=lazy width="400"}
![!slicera](https://www.v1engineering.com/wp-content/uploads/2015/10/sla.png){: loading=lazy width="400"}
![!slicerb](https://www.v1engineering.com/wp-content/uploads/2015/10/slb.png){: loading=lazy width="400"}

Test file just in case.

[Test IE Part](https://www.v1engineering.com/wp-content/uploads/2015/08/test-IE-part.zip)
