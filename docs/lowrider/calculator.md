<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# LowRider v4 Size Calculator

<div class="inline end" style="width: 500px">
   <img src="/../../img/lr4/lr4_simple.jpg" style="width: 500px">
</div>
## Inputs

#### Units
<input type="radio" onchange="to_mm()" name="units" value="mm" checked>Millimeter (mm)<br/>
<input type="radio" onchange="to_inch()" name="units" value="inches">Inch<br/>

#### Usable Cutting Area
<!-- These "value"s are going to be overwritten by the reset_work() function below. -->
<input class="calc" type="number" onkeyup="from_working()" name="xwork" value="1220" size="6"><span class="units">mm</span> X<br/>
<input class="calc" type="number" onkeyup="from_working()" name="ywork" value="2440" size="6"><span class="units">mm</span> Y<br/>

#### XZ Plate Thickness
Shop Aluminum plates are 6.5mm (0.256").

<input class="calc" type="number" onkeyup="from_working()" name="xzplate" value="6.5" size="6"><span class="units">mm</span> XZ Plate<br/>

<p><a  class="btn btn-default" href="javascript:reset_work()">Reset</a></p>

----

## Size Calculator

#### Rail Lengths
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="xrails"     ></span>|2|X Rails|
|<span name="yrail"     ></span>|1|Y Rail|

#### Belt Dimensions
|Length (<span class="units">mm</span>)| Qty | Name |
|--------------------------------------|-----|------|
|<span name="xbelts"    ></span>|1|Belt length along X|
|<span name="ybelts"    ></span>|2|Belt length along Y|
|<span name="belt_total"></span>|**total length**| belts (all 3)|

#### Strut Plates
|Length (<span class="units">mm</span>)|Qty|Name|
|-------------------------------------|---|----|
|<span name="strut"     ></span>|2|Strut length|


#### Table Size

This output is the minimum table required. An extra 25-50mm (1"-2") or more on each dimension is nice if 
you will be pushing it up against a wall or in a corner.

|Length (<span class="units">mm</span>)| Name |
|--------------------------------------|------|
|<span name="xtable"></span>|X table size (width)|
|<span name="ytable"></span>|Y table size (length)|

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

  var v4 = {};
  v4.xrail_core = 169 * unit_convert;
  v4.yrail_minus_work = 255 * unit_convert;
  v4.ytable_minus_work = 313 * unit_convert;
  v4.xbelt_extra = 180 * unit_convert;
  v4.ybelt_extra = 200 * unit_convert;
  v4.xtable_extra = 110 * unit_convert;
  v4.xrail_2mm = 2 * unit_convert;
  
  return v4;
}

function to_mm() {
  // Query whether unit type is changing
  var isUnitChanging = false;
  if ($(".units").first().text() != "mm") {
    isUnitChanging = true;
  }

  // Find all the labels and change them to mm
  $(".units").text("mm");

  // Set the step attributes (you can also set other attributes here, like min, max, whatever)
  $("input[name=xwork]").attr({
    "step": 10.0
  });
  $("input[name=ywork]").attr({
    "step": 10.0
  });
  $("input[name=xzplate]").attr({
    "step": 0.1  
  });

  // Get the current units
  if (isUnitChanging) {
    // Get the current values.
    var xwork = parseFloat($("input[name=xwork]").val());
    var ywork = parseFloat($("input[name=ywork]").val());
    var xzplate = parseFloat($("input[name=xzplate]").val());

    // Change the units.
    // This Math.round(... * 10.0) / 10.0 is to round to the step.
    $("input[name=xwork]").val(Math.round(xwork * 25.4 * 0.1) / 0.1);
    $("input[name=ywork]").val(Math.round(ywork * 25.4 * 0.1) / 0.1);
    $("input[name=xzplate]").val(Math.round(xzplate * 25.4));
  }
  
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
  $("input[name=xzplate]").attr({
    "step": 0.004
  });

  // Get the current values.
  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var xzplate = parseFloat($("input[name=xzplate]").val());

  // Change the units.
  $("input[name=xwork]").val(clip(xwork / 25.4));
  $("input[name=ywork]").val(clip(ywork / 25.4));
  $("input[name=xzplate]").val(clip(xzplate / 25.4));

  // Recalculate the rest of the page.
  from_working();
}

function clip(value) {
  return Math.round(value * 8) / 8; // Round to .125
}

function convertToMetric(num) {
  var units = $("input[name=units]:checked").val();
  return (units == "mm") ? num : Math.floor(num * 25.4);
}

function reset_work() {
  const unit_convert = get_unit_convert();
  $("input[name=xwork]").val(clip(1220 * unit_convert));
  $("input[name=ywork]").val(clip(2440 * unit_convert));
  $("input[name=xzplate]").val(clip(6.35 * unit_convert));
  from_working();
}


function from_working() {
  var offsets = get_offsets();

  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var xzplate = parseFloat($("input[name=xzplate]").val());

  var xrails = xwork + offsets.xrail_core - offsets.xrail_2mm;
  var yrail = ywork + offsets.yrail_minus_work;
   var xstrut = xwork + offsets.xrail_core;

  var xbelts = xwork + offsets.xrail_core + offsets.xbelt_extra;
  var ybelts = yrail + offsets.ybelt_extra;
  var belt_total = 1*xbelts + 2*ybelts;

  var xtable = xwork + offsets.xrail_core + 2*xzplate + offsets.xtable_extra;
  var ytable = ywork + offsets.ytable_minus_work;

  $("span[name=xrails]").text(clip(xrails));
  $("span[name=yrail]").text(clip(yrail));
  $("span[name=xbelts]").text(clip(xbelts));
  $("span[name=ybelts]").text(clip(ybelts));
  $("span[name=belt_total]").text(clip(belt_total));
  $("span[name=xzplate]").text(clip(xzplate));
  $("span[name=xtable]").text(clip(xtable));
  $("span[name=ytable]").text(clip(ytable));
  $("span[name=strut]").text(clip(xstrut));
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
