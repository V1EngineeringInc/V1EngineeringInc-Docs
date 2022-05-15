<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# MPCNC Size Calculator
----

## Sizing

When choosing what size to make your machine, start with the _build area_. This is the area your
tool can reach. Smaller machines are more rigid. The more rigid a machine is, the easier and more
forgiving it is to use. This gives you a larger acceptable feeds and speeds window. More rigid
also means it will be faster and more accurate with the right settings. Every millimeter counts but
**the Z axis has the largest effect on rigidity**. For a Primo MPCNC, 81mm is the shortest and **I
highly** recommend that. More sizing details on [this page](https://www.v1engineering.com/assembly/machine-size/).

![!MPCNC ISO Diagram](https://www.v1engineering.com/wp-content/uploads/2020/06/ISO-Diagram2.jpg){: loading=lazy width="400"}

![!MPCNC Side Diagram](https://www.v1engineering.com/wp-content/uploads/2020/06/Primo-Calc-diagram-1.jpg){: loading=lazy width="400"}

----
## Inputs

#### Units
<input type="radio" onchange="to_mm()" name="units" value="mm" checked>Metric (mm)<br/>
<input type="radio" onchange="to_inch()" name="units" value="inches">Imperial (inch)<br/>

#### Model
<input type="radio" onchange="from_working()" name="model" value="Primo" checked> Primo<br/>
<input type="radio" onchange="from_working()" name="model" value="Burly"> Burly<br/>

#### Tool Choice \*
<input type="radio" onchange="from_working()" name="tool" value="Pen" checked> Full range of motion (pen, laser, drag knife, Makita RT70x, etc)<br/>
<input type="radio" onchange="from_working()" name="tool" value="DW660"> Dewalt DW660<br/>
<input type="radio" onchange="from_working()" name="tool" value="55mm"> 52mm & 55mm Spindle<br/>

!!! note "* Tool Choice"
    Larger tools may collide with the side rails and restrict movement
    before the MPCNC reaches its full range of motion in X and Y.
    Select your intended tool to account for this difference in the following dimensions:

----

## Size Calculator

#### Workspace
<!-- These "value"s are going to be overwritten by the reset_work() function below. -->
<input class="calc" type="number" onchange="from_working()" name="xwork" value="450" size="6"><span class="units">mm</span> x<br/>
<input class="calc" type="number" onchange="from_working()" name="ywork" value="330" size="6"><span class="units">mm</span> y<br/>
<input class="calc" type="number" onchange="from_working()" name="zwork" value="81" size="6"><span class="units">mm</span> z<br/>
<button class="reset" onclick="reset_work()">Reset</button>

#### Tube Lengths
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="xrails"     ></span>|2|x rails, sides|
|<span name="xgantryrail"></span>|1|x rail, gantry|
|<span name="yrails"     ></span>|2|y rails, sides|
|<span name="ygantryrail"></span>|1|y rail, gantry|
|<span name="zrails"     ></span>|2|z rails|
|<span name="zlegs"      ></span>|4|legs|
|<span name="rail_total" ></span>|**total needed**| total tube length assuming 3mm kerf|

#### Material Dimensions
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="leadscrew" ></span>|1|leadscrew length|
|<span name="xbelts"    ></span>|2|belt length along x|
|<span name="ybelts"    ></span>|2|belt length along y|
|<span name="belt_total"></span>|**total length**| belts (all 4)|

#### Table Size
|Length (<span class="units">mm</span>)| Name |
|--------------------------------------|------|
|<span name="xtable"></span>|x table size (outer edges of feet)|
|<span name="ytable"></span>|y table size (outer edges of feet)|

#### Total Machine Footprint
|Length (<span class="units">mm</span>)| Name |
|--------------------------------------|------|
|<span name="xbound" ></span>|x|
|<span name="ybound" ></span>|y|
|<span name="zbound" ></span>|z|
|<span name="zbound2"></span>|clearance to remove z axis|

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

  var burly = {};
  burly.xrail_minus_work = 264 * unit_convert;
  burly.xgantryrail_minus_work = 264 * unit_convert;
  burly.yrail_minus_work = 264 * unit_convert;
  burly.ygantryrail_minus_work = 264 * unit_convert;
  burly.zrail_minus_work = 190 * unit_convert;
  burly.zleg_minus_work = -13 * unit_convert;
  burly.xtable_minus_rail = 20 * unit_convert;
  burly.ytable_minus_rail = 20 * unit_convert;
  burly.xbound_minus_rail = 30 * unit_convert;
  burly.ybound_minus_rail = 30 * unit_convert;
  burly.zbound_minus_rail_and_work = 50 * unit_convert;
  burly.zleadscrew_minus_work = 76 * unit_convert;
  burly.xbelt_minus_rail = 136 * unit_convert;
  burly.ybelt_minus_rail = 136 * unit_convert;
  burly.kerf = 3 * unit_convert;

  var primo = {};
  primo.xrail_minus_work = 304 * unit_convert;
  primo.xgantryrail_minus_work = 249 * unit_convert;
  primo.yrail_minus_work = 313 * unit_convert;
  primo.ygantryrail_minus_work = 258 * unit_convert;
  primo.zrail_minus_work = 190 * unit_convert;
  primo.zleg_minus_work = -21 * unit_convert;
  primo.xtable_minus_rail = -34 * unit_convert;
  primo.ytable_minus_rail = -34 * unit_convert;
  primo.xbound_minus_rail = 68 * unit_convert;
  primo.ybound_minus_rail = 68 * unit_convert;
  primo.zbound_minus_rail_and_work = 50 * unit_convert;
  primo.zleadscrew_minus_work = 50 * unit_convert;
  primo.xbelt_minus_rail = 50 * unit_convert;
  primo.ybelt_minus_rail = 50 * unit_convert;
  primo.kerf = 3 * unit_convert;

  var tool = $("input[name=tool]:checked").val();
  if (tool == "Pen") {
    // don't clip the working space at all
  }
  else if (tool == "DW660") {
    // working space clipped by this much (not necessarily the same between burly and primo
    burly.xrail_minus_work = burly.xrail_minus_work + 10 * unit_convert;
    burly.xgantryrail_minus_work = burly.xgantryrail_minus_work + 10 * unit_convert;
    burly.yrail_minus_work = burly.yrail_minus_work + 8 * unit_convert;
    burly.ygantryrail_minus_work = burly.ygantryrail_minus_work + 8 * unit_convert;
    burly.zrail_minus_work = burly.zrail_minus_work + 2.75 * unit_convert;
    burly.zleg_minus_work = burly.zleg_minus_work + 2.75 * unit_convert;

    primo.xrail_minus_work = primo.xrail_minus_work + 9 * unit_convert;
    primo.xgantryrail_minus_work = primo.xgantryrail_minus_work + 9 * unit_convert;
    primo.yrail_minus_work = primo.yrail_minus_work + 9 * unit_convert;
    primo.ygantryrail_minus_work = primo.ygantryrail_minus_work + 9 * unit_convert;
    primo.zrail_minus_work = primo.zrail_minus_work + 2.75 * unit_convert;
    primo.zleg_minus_work = primo.zleg_minus_work + 2.75 * unit_convert;
  }
  else if (tool == "55mm") {
    // working space clipped by this much (not necessarily the same between burly and primo
    primo.xrail_minus_work = primo.xrail_minus_work + 3 * unit_convert;
    primo.xgantryrail_minus_work = primo.xgantryrail_minus_work + 3 * unit_convert;
    primo.yrail_minus_work = primo.yrail_minus_work + 3 * unit_convert;
    primo.ygantryrail_minus_work = primo.ygantryrail_minus_work + 3 * unit_convert;
    primo.zrail_minus_work = primo.zrail_minus_work + 2.5 * unit_convert;
    primo.zleg_minus_work = primo.zleg_minus_work + 2.5 * unit_convert;
  }
  else {
    alert("internal error: unrecognized tool " + tool);
  }

  var model = $("input[name=model]:checked").val();
  if (model == "Primo") {
    return primo;
  }
  else if (model == "Burly") {
    return burly;
  }
  else {
    alert("internal error: unrecognized model " + model);
  }
}

function to_mm() {
  // Find all the labels and change them to mm
  $(".units").text("mm");

  // Set the step attributes (you can also set other attributes here, like min, max, whatever)
  $("input[name=xwork]").attr({
    "step": 10.0
  });
  $("input[name=ywork]").attr({
    "step": 10.0
  });
  $("input[name=zwork]").attr({
    "step": 1
  });

  // Get the current values.
  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var zwork = parseFloat($("input[name=zwork]").val());

  // Change the units.
  // This Math.round(... * 10.0) / 10.0 is to round to the step.
  $("input[name=xwork]").val(Math.round(xwork * 25.4 * 0.1) / 0.1);
  $("input[name=ywork]").val(Math.round(ywork * 25.4 * 0.1) / 0.1);
  $("input[name=zwork]").val(Math.round(zwork * 25.4));

  // Recalculate the rest of the page.
  from_working();
}

function to_inch() {
  // Find all the labels and change them to inches
  $(".units").text("inches");

  // Set the step attributes (you can also set other attributes here, like min, max, whatever)
  $("input[name=xwork]").attr({
    "step": 0.25
  });
  $("input[name=ywork]").attr({
    "step": 0.25
  });
  $("input[name=zwork]").attr({
    "step": 0.25
  });

  // Get the current values.
  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var zwork = parseFloat($("input[name=zwork]").val());

  // Change the units.
  $("input[name=xwork]").val(clip(xwork / 25.4));
  $("input[name=ywork]").val(clip(ywork / 25.4));
  $("input[name=zwork]").val(clip(zwork / 25.4));

  // Recalculate the rest of the page.
  from_working();
}

function clip(value) {
  return Math.round(value * 4) / 4; // Round to 0.25
}

function reset_work() {
  const unit_convert = get_unit_convert();
  $("input[name=xwork]").val(clip(450 * unit_convert));
  $("input[name=ywork]").val(clip(330 * unit_convert));
  $("input[name=zwork]").val(clip(81 * unit_convert));
  from_working();
}

function from_working() {
  var offsets = get_offsets();

  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var zwork = parseFloat($("input[name=zwork]").val());

  var xrails = xwork + offsets.xrail_minus_work;
  var xgantryrail = xwork + offsets.xgantryrail_minus_work;
  var yrails = ywork + offsets.yrail_minus_work;
  var ygantryrail = ywork + offsets.ygantryrail_minus_work;
  var zrails = zwork + offsets.zrail_minus_work;
  var zlegs = zwork + offsets.zleg_minus_work;
  var rail_total = xrails*2 + xgantryrail + yrails*2 + ygantryrail + zrails*2 + zlegs*4 + 12*offsets.kerf;
  var leadscrew = zwork + offsets.zleadscrew_minus_work;
  var xbelts = xrails + offsets.xbelt_minus_rail;
  var ybelts = yrails + offsets.ybelt_minus_rail;
  var belt_total = 2*xbelts + 2*ybelts;

  var xtable = xrails + offsets.xtable_minus_rail;
  var ytable = yrails + offsets.ytable_minus_rail;
  var xbound = xrails + offsets.xbound_minus_rail;
  var ybound = yrails + offsets.ybound_minus_rail;
  var zbound = zwork + zrails + offsets.zbound_minus_rail_and_work;
  var zbound2 = zrails*2;

  ///$("input[name=xwork]").val(clip(xwork));
  ///$("input[name=ywork]").val(clip(ywork));
  ///$("input[name=zwork]").val(clip(zwork));

  $("span[name=xrails]").text(clip(xrails));
  $("span[name=xgantryrail]").text(clip(xgantryrail));
  $("span[name=yrails]").text(clip(yrails));
  $("span[name=ygantryrail]").text(clip(ygantryrail));
  $("span[name=zrails]").text(clip(zrails));
  $("span[name=zlegs]").text(clip(zlegs));
  $("span[name=rail_total]").text(clip(rail_total));
  $("span[name=leadscrew]").text(clip(leadscrew));
  $("span[name=xbelts]").text(clip(xbelts));
  $("span[name=ybelts]").text(clip(ybelts));
  $("span[name=belt_total]").text(clip(belt_total));

  $("span[name=xtable]").text(clip(xtable));
  $("span[name=ytable]").text(clip(ytable));
  $("span[name=xbound]").text(clip(xbound));
  $("span[name=ybound]").text(clip(ybound));
  $("span[name=zbound]").text(clip(zbound));
  $("span[name=zbound2]").text(clip(zbound2));
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
