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
<input class="calc" type="number" oninput="xwork_changed()" name="xwork" value="1220" size="6"><span class="units">mm</span> X<br/>
<input class="calc" type="number" oninput="ywork_changed()" name="ywork" value="2440" size="6"><span class="units">mm</span> Y<br/>

#### XZ Plate Thickness
Shop Aluminum plates are 6.35mm (0.25").

<input class="calc" type="number" oninput="xthickness_changed()" name="xzplate" value="6.35" size="6"><span class="units">mm</span> XZ Plate<br/>

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

<script src="../calculator.js">
  
</script>
