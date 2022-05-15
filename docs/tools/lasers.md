# Lasers

## Safety

### Eyes

![caution](https://www.v1engineering.com/wp-content/uploads/2019/01/caution-laser-400x278.jpg){: loading=lazy width="200"}

First and foremost, these really are dangerous, not like ripping the tag off your mattress. These
can and will blind and or burn you in less than
[1/100th](https://en.wikipedia.org/wiki/Laser_safety) of a second, It takes ten times that long to
even [react](https://en.wikipedia.org/wiki/Corneal_reflex) by blinking **if** it is in the visible
spectrum. Did I make my point yet?

Safety glasses are paramount. This is not the place to try and save money. You need a high quality
pair and anyone else that could be around it needs the same quality. The cheaper your laser is the
more money you will need to spend on the safety glasses. Import lasers are notorious for being
dirty, mislabeled, and this makes them more dangerous. High quality lasers are of a known wavelength
and strength therefore they are easy to protect yourself from, imports can contain other wavelengths
that your goggles may or may not protect you from or be more powerful than your glasses are rated
for. I am no expert, have no way of testing, and therefore no real say in who makes quality glasses,
I cannot make a recommendation at this time. This [video](https://youtu.be/WnDjIDhxnMs) might help
drive home the point.

While we are on the subject, the laser looks extremely harmless in the goggles, kids (and most
adults) will try to take off the glasses immediately so no youngsters (or tough guys) unless the
laser is fully enclosed behind a laser shield and you trust them to listen. In the glasses the laser
is just a bright dot but you can see in your periphery the entire room lights up. You never know
when the laser could hit something slightly reflective, your mount could fail, the gcode could cram
it into the surface and break your mount, your air assist could drop into and reflect the beam
sending send a death beam in any direction.

### Lungs & Skin

![toxic](https://www.v1engineering.com/wp-content/uploads/2019/01/toxic-gas-hazard-sign241-400x400.jpg){: loading=lazy width="200"}

The other end of the safety spectrum is the material you are working with. You can’t just go etching
and cutting things willy nilly. Ever think you could make [chlorine
gas](https://en.wikipedia.org/wiki/Chlorine_gas_poisoning) or
[cyanide](https://www.cdc.gov/niosh/ershdb/emergencyresponsecard_29750038.html) in your own
house….now you can. Laser cutting vinyl or ABS plastic does just that. Two extremely common
materials. [Here is the list](http://atxhackerspace.org/wiki/Laser_Cutter_Materials) I refer to most
often, if you have a link to a better guide please let me know. Best practice is to contain all the
laser smoke and direct it through a filter and vent it outside, at the very least vent it outside.
You do not want to breath any of the smoke any modern man made material makes.

### Fire

![fire](https://www.v1engineering.com/wp-content/uploads/2019/01/fire-55x55.jpg){: loading=lazy width="100"}

Now this one might be a little bit of a surprise to some and obvious to others. Lasers are burning
your material, add air assist directly to the burn zone and strong ventilation fans and you end up
with the best recipe for fire ever. Pay close attention never leave it unattended and have the
appropriate type of fire suppression on hand. Fire is not extremely common on good cuts but if it
does happen it happens stupid fast with all that force fed oxygen.

---

## Basics

### Types

![diode](https://www.v1engineering.com/wp-content/uploads/2019/01/diode.jpg){: loading=lazy width="200"}

Two of the most common lasers in the maker world are CO2 and Diode lasers. Diode lasers are much
more compact, have self-contained interchangeable optics, and are an order of magnitude lower power
than a typical CO2 laser. More on the Power in a bit.  These lasers operate at different wavelengths
and this can have an effect of the type of material they are suitable for. Diode based lasers can
range in price from a few dollars up to a few hundred, and CO2 based lasers start at a few hundred
and go up from there. Both lasers have some sort of focal lens, but a CO2 laser also has a mirror
system to steer the beam before focus. Diodes can be cooled with a small fan, CO2 use water and
sometimes a chiller.

![tube](https://www.v1engineering.com/wp-content/uploads/2019/01/glass_Co2_laser_tube.png){: loading=lazy width="280"}

Typically on any of the V1 Engineering machines you would be using a diode based laser. If your goal
is to cut wood or plastic you should be looking at a CO2 laser. A Diode is best at marking/etching,
and is only capable of cutting light materials (foam, paper, plastic) and very thin wood.

### Power

Laser power, not as straight forward as you would think. Higher numbers in general mean thicker
materials can be cut, or etching can be done faster. Numbers are not everything! A laser has four
things to consider when talking about its power; wattage, spot size, focal length, spectrum.

Wattage
:   The overall power output of your laser (like a light bulb, energy per time). On most
non-laser specific machines we are limited by speed. Okay stick with me, just like strapping on a
chainsaw motor to the MPCNC stronger is not always better. Since we can only move so fast before we
start to get motion degradation you need to size your laser accordingly. A strong laser moving
slowly will have an extremely limited range of  grey levels. For example at the same speed a higher
powered laser will have to use power 1-20 so you don’t start a fire (19 levels of grey), but a lower
powered laser will be able to use power 1-255 (254 levels of grey) without starting a fire. Make
sense?

Spot size
:   How small of a spot the wattage is concentrated on. Spot size dictates the resolution of
the image you can produce, think printer DPI (dots per inch). Another side effect of spot size can
be ability to cut. A poorly focused laser’s power is too spread out to be effective, a finely
focused laser cuts significantly better. For a diode this can vary 100-400 micron in diameter just
by laser wattage. To be more clear, more powerful diode lasers cannot be focused to as small of a
point as lower powered lasers (the source is not truly a point, larger diodes equal larger initial
“points”, and it is not actually a spot but a rectangular spot).

Focal length
![!focal_length](https://www.v1engineering.com/wp-content/uploads/2019/01/Focal-Length-1.gif){: loading=lazy width="400"}
:   This influences the shape of the laser cone (long and narrow or short and fat). The
focal length is dependent on the lens you use and should be a small range depending on the lens. If
you have a choice; a longer focal length can aid in cutting ability (a thinner steeper beam/cone can
cut deeper before power is lost to the edges of the material).

Spectrum
:   The wavelength of the light it produces (diodes-UV to viable, CO2- mid-infrared).
Materials react differently to every spectrum as do safety glasses. If you have a specific need do
your research before buying.

Duty cycle
:   One more thing on the topic of power, duty cycle or continuous time on. On the cheap
import look out for sensational things like “15W $50!” somewhere in the description it could say
“One second continuous operation time”. This means they are over driving the heck out of the laser,
it will not last long, and at 1 second bursts it is not very useful. Guard your wallet from these
Scammy Chumps. I just found another ad that says no more than 30min continuous, that might sound
like a lot at first but you can do some really detailed things that take a few hours.

### Air Assist

To get cleaner etching, deeper cuts, and to save your lens you need some sort of air assist. While
using your laser your material will produce smoke. This smoke if not directed away will stick to the
material you are working with producing a sooty poor looking cut or etching. This smoke will also
stick to the laser’s lens and very quickly build up heat before you know it the lens will break.
Bare minimum you need to have a
[40mm](https://shop.v1engineering.com/collections/miscellaneous/products/fan) fan clearing the area,
even better are
[radial](https://shop.v1engineering.com/collections/miscellaneous/products/radial-fan) fans (higher
pressure more direct), or even better yet a [small compressor](https://amzn.to/2SBnbkg). If you have
the ability to hook up your compressor and aim the air stream you can get significantly better cuts
this way. Once again don’t forget to vent your fumes safely and accordingly.

---

## The Hard Part

### Choosing

![pewpew](https://www.v1engineering.com/wp-content/uploads/2019/01/pew_pew.jpg){: loading=lazy width="300"}

Choosing which laser to buy can be the hardest part.

If this all already seems overwhelming just buy a [JTechPhotonics
kit](https://jtechphotonics.com/?product_cat=laser-and-driver-combo-kits).
Why; it is a trusted laser/company, glasses proven suitable for it, complete kits available, the
only kit that is [US
legal](https://www.fda.gov/Radiation-EmittingProducts/RadiationEmittingProductsandProcedures/HomeBusinessandEntertainment/LaserProductsandInstruments/default.htm),
and the connections and use are as simple as it gets (more later). I think the 2W kits are a great
deal. If you have other companies to suggest please let me know, and I will check them out.


### PWM, TTL, WTF?

PWM, and TTL in this context are just how the power of the laser is controlled. All we really care
about is if the laser is controlled by 5V or 12V. Good brands and companies make this abundantly
clear, if you are buying an import this is by far the hardest part of the whole thing. The specs are
not clear, the wiring diagrams are typically non-existent and if they are they can be wrong, we even
have drivers with PCB’s with misprinted polarity so you can’t even follow that. Unfortunately import
lasers, while super cheap, tend to be a guess and check game, both with connections and lens specs.

With all common boards we can handle 12V and 5V signals, no big deal!

**12V** signal driven lasers are less common (Jtech). They are simple, you plug them into the print fan
port (or any 12V port) on your control board and you are good to go. Using a 12V port you will
typically use M106 SXXX to turn the laser on and M107 to turn the laser off. The Sxxx is the laser
strength with a value between 0-255, 255 being the most power.

**5V** driven lasers need a firmware edit to assign the right pin for your board, this just reassigns
the 12v fan pin to instead control a 5V pin. After that the same rules apply, use M106 SXXX to turn
the laser on and M107 to turn the laser off. The Sxxx is the laser strength with a value between
0-255, 255 being the most power.  ([Thanks Guffy](https://www.v1engineering.com/forum/topic/another-laser/#post-83368))

---

Rambo=45
:   ![rambo](https://www.v1engineering.com/wp-content/uploads/2017/04/IMG_20180626_1559002.jpg){: loading=lazy width="400"}

---

Archim=53?

---

MiniRambo=23

---

Ramps=44
:   ![!ramps](https://www.v1engineering.com/wp-content/uploads/2019/01/Leo44Pic.jpg){: loading=lazy width="400"}

---

### Leo’s Laser

A short DIY guide to building your own diode laser and power supply. Leo was the first one that made Lasers seem doable, even for me. My [Leo
laser](https://www.v1engineering.com/the-2-8-watt-100-laser/) is still working perfectly. The Import lasers are pretty stable now, so this guide is a bit out of date. Thanks a million Leo69 for getting us all started with the Pew Pew's.

## Software

TODO script description

### Using your laser

TODO

Need some suggestions here….

### Image based, Raster

[Image2Gcode](https://www.thingiverse.com/thing:2726163) – [Forum link](https://www.v1engineering.com/forum/topic/image2gcode-free-raster-image-laser-engraving-software-modified-for-mpcnc/page/11/#post-78280)

Vector based, Solid lines

[Inkscape Plug-In –](https://jtechphotonics.com/?page_id=2012)

[dxf2gcode](https://sourceforge.net/projects/dxf2gcode/) – [Forum link](https://www.v1engineering.com/forum/topic/dxf2gcode-a-quick-simple-open-source-app-for-vectordxfpdf-laser-engraving/)

## Gallery

TODO laser gallery link
