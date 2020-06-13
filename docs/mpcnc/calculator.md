<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# MPCNC Size Calculator

## Model:

<input type="radio" name="model" value="Primo"> Primo<br>

<input type="radio" name="model" value="Burly" checked> Burly<br>

## Tool:

Larger tools may collide with the side rails and contstrain movement
before the MPCNC reaches its full range of motion in x and y.
Select your intended tool to account for this difference:

<input type="radio" name="tool" value="Pen" checked> Full range of motion

<input type="radio" name="tool" value="DW660"> Dewalt DW660

<input type="radio" name="tool" value="Makita"> Makita

## Working space

<input type="text" name="xwork" value="300", size="4"> mm x

<input type="text" name="ywork" value="400", size="4"> mm y

<input type="text" name="zwork" value="75", size="4"> mm z

<button class="calculator-button" onclick="from_working()">Calculate tube lengths<br>and bounding box from<br>working space</button>

## Tube lengths

<input type="text" name="xrails" value="", size="4"> mm x rails, side and gantry (total 3 needed)

<input type="text" name="yrails" value="", size="4"> mm y rails, side and gantry (total 3 needed)

<input type="text" name="zrails" value="", size="4"> mm z rails (2 needed)

<input type="text" name="zlegs" value="", size="4" readonly> mm legs (4 needed)

<input type="text" name="railtotal" value="", size="4" readonly> mm total needed assuming 3mm kerf

<button class="calculator-button" onclick="from_tubes()">Calculate working space<br>and bounding box from<br>tube lengths</button>

## Bounding box

<input type="text" name="xbound" value="", size="4"> mm x

<input type="text" name="ybound" value="", size="4"> mm y

<input type="text" name="zbound" value="", size="4"> mm z

<input type="text" name="zbound2" value="", size="4" readonly> mm clearance to remove z axis

<button class="calculator-button" onclick="from_bbox()">Calculate working space<br>and tube lengths from<br>bounding box</button>

<script>

function get_offsets() {
  var burly = {};
  burly.xrail_minus_work = 264;
  burly.yrail_minus_work = 264;
  burly.zrail_minus_work = 190;
  burly.zleg_minus_work = -13;
  burly.xbound_minus_rail = 20;
  burly.ybound_minus_rail = 20;
  burly.zbound_minus_rail_and_work = 50;

  var primo = {};
  primo.xrail_minus_work = 310;
  primo.yrail_minus_work = 320;
  primo.zrail_minus_work = 350;
  primo.zleg_minus_work = -13;
  primo.xbound_minus_rail = 20;
  primo.ybound_minus_rail = 20;
  primo.zbound_minus_rail_and_work = 50;

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
  var yrails = ywork + offsets.yrail_minus_work;
  var zrails = zwork + offsets.zrail_minus_work;
  var zlegs = zwork + offsets.zleg_minus_work;
  var kerf = 3;
  var railtotal = xrails*3 + yrails*3 + zrails*2 + zlegs*4 + 11*kerf;
  
  var xbound = xrails + offsets.xbound_minus_rail;
  var ybound = yrails + offsets.ybound_minus_rail;
  var zbound = zrails + zwork + offsets.zbound_minus_rail_and_work;
  var zbound2 = zrails*2;
  
  $("input[name=xrails]").val(xrails);
  $("input[name=yrails]").val(yrails);
  $("input[name=zrails]").val(zrails);
  $("input[name=zlegs]").val(zlegs);
  $("input[name=railtotal]").val(railtotal);
  
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
  var railtotal = xrails*3 + yrails*3 + zrails*2 + zlegs*4 + 11*kerf;

  var xbound = xrails + offsets.xbound_minus_rail;
  var ybound = yrails + offsets.ybound_minus_rail;
  var zbound = zrails + zwork + offsets.zbound_minus_rail_and_work;
  var zbound2 = zrails*2;
  
  $("input[name=zlegs]").val(zlegs);
  $("input[name=railtotal]").val(railtotal);
  
  $("input[name=xwork]").val(xwork);
  $("input[name=ywork]").val(ywork);
  $("input[name=zwork]").val(zwork);

  $("input[name=xbound]").val(xbound);
  $("input[name=ybound]").val(ybound);
  $("input[name=zbound]").val(zbound);
  $("input[name=zbound2]").val(zbound2);  
}


function from_bbox() {
  var offsets = get_offsets();
  alert("not yet implemented");
}

from_working();
</script>
</body>
</html>
