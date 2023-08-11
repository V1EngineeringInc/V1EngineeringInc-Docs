Version=11244
Setting type=Postprocessor settings
Length unit CNC=mm
Feed unit CNC=mm_min
File extension=gcode
Use arcs=yes
I/J relative=yes
Program start text=
[>>>]
(Project <project>)
(Created by Estlcam version <version> build <build>)
(Machining time about <time> hours)

(Required tools:)
<tools>
G21
G90
G94
G92 X0 Y0
M0 (MSG Attach probe)
G38.2 Z-80 F200 P0.5 ( probe down set thickness )
G1 Z10 F900
M0 (MSG Remove probe)
M62 P0 ( start spindle pin26 )

[<<<]
Program end text=
[>>>]

M63 P0 ( stop spindle pin26 )
$HZ
M30
[<<<]
Operation start text=
[>>>]


(No. <order>: <name>)
[<<<]
Tool change text=
[>>>]
M63 P0 ( turn off pin 26)
$HZ (Home Z)
G0 X0 Y10 F2520 
M0 (MSG change tool, probe)
G38.2 Z-80 F200 P0.5 ( Probe set thickness)
G00 Z10.0000 F500 ( Clearance )
M0 (MSG remove probe)
M62 P0 ( turn on pin26 )
[<<<]
Start cut text=
End cut text=
Name X=X
Format X=
Order X=2
Scale X=1
Enable X=yes
Repeat X=no
Name Y=Y
Format Y=
Order Y=3
Scale Y=1
Enable Y=yes
Repeat Y=no
Name Z=Z
Format Z=
Order Z=4
Scale Z=1
Enable Z=yes
Repeat Z=no
Name I=I
Format I=
Order I=5
Scale I=1
Enable I=yes
Repeat I=yes
Name J=J
Format J=
Order J=6
Scale J=1
Enable J=yes
Repeat J=yes
Name F=F
Format F=
Order F=7
Scale F=1
Enable F=yes
Repeat F=no
Name S=S
Format S=
Order S=8
Scale S=1
Enable S=yes
Repeat S=no
Name N=
Format N=
Order N=1
Scale N=1
Enable N=no
Repeat N=no
Plot axis Z=no
Up Z=
Down Z=
Rapid feed XY=15000
Rapid feed Z=3000
Initial value N=1
Command rapid move=G0
Command linear move=G1
Command clockwise arc=G2
Command counterclockwise arc=G3
Command order=1
Command repeat=yes
Encoder=ASCII
Delimiter= 
Decimal point=.
Line end=
Character replacements=
[>>>]
Ä|Ae
Ö|Oe
Ü|Ue
ä|ae
ö|oe
ü|ue
ß|ss
[<<<]
Lock units=no
Special formatter=Off
