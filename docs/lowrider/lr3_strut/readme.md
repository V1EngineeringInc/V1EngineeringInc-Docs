# Lowrider 3 mod, generate all the Struts

Forked/copied from https://github.com/aaronse/v1engineering-mods/tree/main/lowrider3/strut-plate-variable

## Summary
- Generate *ALL the Strut .SVG files, in 1mm increments, so that LR3 builders don't have to.
- For more context, see https://forum.v1engineering.com/t/lowrider-3-cnc-lr3-release-notes/32748/350

*ALL - as in all the possible sizes that would be rationally chosen 480mm to 1700mm, in 1mm increments.
- From https://docs.v1engineering.com/lowrider/calculator
  - Min 12" Usable Cutting Area would have 480mm Tube/Strut Length
  - Max 60" Usable Cutting Area would have 1700mm Tube/Strut Length 
 

## Usage
- Generate strut .SVG files (Window CMD shell) :
```
for /l %i in (480,1,999) do "C:\Program Files\OpenSCAD\openscad.exe" --D "beam_len=%i" -q -o svg_0\lr3-strut-plate-variable_%i.svg LR3-strut-plate-variable.scad

for /l %i in (1000,1,1700) do "C:\Program Files\OpenSCAD\openscad.exe" --D "beam_len=%i" -q -o svg_1\lr3-strut-plate-variable_%i.svg LR3-strut-plate-variable.scad
```
- Publish somewhere folks can access, e.g. this repo
- Test/Verify Output.  For example generate a test.html file, zoom out and scroll through, eyeball verify quality... :
```
echo ^<html^>^<style^>body {font-size:100px; white-space:nowrap }^</style^>^<body^> > test.html
for /l %i in (480,1,999) do echo ^<br/^>%i ^<img src=svg_0/lr3-strut-plate-variable_%i.svg /^> >> test.html
for /l %i in (1000,1,1700) do echo ^<br/^>%i ^<img src=svg_1/lr3-strut-plate-variable_%i.svg /^> >> test.html
echo ^</body^>^</html^> >> test.html
start test.html
```

## Acknowledgments
- Copied/forked OpenSCAD script from Jamie's https://www.printables.com/model/206716-lr3-strut-plate-variable
  - For context, see https://forum.v1engineering.com/t/lowrider-3-cnc-lr3-release-notes/32748/93?u=aaronse


## License
- This work is licensed under a [Creative Commons (4.0 International License) Attribution—Noncommercial—Share Alike](http://creativecommons.org/licenses/by-nc-sa/4.0/)
