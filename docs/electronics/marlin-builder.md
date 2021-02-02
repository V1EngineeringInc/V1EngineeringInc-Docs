<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>

# Marlin Firmware

## V1CNC (MPCNC or Low Rider CNC) Configurations

### Ultimachine

<div name="v1cnc-ultimachine"></div>

### Skr Pro Configurations

<div name="v1cnc-skr"></div>

### Other Configurations

<div name="v1cnc-other"></div>

## MP3DP (3D Printer, not MPCNC) Configurations

### Ultimachine

<div name="v13dp-ultimachine"></div>

### Skr Pro Configurations

<div name="v13dp-skr"></div>

### Other Configurations

<div name="v13dp-other"></div>

## ZenXY Configurations

### Ultimachine

<div name="v1zxy-ultimachine"></div>

### Skr Pro Configurations

<div name="v1zxy-skr"></div>

### Other Configurations

<div name="v1zxy-other"></div>

## Levels of Testing

### V1Engineering Tested Configurations

!!! success "Officially Supported Firmware Configurations"
    These options are tested at V1Engineering.

### Community Tested Configurations

!!! note "Community Teseted Firmware Configurations"
    These options are not tested at V1Engineering, but community members in the
    [forums](https://forums.v1engineering.com) have tested them and report that they work.

### Untested Configurations

!!! warning "Not Tested Firmware Configurations"
    These options are not tested. Let us know if they work for you in the [forums](https://forums.v1engineering.com).

    Use at your own risk.

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
  table += "<thead> <tr> <th>Config</th> <th>Version</th> <th>Support</th> </tr> </thead>"
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
  'V1CNC_MiniRambo',
  'V1CNC_Rambo',
  'V1CNC_Rambo_Dual',
  'V1CNC_SkrPro_2209',
  'V1CNC_SkrPro_Dual_2209',
]

const community_configs = [
  'V13DP_MiniRambo',
  'V1CNC_Ramps',
  'V1CNC_SkrPro_DualLR_2209',
  'V1ZXY_MiniRambo',
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
      const zipName = /[_a-zA-Z-.0-9]*-src\.zip/.exec(url)
      
      // If you want to edit this, try using this online regex editor: https://regex101.com/r/K2eUnz/1
      // This grabs the whole thing again, but this time, group 1 is the config name and group 2 is the marlin version.
      const zipParts = /([_a-zA-Z.0-9]*)-([_a-zA-Z.0-9]*)-src\.zip/.exec(zipName)
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
      } else if ("V13DP" === machineType) {
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



