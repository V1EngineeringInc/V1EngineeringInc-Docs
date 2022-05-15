<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# ZenXY v2 Size Calculator
----

## Sizing

The ZenXY v2 has two dimensions to take into consideration. The footprint of the machine is the
minimum dimensions needed to build it. The "image dimension" is the size of the field the machine can
produce designs in (the firmware number). The one consideration is the image area also contains the steel ball width, so
"image dimension" (X or Y) + diameter (one radius on each side) gives you the "actual area needed".

![!ZenXY v2 Working area](https://www.v1engineering.com/wp-content/uploads/2021/03/Working-area.jpg){: loading=lazy width="400"}

This picture does not include the ball diameter. For example the offset (92mm) for a half inch ball
(12.7mm) would be 92mm-6.35mm or 85.65mm. For table designs that are not exact fitting this doesn't
really come into play. The calculator below does have this factored in.

The height/thickness of the machine is 66mm plus the thickness of your spacers. Most steppers will protrude
further than that. If you are planning on covering the bottom to keep fingers out, plan to have
small stepper cutouts to keep thickness to a minimum. If you do want to cover it all, the thickness
will be 40.25mm plus the stepper thickness with a minimum of 66mm.


----
## Inputs

#### Units
<input type="radio" onchange="to_mm()" name="units" value="mm" checked>Metric (mm)<br/>
<input type="radio" onchange="to_inch()" name="units" value="inches">Imperial (inch)<br/>

#### Model
<input type="radio" onchange="from_working()" name="model" value="us_version" checked> US Version<br/>
<input type="radio" onchange="from_working()" name="model" value="other_version" disabled> Other Version<br/>

----

## Size Calculator

#### ZenXY Build Footprint
<!-- These "value"s are going to be overwritten by the reset_work() function below. -->
<input class="calc" type="number" onchange="from_working()" name="xfootprint" value="410" size="8"><span class="units">mm</span> X - Left / Right<br/>
<input class="calc" type="number" onchange="from_working()" name="yfootprint" value="370" size="8"><span class="units">mm</span> Y - Forward / Back<br/>
<input class="calc" type="number" onchange="from_working()" name="balldiameter" value="12.75" size="4"><span class="units">mm</span> Ball Diameter<br/>
<button class="reset" onclick="reset_work()">Reset</button>

#### Part Lengths
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="xrails"></span>|2|x rails, small|
|<span name="yrails"></span>|2|y rails, large|
|<span name="belt"  ></span>|1|belt length|


#### Work area
|Length (<span class="units">mm</span>)| Name |
|--------------------------------------|------|
|<span name="xarea"></span>|X image dimensions|
|<span name="xballarea"></span>|X actual area needed|
|<span name="yarea"></span>|Y image dimensions|
|<span name="yballarea"></span>|Y actual area needed|


<script>

function get_unit_convert() {
  // Get the currently chosen units.
  var units = $("input[name=units]:checked").val();

  // Get the multiplier.
  var unit_convert = 1.0;
  if (units == "mm") {
    // We have mm selected.
    unit_convert = 1.0;
  } else if (units == "inches") {
    // We have inches selected.
    unit_convert = 1.0/25.4;
  }
  else {
    alert("internal error: unrecognized units " + units);
  }
  return unit_convert;
}

function get_offsets() {

  const unit_convert = get_unit_convert();

  var us_version = {};
  us_version.xrail_offset = 96 * unit_convert;
  us_version.yrail_offset = 92.5 * unit_convert;
  us_version.xwork_offset = 184 * unit_convert;
  us_version.ywork_offset = 184 * unit_convert;
  us_version.extra_belt = 200 * unit_convert;

  var other_version = {};
  // TODO These are not correct.
  other_version.xrail_offset = 96 * unit_convert;
  other_version.yrail_offset = 92.5 * unit_convert;
  other_version.xwork_offset = 184 * unit_convert;
  other_version.ywork_offset = 184 * unit_convert;
  other_version.extra_belt = 200 * unit_convert;

  var model = $("input[name=model]:checked").val();
  if (model == "us_version") {
    return us_version;
  }
  else if (model == "other_version") {
    return other_version;
  }
  else {
    alert("internal error: unrecognized model " + model);
  }
}

function to_mm() {
  // Find all the labels and change them to mm
  $(".units").text("mm");

  // Set the step attributes (you can also set other attributes here, like min, max, whatever)
  $("input[name=xfootprint]").attr({ "step": 10.0 });
  $("input[name=yfootprint]").attr({ "step": 10.0 });
  $("input[name=balldiameter]").attr({ "step": 0.25 });

  // Get the current values.
  var xfootprint = parseFloat($("input[name=xfootprint]").val());
  var yfootprint = parseFloat($("input[name=yfootprint]").val());
  var balldiameter = parseFloat($("input[name=balldiameter]").val());

  // Change the units.
  // This Math.round(... * 10.0) / 10.0 is to round to the step.
  $("input[name=xfootprint]").val(Math.round(xfootprint * 25.4 * 0.1) / 0.1);
  $("input[name=yfootprint]").val(Math.round(xfootprint * 25.4 * 0.1) / 0.1);
  $("input[name=balldiameter]").val(Math.round(balldiameter * 25.4 * 0.1) / 0.1);

  // Recalculate the rest of the page.
  from_working();
}

function to_inch() {
  // Find all the labels and change them to inches
  $(".units").text("inches");

  // Set the step attributes (you can also set other attributes here, like min, max, whatever)
  $("input[name=xfootprint]").attr({ "step": 0.25 });
  $("input[name=yfootprint]").attr({ "step": 0.25 });
  $("input[name=balldiameter]").attr({ "step": 0.125 });

  // Get the current values.
  var xfootprint = parseFloat($("input[name=xfootprint]").val());
  var yfootprint = parseFloat($("input[name=yfootprint]").val());
  var balldiameter = parseFloat($("input[name=balldiameter]").val());

  // Change the units.
  $("input[name=xfootprint]").val(clip(xfootprint / 25.4));
  $("input[name=yfootprint]").val(clip(yfootprint / 25.4));
  $("input[name=balldiameter]").val(clip(balldiameter / 25.4));

  // Recalculate the rest of the page.
  from_working();
}

function clip(value) {
  return Math.round(value * 4) / 4; // Round to 0.25
}

function reset_work() {
  const unit_convert = get_unit_convert();
  $("input[name=xfootprint]").val(clip(550 * unit_convert));
  $("input[name=yfootprint]").val(clip(600 * unit_convert));
  $("input[name=balldiameter]").val(clip(12.7 * unit_convert));
  from_working();
}

function from_working() {
  var offsets = get_offsets();

  var xfootprint = parseFloat($("input[name=xfootprint]").val());
  var yfootprint = parseFloat($("input[name=yfootprint]").val());
  var balldiameter = parseFloat($("input[name=balldiameter]").val());

  var xrails = xfootprint - offsets.xrail_offset;
  var yrails = yfootprint - offsets.yrail_offset;
  var belt = xrails * 4 + yrails * 4 + offsets.extra_belt;

  var xarea = xfootprint - offsets.xwork_offset;
  var yarea = yfootprint - offsets.ywork_offset;
  var xballarea = xfootprint - offsets.xwork_offset + balldiameter;
  var yballarea = yfootprint - offsets.ywork_offset + balldiameter;

  $("span[name=xfootprint]").text(clip(xfootprint));
  $("span[name=yfootprint]").text(clip(yfootprint));
  $("span[name=balldiameter]").text(clip(balldiameter));

  $("span[name=xrails]").text(clip(xrails));
  $("span[name=yrails]").text(clip(yrails));
  $("span[name=belt]").text(clip(belt));
  $("span[name=xarea]").text(clip(xarea));
  $("span[name=yarea]").text(clip(yarea));
  $("span[name=xballarea]").text(clip(xballarea));
  $("span[name=yballarea]").text(clip(yballarea));
}

// Set these up the first time.
$(window).on('load', function(){
  // Get back to mm
  $("input[value=mm]").prop('checked', true);
  $("input[value=inches]").prop('checked', false);

  to_mm();

  reset_work();
});

</script>
