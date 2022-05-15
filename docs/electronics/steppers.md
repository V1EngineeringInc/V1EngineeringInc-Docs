# Wiring the steppers

![!pic](https://www.v1engineering.com/wp-content/uploads/2015/10/IMG_20151022_112457.jpg){: loading=lazy width="400"}

Using [this wiring kit](https://vicious1-com.myshopify.com/collections/parts/products/wiring-kit-1),
you really just need to plug in the motors, tape or otherwise secure the connection and go.

There are now two wiring choices. I highly recommend  you start with the series wiring kit. The dual
kit adds complexity with that complexity you gain accuracy and precision. More dual endstop
information [here](../electronics/dual-endstops.md)

![!pic](https://www.v1engineering.com/wp-content/uploads/2017/11/IMG_20180529_175849.jpg){: loading=lazy width="400"}
![!pic](https://www.v1engineering.com/wp-content/uploads/2018/05/IMG_20180529_1806062.jpg){: loading=lazy width="400"}

**Make sure to always secure the connections with tape.**

If one of the steppers is going the wrong way, flip it’s plug over to reverse it. If they are both
going the wrong way, [flip them](../software/reverse-motor.md) at the board (is series wired of course).

## The DIY way

The stepper for the z axis just needs its wires extended. Usually you would just cut the plug and
splice in some 4/24 shielded cable and be done with it.

### Series (do it this way)-

Same amp draw as a single stepper (heat), twice the power, slightly less top speed. We do not need
to worry about top speed, delta’s maybe cnc’s, no. There are plenty of online resources to see how
this is done, here is a quick sketch just in case you can’t find a clear one.

RigidWiki
![!pic](https://www.v1engineering.com/wp-content/uploads/2018/07/image-4.jpg){: loading=lazy width="400"}
![!pic](https://www.v1engineering.com/wp-content/uploads/2019/02/wiring.jpg){: loading=lazy width="400"}

Hand drawn diagram

![!pic](https://www.v1engineering.com/wp-content/uploads/2016/08/IMG_20160831_114146-e1492533409509.jpg){: loading=lazy width="400"}

Modified parallel harness

![!pic](https://www.v1engineering.com/wp-content/uploads/2016/08/IMG_20160829_150944.jpg){: loading=lazy width="400"}
 
### Parallel (don’t do it this way) –

Twice the amp draw as series (heat) less power, slightly higher top speed.

The steppers for the X and Y axis are wired in parallel, with the far motor getting one coil wired in reverse.

![!pic](https://www.v1engineering.com/wp-content/uploads/2015/10/IMG_20151022_112559.jpg){: loading=lazy width="400"}

In this picture the yellow and blue are a pair/coil, and the green and red are a pair/coil. So to reverse this stepper you would wire this blue to the other yellow, and this yellow to the other blue. Do not get caught up in my colors, the position on the plug tells you what 2 wires are pairs.

![!pic](https://www.v1engineering.com/wp-content/uploads/2015/09/STEPPER_display_large.jpg){: loading=lazy width="400"}
![!pic](https://www.v1engineering.com/wp-content/uploads/2015/09/wiring.png){: loading=lazy width="400"}

To wire in parallel you connect all the like colors and plug it into the ramps board, then on the far stepper change on pair/coil.


