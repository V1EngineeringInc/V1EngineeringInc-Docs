# v1pi

![Landing Page](https://www.v1engineering.com/wp-content/uploads/2018/05/v1pi.png) 

[OctoPrint](https://octoprint.org/), [CNC.js](https://cnc.js.org/docs/), Raspberry Pi, CNC control from your phone… any of those pique your interest? It
has never been this easy to try them out. Jeffeb3 (El Heffe) has taken it to the next level of ease,
**v1pi**.

Previously we had Daniel Dunn’s guide,
[here](http://danielwdunn.com/mpcnc-with-cncjs-wireless-web-interface/). Honestly I was intimidated
even though Daniel laid out a very clear and detailed walk through.

![!CNC.js](https://www.v1engineering.com/wp-content/uploads/2018/05/cncjs.png){: loading=lazy width="400"}

Well Heffe made a pre-made image. It takes 2 steps, It worked for me first try. Load the imagine
onto a MicroSD card, boot the Pi, done. Seriously. You even have options, If you have WiFi access
near your machine you can connect to it, if not it will run as a hot spot and you can connect to it
that way. You can move that machine from any device connected on that network, add a live cam (to
show the world what you are doing, not to leave your machine alone…FIRE), run files, so much.
Please at least drop into one of the links and give him a thanks, this is an insanely easy to use
piece of work.

![!Octoprint](https://www.v1engineering.com/wp-content/uploads/2018/05/octo.jpg){: loading=lazy width="400"}

The [forum thread](https://www.v1engineering.com/forum/topic/v1pi-raspberry-pi-image-with-octoprint-and-cnc-js-and-wifi-hotspot/).

GitHub link to the [file and instructions](https://github.com/jeffeb3/v1pi).

The program let me load the image on a windows machine, [Etcher.io](https://etcher.io/).

Heffe once again, you are amazing, and I appreciate your hard work more than you could know.

 
???+ "CNC.js currently has a tiny issue"
     There's an issue with a timeout failing, and the `ok` getting
     missed. There is a solution to commenting out a line, and there’s a GitHub issue for it. The
     workaround is to send some other command in the terminal window, which will send another `ok`. I
     just send `G1 X0`.
