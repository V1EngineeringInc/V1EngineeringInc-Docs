
## Vcarve inlay process using F-engrave ##

- Select the picture you want to use for your inlay
  <img src="hummingbird.jpg" alt="Humming Bird" width="250" height="220" align="right">
    - It is best to use a dxf or bmp file
    - It is better to use a black and white picture
    - The detail in the picture will determine its suitability for inlay work
  
     
- Prepare the picture for use with F-engrave
    - I use Inkscape or Gimp or plain old Windows Paint
    - You may have to do some work on simplifying the picture or enhancing the details

* Start F-engrave and import your picture

    + The picture will display, some of the imperfections may be purely the representation but others may cause your inlay part to have defects
    + Make the necessary selections with F-engrave – see [Scorchworks instructions](http://www.scorchworks.com/Fengrave/fengrave.html#documentation "Scorchworks F-Engrave instructions")
    + Use the save Gcode option (this will be the “MAIN” file)
    + Save the Clean Gcode and the Vclean Gcode
       - If there is nothing to Clean or Vclean F-engrave will complain that the clean up hasn’t been run.

<img src="Capture1.JPG" alt="F-Engrave Screen" width="650" height="500" align="center">

**I use the following;**
    
<img src="Capture2.JPG" alt="F-Engrave Screen" width="750" height="500" align="center">
    
----
    
* **Start MODfef and process the output files from F-engrave**

    + Select the Main file, the “VCLEAN” file and the “CLEAN” file
    + You can also select a customer start file and end file (these are not produced by F-engrave)
    + You can select the file extension for your gcode file
    + You can enter a tool change line. The program will insert a pause here so you can change your cutter on the machine.
    + You can enter the character that should be used for comments. F-engrave will enclose comments in parentheses () by default.
    + You can choose if you want the files to concatenated. If you select this it will make one file with a tool change.
    + The output file will have the same name as the “MAIN” file but with your new extension.
    + The concatenated file will run the “START” file (if one is selected), then the “MAIN” file, then the “VCLEAN” file (if one is selected), then the tool change, then the “CLEAN” file (if one is selected), then the “END” file (if one is selected).

<img src="Capture3.JPG" alt="F-Engrave Screen" width="850" height="500" align="center">

    
+ Load the MODfef processed gcode file into Octoprint (or your gcode streamer)
+ Select appropriate wood for the inlay
    - Choose contrasting wood for the male and female parts
        - The male part is wood that will be inlayed.
        - The female part is the wood that will have the inlay glued into it.
+ Cut the female part
+ Cut the male part
+ Clean up the parts
    - I use a scalpel to clean any edges or corners that need it.
    - I also remove any burs that may be present.
    - I dry fit them to see that the gap between the male and female parts are consistent.
    - If it doesn’t look right using some color on the inlay protrusions during a dry fit can help to show where the parts are interfering.
+ Glue the parts together
    - I use regular wood glue and leave it to dry overnight
    - It is important to clamp the parts evenly as you can influence the fit which will spoil the inlay effect.
+ Trim the excess from the inlay (male part)
    - I usually do this on the band saw but you can do it with any tool that will remove the excess wood without dislodging the inlay.
+ Sand the part down until the inlay is flush
    - There is normally quite a bit of inlay wood to be removed, some form of belt sander works very well here.
+ Finish the part with the appropriate finish
    - It depends on the type of wood you have chosen. Select a finish that will work with both the female wood and the male wood.

----

## References: ##

F-Engrave - [Website](https://www.google.com "Scorchworks F-Engrave site")


MODfef - [Download](https://www.jobbos.com/MODfef/MODfef2.zip "Download the zip file with for MODfef")


Inkscape - [Website](https://www.inkscape.org/ "Inkscape site")


Gimp - [Website](https://www.gimp.org/ "Gimp site")


Octoprint - [Website](https://www.octoprint.org/ "Octoprint site")


MPCNC - [Website](https://www.v1engineering.com/ "V1 Engineering site")


Hummingbird Picture - [Website](https://www.clipart.email/download/1122147.html "Clipart site")
