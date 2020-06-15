<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# MPCNC Size Calculator
----
## Inputs

#### Units
<input type="radio" onchange="from_working()" name="units" value="metric" checked> Metric<br/>

#### Model
<input type="radio" onchange="from_working()" name="model" value="Primo"> Primo<br/>
<input type="radio" onchange="from_working()" name="model" value="Burly" checked> Burly<br/>

#### Tool Choice*
<input type="radio" onchange="from_working()" name="tool" value="Pen" checked> Full range of motion (pen, laser, drag knife, etc)<br/>
<input type="radio" onchange="from_working()" name="tool" value="DW660"> Dewalt DW660<br/>
<input type="radio" onchange="from_working()" name="tool" value="Makita"> Makita<br/>

\*\ Larger tools may collide with the side rails and contstrain movement
before the MPCNC reaches its full range of motion in x and y.
Select your intended tool to account for this difference in the following dimensions:

----

## Size Calculator

#### Workspace 
<input class="calc" type="number" step="10" onchange="from_working()" name="xwork" value="300" size="6">mm x<br/>
<input class="calc" type="number" step="10" onchange="from_working()" name="ywork" value="300" size="6">mm y<br/>
<input class="calc" type="number" onchange="from_working()" name="zwork" value="81" size="6">mm z<br/>

#### Tube Lengths
<input class="ro-calc" type="text" onchange="from_tubes()" name="xrails" value="" size="6" readonly>mm x rails, sides (total 2 needed)<br/>
<input class="ro-calc" type="text" onchange="from_tubes()" name="xgantryrail" value="" size="6" readonly>mm x rail, gantry (total 1 needed)<br/>
<input class="ro-calc" type="text" onchange="from_tubes()" name="yrails" value="" size="6" readonly>mm y rails, side and gantry (total 2 needed)<br/>
<input class="ro-calc" type="text" onchange="from_tubes()" name="ygantryrail" value="" size="6" readonly>mm y rail, gantry (total 1 needed)<br/>
<input class="ro-calc" type="text" onchange="from_tubes()" name="zrails" value="" size="6" readonly>mm z rails (2 needed)<br/>
<input class="ro-calc" type="text" onchange="from_tubes()" name="zlegs" value="", size="6" readonly>mm legs (4 needed)<br/>
<input class="ro-calc" type="text" name="rail_total" value="", size="7" readonly>mm **total needed** assuming 3mm kerf<br/>

#### Material Dimensions
<input class="ro-calc" type="text" name="leadscrew" value="", size="6" readonly>mm leadscrew length (minimum)<br/>
<input class="ro-calc" type="text" name="xbelts" value="", size="6" readonly>mm belt length along x (2 needed)<br/>
<input class="ro-calc" type="text" name="ybelts" value="", size="6" readonly>mm belt length along y (2 needed)<br/>
<input class="ro-calc" type="text" name="belt_total" value="", size="6" readonly>mm **Total belt length** (all 4)<br/>

#### Table Size
<input class="ro-calc" type="text" onchange="from_bbox()" name="xtable" value="", size="6" readonly>mm x table size (outer edges of feet)<br/>
<input class="ro-calc" type="text" onchange="from_bbox()" name="ytable" value="", size="6" readonly>mm y table size (outer edges of feet)<br/>



#### Total Machine Footprint
<input class="ro-calc" type="text" name="xbound" value="", size="5" readonly>mm x<br/>
<input class="ro-calc" type="text" name="ybound" value="", size="5" readonly>mm y<br/>
<input class="ro-calc" type="text" onchange="from_bbox()" name="zbound" value="", size="5" readonly>mm z<br/>
<input class="ro-calc" type="text" name="zbound2" value="", size="5" readonly>mm clearance to remove z axis<br/>

<script>


function get_offsets() {
  var burly = {};
  burly.xrail_minus_work = 264;
  burly.xgantryrail_minus_work = 264;
  burly.yrail_minus_work = 264;
  burly.ygantryrail_minus_work = 264;
  burly.zrail_minus_work = 190;
  burly.zleg_minus_work = -13;
  burly.xtable_minus_rail = 20;
  burly.ytable_minus_rail = 20;
  burly.xbound_minus_rail = 30;
  burly.ybound_minus_rail = 30;
  burly.zbound_minus_rail_and_work = 50;
  burly.zleadscrew_minus_work = 76;
  burly.xbelt_minus_rail = 136;
  burly.ybelt_minus_rail = 136;

  var primo = {};
  primo.xrail_minus_work = 304;
  primo.xgantryrail_minus_work = 249;
  primo.yrail_minus_work = 312;
  primo.ygantryrail_minus_work = 257;
  primo.zrail_minus_work = 190;
  primo.zleg_minus_work = -19.5;
  primo.xtable_minus_rail = 34;
  primo.ytable_minus_rail = 34;
  primo.xbound_minus_rail = 68;
  primo.ybound_minus_rail =68;
  primo.zbound_minus_rail_and_work = 50;
  primo.zleadscrew_minus_work = 50;
  primo.xbelt_minus_rail = 50;
  primo.ybelt_minus_rail = 50;

  var tool = $("input[name=tool]:checked").val();
  if (tool == "Pen") {
    // don't clip the working space at all
  }
  else if (tool == "DW660") {
    // working space clipped by this much (not necessarily the same between burly and primo
    burly.xrail_minus_work = burly.xrail_minus_work + 10;
    burly.xgantryrail_minus_work = burly.xgantryrail_minus_work + 10;
    burly.yrail_minus_work = burly.xrail_minus_work + 8;
    burly.zrail_minus_work = burly.zrail_minus_work + 2.75;
    burly.zleg_minus_work = burly.zleg_minus_work + 2.75;

    primo.xrail_minus_work = primo.xrail_minus_work + 9;
    primo.xgantryrail_minus_work = primo.xgantryrail_minus_work + 9;
    primo.yrail_minus_work = primo.yrail_minus_work + 9;
    primo.ygantryrail_minus_work = primo.ygantryrail_minus_work + 9;
    primo.zrail_minus_work = primo.zrail_minus_work + 2.75;
    primo.zleg_minus_work = primo.zleg_minus_work + 2.75;
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


function from_working() {
  var offsets = get_offsets();

  var xwork = parseFloat($("input[name=xwork]").val());
  var ywork = parseFloat($("input[name=ywork]").val());
  var zwork = parseFloat($("input[name=zwork]").val());

  var xrails = xwork + offsets.xrail_minus_work;
  var xgantryrail = xwork + offsets.xgantryrail_minus_work;
  var yrails = ywork + offsets.yrail_minus_work;
  var ygantryrail = xwork + offsets.ygantryrail_minus_work;
  var zrails = zwork + offsets.zrail_minus_work;
  var zlegs = zwork + offsets.zleg_minus_work;
  var kerf = 3;
  var rail_total = xrails*2 + xgantryrail + yrails*2 + ygantryrail + zrails*2 + zlegs*4 + 12*kerf;
  var leadscrew = zwork + offsets.zleadscrew_minus_work;
  var xbelts = xrails + offsets.xbelt_minus_rail;
  var ybelts = yrails + offsets.ybelt_minus_rail;
  var belt_total = 2*xbelts + 2*ybelts;

  var xtable = xrails + offsets.xtable_minus_rail;
  var ytable = yrails + offsets.ytable_minus_rail;
  var xbound = xrails + offsets.xbound_minus_rail;
  var ybound = yrails + offsets.ybound_minus_rail;
  var zbound = zwork + zrails + 50;
  var zbound2 = zrails*2;

  ///$("input[name=xwork]").val(xwork);
  ///$("input[name=ywork]").val(ywork);
  ///$("input[name=zwork]").val(zwork);

  $("input[name=xrails]").val(xrails);
  $("input[name=xgantryrail]").val(xgantryrail);
  $("input[name=yrails]").val(yrails);
  $("input[name=ygantryrail]").val(ygantryrail);
  $("input[name=zrails]").val(zrails);
  $("input[name=zlegs]").val(zlegs);
  $("input[name=rail_total]").val(rail_total);
  $("input[name=leadscrew]").val(leadscrew);
  $("input[name=xbelts]").val(xbelts);
  $("input[name=ybelts]").val(ybelts);
  $("input[name=belt_total]").val(belt_total);

  $("input[name=xtable]").val(xtable);
  $("input[name=ytable]").val(ytable);
  $("input[name=xbound]").val(xbound);
  $("input[name=ybound]").val(ybound);
  $("input[name=zbound]").val(zbound);
  $("input[name=zbound2]").val(zbound2);
}


function from_tubes() {
  var offsets = get_offsets();

  var xrails = parseFloat($("input[name=xrails]").val());
  var yrails = parseFloat($("input[name=yrails]").val());
  var zrails = parseFloat($("input[name=zrails]").val());

  var xwork = xrails-offsets.xrail_minus_work;
  var ywork = yrails-offsets.yrail_minus_work;
  var zwork = zrails-offsets.zrail_minus_work;

  var zlegs = zwork + offsets.zleg_minus_work;
  var kerf = 3;
  var rail_total = xrails*2 + xgantryrail + yrails*2 + ygantryrail + zrails*2 + zlegs*4 + 12*kerf;
  var leadscrew = zwork + offsets.zleadscrew_minus_work;
  var xbelts = xrails + offsets.xbelt_minus_rail;
  var ybelts = yrails + offsets.ybelt_minus_rail;
  var belt_total = 2*xbelts + 2*ybelts;

  var xtable = xrails + offsets.xtable_minus_rail;
  var ytable = yrails + offsets.ytable_minus_rail;
  var xbound = xrails + offsets.xbound_minus_rail;
  var ybound = yrails + offsets.ybound_minus_rail;
  var zbound = (zwork + offsets.zbound_minus_rail_and_work)*2 + 140 + 50;
  var zbound2 = zrails*2 + 50;

  $("input[name=xwork]").val(xwork);
  $("input[name=ywork]").val(ywork);
  $("input[name=zwork]").val(zwork);

  //$("input[name=xrails]").val(xrails);
  //$("input[name=yrails]").val(yrails);
  //$("input[name=zrails]").val(zrails);
  $("input[name=zlegs]").val(zlegs);
  $("input[name=rail_total]").val(rail_total);
  $("input[name=leadscrew]").val(leadscrew);
  $("input[name=xbelts]").val(xbelts);
  $("input[name=ybelts]").val(ybelts);
  $("input[name=belt_total]").val(belt_total);

  $("input[name=xtable]").val(xtable);
  $("input[name=ytable]").val(ytable);
  $("input[name=xbound]").val(xbound);
  $("input[name=ybound]").val(ybound);
  $("input[name=zbound]").val(zbound);
  $("input[name=zbound2]").val(zbound2);
}


function from_bbox() {
  var offsets = get_offsets();

  var xtable = parseFloat($("input[name=xtable]").val());
  var ytable = parseFloat($("input[name=ytable]").val());
  var zbound = parseFloat($("input[name=zbound]").val());

 var yrails = ytable-offsets.ytable_minus_rail;
  var zrail_and_work = zbound-offsets.zbound_minus_rail_and_work;
  var zwork = (zrail_and_work-offsets.zrail_minus_work)/2;
  var zrails = zwork + offsets.zrail_minus_work;

  var xwork = xrails-offsets.xrail_minus_work;
  var ywork = yrails-offsets.yrail_minus_work;

  var zlegs = zwork + offsets.zleg_minus_work;
  var kerf = 3;
  var rail_total = xrails*3 + yrails*3 + zrails*2 + zlegs*4 + 11*kerf;
  var leadscrew = zwork + offsets.zleadscrew_minus_work;
  var xbelts = xrails + offsets.xbelt_minus_rail;
  var ybelts = yrails + offsets.ybelt_minus_rail;
  var belt_total = 2*xbelts + 2*ybelts;

  var xbound = xrails + offsets.xbound_minus_rail;
  var zbound = zrails +  + 50;
  var zbound2 = zrails*2 + 50;

  $("input[name=xwork]").val(xwork);
  $("input[name=ywork]").val(ywork);
  $("input[name=zwork]").val(zwork);

  $("input[name=xrails]").val(xrails);
  $("input[name=yrails]").val(yrails);
  $("input[name=zrails]").val(zrails);
  $("input[name=zlegs]").val(zlegs);
  $("input[name=rail_total]").val(rail_total);
  $("input[name=leadscrew]").val(leadscrew);
  $("input[name=xbelts]").val(xbelts);
  $("input[name=ybelts]").val(ybelts);
  $("input[name=belt_total]").val(belt_total);

  //$("input[name=xtable]").val(xtable);
  //$("input[name=ytable]").val(ytable);
  $("input[name=xbound]").val(xbound);
  $("input[name=ybound]").val(ybound);
  //$("input[name=zbound]").val(zbound);
  $("input[name=zbound2]").val(zbound2);

}

from_working();

</script>
