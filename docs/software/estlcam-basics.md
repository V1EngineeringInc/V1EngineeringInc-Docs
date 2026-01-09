# Estlcam Basics


![!Estlcam Preview](../img/old/2015/05/ESTLCAM.png){: loading=lazy width="400"}

**EstlCAM is for making tool paths.**

Estlcam seem to be the easiest way to generate CNC tool paths that we can find. Generally this is used for everything except work with lasers, for that [lightburn](../tools/lasers.md/#lightburn) is the better program. This is a low cost program with a mostly unlimited free trial. anything you learn from estlcam will transfer over to other cam software so no time is "wasted" by starting with this program even if you are confident you will use another software package later.

Estlcam is also very easy for everyone here to troubleshoot. If you have CAM issues with other software you are pretty much on your own. Most of us know estlcam very well and can help you get going very easily.

If you are unsure what a tool path or CAM is I suggest taking a look at this page, [CNC Software Basics](../learn/software_overview.md/#tool-path-generationcam)

## Step one – Install Estlcam

[Estlcam is found here.](http://estlcam.com) Currently we recommend Estlcam V12.

![!language](../img/software/es1.jpg){: loading=lazy width="400"}

The installer starts in German, you will be able to change this later.

Deselect option shown below.  We can't use this with Jackpot/SKR Control Boards.

---

![!controller deselect](../img/software/es2.jpg){: loading=lazy width="400"}

Install Estlcam. Using the default options in the installer, remove the one controller option shown here.

---

![!language](../img/software/es3.jpg){: loading=lazy width="400"}

 You will now need to launch Estlcam and continue the setup. In the top menu select Setup/basic setting. Match all the setting shown here, pay close attention to the seconds and minutes selection shown, it is common for people to get this wrong.

 If you are using the Jackpot CNC controller select **"GRBL"** here.

 If you are using the SKR pro or other older V1 boards select **"Marlin"** here.

 For now other than language it is best just to match all of the settings shown. Only change these later if you understand them completely and have completed a job on your own. If you ask for help chances are we are going to ask to see this screen.

After you click okay close Estlcam and restart it to update the settings.


## Step 2 – First Use Estlcam Setup


![!Esetup](../img/software/e4.jpg){: loading=lazy width="400"}

Next menu is "Setup/CNC Programs" Then "Presets" tab. Change the file extension “gcode” so all the programs recognize it.

---

![!texts setup](../img/software/es5.jpg){: loading=lazy width="400"}

The next tab to set is the "texts" tab. This is where you enter the starting, ending, and tool change setting from the [Milling Basics](../tools/milling-basics.md/#starting-gcode) Gcode section. 

These will vary depending on your control board, but you can simply cut and paste the sections if you are using GRBL or Marlin.

---

![!values setup](../img/software/es6.jpg){: loading=lazy width="400"}

In the "Values" tab, It is best to repeat the "F" values on each line, and this is where you set your "rapids" values. The values shown should work for everyone but can be modified later after evaluating your build to save a little time and move faster between cuts.

Click "OK" to save, That is all it takes to get estlcam speaking the language the control board needs. You should not have to change any of those setting often if ever again.

---

You are ready to generate some GCode.

## Step 3 – 2D gcode, Good for pen plotting or 2D milling (cutting things out)

For this 2D or 2.5D work .DXF files are used. You can use any vector program to make them,
illustrator, Inkscape, SolidWorks, fusion, Onshape, etc.

I used this one, [Crown Vector](../img/software/crown.zip), in the [video](https://youtu.be/s8YwkcK3P9U).

Open DXF. **File>Open** – If your DXF is completely the wrong size try again with different initial
units.

![!eopen](../img/software/es8.jpg){: loading=lazy width="400"}

---

This is what the crown looks like, notice there is no indication of size.

![!esize](../img/software/es9.jpg){: loading=lazy width="400"}

---

## Step 4 – Scale / Re-Zero


#### Grid Size. 

DXF files can be crazy sizes sometimes so to make sure your DXF is the right size change the
grid. Found in teh bottom left hand corner of the screen. I set mine to a number that makes sense for the job at hand, in this case 10mm, or 25.4mm=1in.

![!eGrid](../img/software/es10.jpg){: loading=lazy width="400"}

---

The crown imported at about 55mm wide I want about 150mm wide.

**Select>Resize>Drawing Layers**, then click on the DXF to select it. I scaled the crown 250x to get it
to 150mm (5 3/4″).  Zoom out to see your DXF.

![!eescale](../img/software/es11.jpg){: loading=lazy width="400"}

---

**Zero>Create arbitrary point**, then select outside of the DXF paths. This is how to set your origin
(or Home). The little blue plus symbol is what your machine sees as 0,0 (x=0, y=0, generally the
lower left corner of your work). When you start your program the machine will work to the right and
above where you start it from (represented by the blue plus). Some people like to work from the
center for round or oval objects.

![!ezero](../img/software/es12.jpg){: loading=lazy width="400"}

---

## Step 5 – Make the tool paths

Before making a tool path you need to define your tool. For this example I will set it up as a "pen" but this will work with an endmill if you want to live dangerously. Setting the right diameter will help visualize how the job will actually look.

![!ezero](../img/software/espen.jpg){: loading=lazy width="400"}

---

when using a pen you want to draw **on** the line, so use engrave tool (centered on line). Click **Engrave** then just click on each line segment.

![!ezero](../img/software/espaths.jpg){: loading=lazy width="400"}

---

## Step 6 – Save

Export. **File>Save CNC Program**. Give it a name. You will get a depth popup, for the pen I use 1mm or
less, anything else, set it to the thickness of your material plus a bit to cut all the way through.
You can then preview the path.

![!ezero](../img/software/essim.jpg){: loading=lazy width="400"}

---

If you hold the left mouse button and drag you will get a depth view of your job. Always check this to make sure the moves look right. Red dashed lines are travel moves and should be above your work.

![!ezero](../img/software/esleftmouse.jpg){: loading=lazy width="400"}

---

## Step 7 – Running the Code

Power up your machine and drive the pen or router to surface of your material. Drive the tip of the pen (or tool) a hair above where you want it to start and start the file you just created. 

It should pick up, move to the start, move down and start drawing/cutting. 

## Test File

Marlin, SKR Pro, rambo, ramps -  [Test Crown GCODE](../img/old/2015/09/Test-Crown-12mms.gcode)– [Test Crown Zipped file](../img/Test-Crown-12mms.zip).

GRBL, Jackpot - [Grbl Test Crown](../img/software/crownGRBL.gcode) - [Grbl Test Crown Zip](../img/software/crownGRBL.zip)

This all it takes to plot with a pen or do basic 2D (2.5D) milling, some of the most common
things this type of mill is used for. Make sure to adjust your tool and its settings depending on
the material in use. Always do a test cut!

Here is an old video

<iframe width="560" height="315" src="https://www.youtube.com/embed/s8YwkcK3P9U"
  title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
  clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This video is of the very first MPCNC, drawing the very first test crown (that I still have framed in my room). This video still makes me smile ear to ear, I am very proud of it even though we can do so much more and so much faster these days. At the time this was amazing and I hope your first crown feels the same way.

**P.S.** The crown's "Jewel" is not perfectly round. 

## Milling Basics

Once you can do some drawings and you are ready to try and cut something, here are some [Milling Basics](../tools/milling-basics.md).
