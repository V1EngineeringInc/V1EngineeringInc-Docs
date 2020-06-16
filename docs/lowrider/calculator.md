<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# Low Rider Size Calculator
----
## Inputs

#### Units
<input type="radio" onchange="to_mm()" name="units" value="mm" checked>Metric (mm)<br/>
<input type="radio" onchange="to_inch()" name="units" value="inches">Imperial (inch)<br/>

#### Model
<input type="radio" onchange="from_working()" name="model" value="v2" checked> Low Rider v2<br/>
<input type="radio" onchange="from_working()" name="model" value="old"> Old Version<br/>

----

## Size Calculator

#### Workspace
<!-- These "value"s are going to be overwritten by the reset_work() function below. -->
<input class="calc" type="number" onchange="from_working()" name="xwork" value="1220" size="6"><span class="units">mm</span> x<br/>
<input class="calc" type="number" onchange="from_working()" name="ywork" value="2440" size="6"><span class="units">mm</span> y<br/>
<input class="calc" type="number" onchange="from_working()" name="zwork" value="89" size="6"><span class="units">mm</span> z<br/>
<button class="reset" onclick="reset_work()">Reset</button>

#### Tube Lengths
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="xrails"     ></span>|2|x rails|
|<span name="zrails"     ></span>|4|z rails|
|<span name="rail_total" ></span>|**total needed**| total tube length assuming 3mm kerf|

#### Material Dimensions
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="leadscrew" ></span>|2|leadscrew length (minimum)|
|<span name="xbelts"    ></span>|1|belt length along x|
|<span name="ybelts"    ></span>|2|belt length along y|
|<span name="belt_total"></span>|**total length**| belts (all 4)|

#### Table Size
|Length (<span class="units">mm</span>)| Name |
|--------------------------------------|------|
|<span name="xtable"></span>|x table size (width)|
|<span name="ytable"></span>|y table size (length)|

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

  var old = {};
  old.xrail_minus_work = 317.0 * unit_convert;
  old.zrail_minus_work = 210 * unit_convert;
  old.xtable_minus_work = 247.5 * unit_convert;
  old.ytable_minus_work = 371 * unit_convert;
  old.zleadscrew_minus_work = 161.0 * unit_convert;
  old.xbelt_minus_rail = 69.4 * unit_convert; // This seems wrong. It shouldn't be less than the rail, should it?
  old.ybelt_minus_rail = 470 * unit_convert;
  old.kerf = 3 * unit_convert;

  var v2 = {};
  v2.xrail_minus_work = 276.6 * unit_convert;
  v2.zrail_minus_work = 216 * unit_convert;
  v2.xtable_minus_work = 203.2 * unit_convert;
  v2.ytable_minus_work = 381 * unit_convert;
  v2.zleadscrew_minus_work = 57.15 * unit_convert;
  v2.xbelt_minus_rail = 300 * unit_convert;
  v2.ybelt_minus_rail = 420 * unit_convert;
  v2.kerf = 3 * unit_convert;

  var model = $("input[name=model]:checked").val();
  if (model == "v2") {
    return v2;
  }
  else if (model == "old") {
    return old;
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
  $("input[name=xwork]").val(clip(1220 * unit_convert));
  $("input[name=ywork]").val(clip(2440 * unit_convert));
  $("input[name=zwork]").val(clip(89 * unit_convert));
  from_working();
}

function from_working() {
  var offsets = get_offsets();

  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var zwork = parseFloat($("input[name=zwork]").val());

  var xrails = xwork + offsets.xrail_minus_work;
  var zrails = zwork + offsets.zrail_minus_work;
  var rail_total = xrails*2 + zrails*4 + 6*offsets.kerf;

  var leadscrew = zwork + offsets.zleadscrew_minus_work;
  var xbelts = xwork + offsets.xbelt_minus_rail;
  var ybelts = ywork + offsets.ybelt_minus_rail;
  var belt_total = 1*xbelts + 2*ybelts;

  var xtable = xwork + offsets.xtable_minus_work;
  var ytable = ywork + offsets.ytable_minus_work;

  ///$("input[name=xwork]").val(clip(xwork));
  ///$("input[name=ywork]").val(clip(ywork));
  ///$("input[name=zwork]").val(clip(zwork));

  $("span[name=xrails]").text(clip(xrails));
  $("span[name=zrails]").text(clip(zrails));
  $("span[name=rail_total]").text(clip(rail_total));
  $("span[name=leadscrew]").text(clip(leadscrew));
  $("span[name=xbelts]").text(clip(xbelts));
  $("span[name=ybelts]").text(clip(ybelts));
  $("span[name=belt_total]").text(clip(belt_total));

  $("span[name=xtable]").text(clip(xtable));
  $("span[name=ytable]").text(clip(ytable));
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
