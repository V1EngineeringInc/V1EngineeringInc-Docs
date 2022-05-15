<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# Marlin Firmware

This is where you can download the latest configured Marlin Firmware for your V1Engineering machines.
Release notes and details are [in github](https://github.com/V1EngineeringInc/MarlinBuilder/releases)

After downloading the right firmware below, you can flash it to your controller ([Rambo, Mini-Rambo,
Ramps](xloader.md), or [Skr](skrpro.md#firmware)). Or compile and flash using
[platformio](../learn/platformio.md) or [arduino](arduino.md).

## Levels of Testing

Not all of these configurations go through the same rigor before being released. There are just too
many to test, but that doesn't mean we shouldn't share what *should* work. These levels give you a
rough idea of which configurations have the most users and the most testing.

### V1Engineering Tested Configurations

!!! success "Officially Tested Firmware Configurations"
    These options are tested at V1Engineering.

### Community Tested Configurations

!!! note "Community Teseted Firmware Configurations"
    These options are not tested at V1Engineering, but community members in the
    [forums](https://forums.v1engineering.com) have tested them and report that they work.

### Untested Configurations

!!! warning "Not Tested Firmware Configurations"
    These options are not tested. Let us know if they work for you in the [forums](https://forums.v1engineering.com).

    Use at your own risk.

## V1CNC (MPCNC or Low Rider CNC) Configurations

![!MPCNC Render](https://www.v1engineering.com/wp-content/uploads/2020/06/Primo-scaled.jpg){: loading=lazy width="450"}

![!lowrider](https://www.v1engineering.com/wp-content/uploads/2018/07/LowRider2-CNC-Render.jpg){: loading=lazy width="450"}

### Ultimachine

<div name="v1cnc-ultimachine"></div>

### Skr Pro Configurations

<div name="v1cnc-skr"></div>

### Other Configurations

<div name="v1cnc-other"></div>

## MP3DP (3D Printer, not MPCNC) Configurations

![!mp3dp](https://www.v1engineering.com/wp-content/uploads/2018/01/MVIMG_20180111_1403212.jpg){: loading=lazy width="450"}

### Ultimachine

<div name="v13dp-ultimachine"></div>

### Skr Pro Configurations

<div name="v13dp-skr"></div>

### Other Configurations

<div name="v13dp-other"></div>

## ZenXY Configurations

![!FirstZenXY](https://www.v1engineering.com/wp-content/uploads/2021/03/XZXY-V2F-squarer.jpg){: loading=lazy width="450"}

### Ultimachine

<div name="v1zxy-ultimachine"></div>

### Skr Pro Configurations

<div name="v1zxy-skr"></div>

### Other Configurations

<div name="v1zxy-other"></div>

## Decoding the Config Names

### Machine Type

V1CNC
:   These are created for the CNC machines designed at V1Engineering. This includes the
[MPCNC](../mpcnc/intro.md) and the [Low Rider CNC](../lowrider/index.md).

V13DP
:   V1 3D Printer. This is for the [MP3DP](../mp3dp/index.md).

V1ZXY
:   V1 Zen XY Sand Machine. This is for the [ZenXY](../zenxy/index.md), a corexy machine for 2D drawings in the sand.

### Board Type

Rambo
:   The [Ultimachine Rambo](ultimachine.md#rambo-13-14) board. For purchase in the [Shop](https://shop.v1engineering.com/collections/parts/products/rambo-v1-3l).

Mini-Rambo
:   The [Ultimachine Mini-Rambo](ultimachine.md#mini-rambo) board. For purchase in the [Shop](https://vicious1-com.myshopify.com/products/mini-rambo-1-3).

Archim1, Archim2
:   The [Ultimachine Archim 1 or Archim 2](ultimachine.md#archim). For purchase in the [Shop](https://vicious1-com.myshopify.com/collections/miscellaneous/products/archim-1-0a).

SkrPro
:   The [BigTreeTech Skr Pro v1.2](skrpro.md) (or v1.1), with 6 drivers. For purchase in the
[Shop](https://shop.v1engineering.com/collections/parts/products/skr-pro1-2-6x-2209-drivers-tft35-e3-v3)
This does not work for the Skr Turbo, Skr mini, or the Skr 1.3/1.4 (without the pro, turbo, or mini
name).

Skr1p3
:   The BigTreeTech Skr v1.3 or Skr v1.4. These boards are smaller than the Skr Pro, and has 5 drivers, not 6.

SkrTurbo
:   The BigTreeTech Skr Turbo v1.4.

Ramps
:   The good old [Ramps](ramps.md) board.

### Dual or Series stepper wiring

Serial
:   Any of the V1CNC configs that don't have `Dual` or `DualLR` in the name are configured for
serial wiring (which works on the MPCNC and the Low Rider). Check out [more information about series stepper wiring](steppers.md)

Dual
:   This indicates a configuration for a Dual Endstop MPCNC. Check out [more information about dual
endstops](dual-endstops.md)

DualLR
:   This indicates a configuration for a Dual Endstop Low Rider. Check out [more information about
dual endstops for Low Rider](dual-lr.md)

### Driver Type

Some boards support more than one kind of driver. These codes indicate which drivers you install into the driver sockets.

8825
:   DRV8825. Made famous by pololu. The a4498 or any 8825 compatible driver (like a TMC driver in
standalone mode) would use this type.

2209
:   TMC2209. These are for the Trinamic TMC 2209 drivers. If you are using another TMC driver in SPI
or UART mode, then you will start with this, and change the driver type.

## Alternatives

Depending on what type of control board you use you might have other firmware options. Many firmware
versions are fairly board specific though. There could be a long list here, instead may we suggest
having a look in the forums to see what others have tried out and if it might be a better option for
your specific use case.

<script>

function build_tablerow( configInfo, version ) {
  let row = "<tr>"
  row += "<td><a href='" + configInfo[0] + "'>" + configInfo[1] + "</a></td>"
  row += "<td>" + configInfo[2] + " / " + version + "</td>"
 
  let supportLink = "untested-configurations"
  if (configInfo[3] === "V1Engineering") {
    supportLink = "v1engineering-tested-configurations"
  } else if (configInfo[3] === "community") {
    supportLink = "community-tested-configurations"
  }
  row += "<td><a href='#" + supportLink + "'>" + configInfo[3] + "</a></td>"
  row += "</tr>"
  return row
}

function build_table(entries, version) {

  let table = "<table>"
  table += "<thead> <tr> <th>Config</th> <th>Version</th> <th>Testing</th> </tr> </thead>"
  table += "<tbody>"

  // Build the table row in order of support type.
  $.each(entries, function(i, configInfo) {
    if (configInfo[3] === "V1Engineering") {
      table += build_tablerow(configInfo, version)
    }
  })
  
  $.each(entries, function(i, configInfo) {
    if (configInfo[3] === "community") {
      table += build_tablerow(configInfo, version)
    }
  })
  
  $.each(entries, function(i, configInfo) {
    if (configInfo[3] === "untested") {
      table += build_tablerow(configInfo, version)
    }
  })
  
  table += "</tbody>"
  
  return table
}

// These are the key parts where we define which configs we support in each category.
// Stuff that isn't in these two lists are untested.
const v1engineering_configs = [
  'V13DP_MiniRambo',
  'V1CNC_MiniRambo',
  'V1CNC_Rambo',
  'V1CNC_Rambo_Dual',
  'V1CNC_SkrPro_2209',
  'V1CNC_SkrPro_Dual_2209',
  'V1ZXY_MiniRambo',
]

const community_configs = [
  'V1CNC_Ramps',
  'V1CNC_Rambo_DualLR',
  'V1CNC_SkrPro_DualLR_2209',
  'V1ZXY_Rambo',
]

function update_links() {

  $.getJSON("https://api.github.com/repos/V1EngineeringInc/MarlinBuilder/releases/latest", function(result, status){
 
    let version = "Error"

    v1cnc_ultimachine = []
    v1cnc_skr = []
    v1cnc_other = []
    
    v13dp_ultimachine = []
    v13dp_skr = []
    v13dp_other = []
    
    v1zxy_ultimachine = []
    v1zxy_skr = []
    v1zxy_other = []
    
    $.each(result["assets"], function(i, field){
    
      // This looks something like this: 'https://github.com/V1EngineeringInc/MarlinBuilder/releases/download/509/V1CNC_Rambo_DualLR-2.0.7.2-src.zip'
      const url = field.browser_download_url
      
      // This is the release folder name '509'
      version = /\/([v0-9]+)\//.exec(url)[1]
     
      // This is the zip name 'V1CNC_Rambo_DualLR-2.0.7.2-src.zip'
      const zipName = /[_a-zA-Z-.0-9]*[-src]*\.zip/.exec(url)
      
      // If you want to edit this, try using this online regex editor: https://regex101.com/r/K2eUnz/1
      // This grabs the whole thing again, but this time, group 1 is the config name and group 2 is the marlin version.
      const zipParts = /([_a-zA-Z.0-9]*)-([_a-zA-Z.0-9]*)[-src]*\.zip/.exec(zipName)
      const configType = zipParts[1]
      const marlinVersion = zipParts[2]
      
      // Machine type is like 'V1CNC'
      const machineType = /[A-Z0-9]+/.exec(configType)[0]
     
      let supportType = "untested"
      if (v1engineering_configs.indexOf(configType) > -1) {
        supportType = "V1Engineering"
      } else if (community_configs.indexOf(configType) > -1) {
        supportType = "community"
      }
      
      if ("V1CNC" === machineType) {
        if (/Rambo/.test(configType)) {
          v1cnc_ultimachine.push([url, configType, marlinVersion, supportType])
        } else if (/SkrPro/.test(configType)) {
          v1cnc_skr.push([url, configType, marlinVersion, supportType])
        } else {
          v1cnc_other.push([url, configType, marlinVersion, supportType])
        }
      } else if (("V13DP" === machineType) || ("V13RP" === machineType)) {
        if (/Rambo/.test(configType)) {
          v13dp_ultimachine.push([url, configType, marlinVersion, supportType])
        } else if (/SkrPro/.test(configType)) {
          v13dp_skr.push([url, configType, marlinVersion, supportType])
        } else {
          v13dp_other.push([url, configType, marlinVersion, supportType])
        }
      } else if ("V1ZXY" === machineType) {
        if (/Rambo/.test(configType)) {
          v1zxy_ultimachine.push([url, configType, marlinVersion, supportType])
        } else if (/SkrPro/.test(configType)) {
          v1zxy_skr.push([url, configType, marlinVersion, supportType])
        } else {
          v1zxy_other.push([url, configType, marlinVersion, supportType])
        }
      } else {
        console.log("Unknown machine type")
        console.log(machineType)
      }
      
    });
  
    // Now, actually make the tables
    $("div[name=v1cnc-ultimachine]").append(build_table(v1cnc_ultimachine, version))
    $("div[name=v1cnc-skr]").append(build_table(v1cnc_skr, version))
    $("div[name=v1cnc-other]").append(build_table(v1cnc_other, version))
    $("div[name=v13dp-ultimachine]").append(build_table(v13dp_ultimachine, version))
    $("div[name=v13dp-skr]").append(build_table(v13dp_skr, version))
    $("div[name=v13dp-other]").append(build_table(v13dp_other, version))
    $("div[name=v1zxy-ultimachine]").append(build_table(v1zxy_ultimachine, version))
    $("div[name=v1zxy-skr]").append(build_table(v1zxy_skr, version))
    $("div[name=v1zxy-other]").append(build_table(v1zxy_other, version))
    
  });  
}

// Set these up the first time.
$(window).on('load', function(){
  links = update_links();
});

</script>



