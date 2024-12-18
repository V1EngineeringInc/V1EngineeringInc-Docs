// Enum to help keep track of unit systems rather than hard-coded strings throughout the code 
const Units = Object.freeze({
    Metric: "mm",
    Imperial: "inches"
});

// object to hold offsets in a spot that is easy to edit
const offsets = Object.freeze({
    xrail_core: 168,
    yrail_minus_work: 255,
    ytable_minus_work: 313,
    xbelt_extra: 180,
    ybelt_extra: 200,
    xtable_extra: 107.5,
    xrail_cushion: 3
});

// initialize current display unit
var displayUnit = Units.Metric;

// To prevent rounding error creep, we are going to keep the desired size in 
// variables instead of relying on the after-conversion number on display in the textboxes
var xUsable = 1220;
var yUsable = 2440;
var xThickness = 6.35;


/**
 * Update display.
 *
 * This updates the visual components on the page with the correct text, etc. to match the selected unit.
 *
 * @param {Units}  currentUnit   Current Display unit.
 */
function setUnitDisplay(currentUnit) {
    switch (currentUnit) {
        case Units.Metric:
            // Find all the labels and change them to inches
            $(".units").text(Units.Metric);
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
            break;
        case Units.Imperial:
            // Find all the labels and change them to inches
            $(".units").text(Units.Imperial);

            // Set the step attributes (you can also set other attributes here, like min, max, whatever)
            $("input[name=xwork]").attr({
                "step": 0.125
            });
            $("input[name=ywork]").attr({
                "step": 0.125
            });
            $("input[name=xzplate]").attr({
                "step": 0.004
            });
            break;
    }
}

/**
 * Switch to Metric
 *
 * This updates the inputs on the page with the correct text to match the selected unit, and updates the calculator
 * Should be called when the unit selector switches to mm
 */
function to_mm() {
    var isUnitChanging = displayUnit === Units.Imperial;
    displayUnit = Units.Metric;
    setUnitDisplay(displayUnit);

    // Get the current units
    if (isUnitChanging) {
        // Change the units.
        // If we are changing from inches, round up to the next highest mm to keep display clean
        // Underlying values remain the same to preserve calculation and prevent rounding error creep when switching back and forth
        $("input[name=xwork]").val(Math.ceil(xUsable));
        $("input[name=ywork]").val(Math.ceil(yUsable));

        // XZ plate thickness might require a little more accuracy so just display to 2 decimal places. This is more likely a mcahined part
        // than wood being cut with simple tools
        $("input[name=xzplate]").val(parseFloat(xThickness.toFixed(2)));
    }

    // Recalculate the rest of the page.
    calculate();
}

/**
 * Switch to Imperial
 *
 * This updates the inputs on the page with the correct text to match the selected unit, and updates the calculator
 * Should be called when the unit selector switches to inches
 */
function to_inch() {
    var isUnitChanging = displayUnit === Units.Metric;
    displayUnit = Units.Imperial;
    setUnitDisplay(displayUnit);

    if (isUnitChanging) {
        // Change the units.
        $("input[name=xwork]").val(roundToNearest(xUsable / 25.4));
        $("input[name=ywork]").val(roundToNearest(yUsable / 25.4));

        // XZ plate thickness might require a little more accuracy so just display to 3 decimal places. This is more likely a mcahined part
        // than wood being cut with simple tools
        $("input[name=xzplate]").val(parseFloat((xThickness / 25.4).toFixed(3)));
    }

    // Recalculate the rest of the page.
    calculate();
}

/**
 * Round Up To Nearest 1/8".
 *
 * Round up the supplied value to the next nearest 1/8" increment. This only affects Imperial measurements as metric values
 * should already be rounded to the nearest whole number.
 *
 * @param {number}  value   value to be rounded.
 */
function roundUpToNearest(value) {
    return Math.ceil(value * 8) / 8; // Round to .125
}

/**
 * Round To Nearest 1/8".
 *
 * Round up the supplied value to the next nearest 1/8" increment. This only affects Imperial measurements as metric values
 * should already be rounded to the nearest whole number.
 *
 * @param {number}  value   value to be rounded.
 */
function roundToNearest(value) {
    return Math.round(value * 8) / 8; // Round to .125
}

/**
 * Reset Workspace
 *
 * Resets inputs back to initial values. Retains selected unit system
 */
function reset_work() {
    xUsable = 1220;
    yUsable = 2440;
    xThickness = 6.35;

    switch (displayUnit) {
        case Units.Metric:
            $("input[name=xwork]").val(xUsable);
            $("input[name=ywork]").val(yUsable);
            $("input[name=xzplate]").val(xThickness);
            break;
        case Units.Imperial:
            $("input[name=xwork]").val(roundToNearest(xUsable / 25.4));
            $("input[name=ywork]").val(roundToNearest(yUsable / 25.4));
    
            // XZ plate thickness might require a little more accuracy so just display to 3 decimal places. This is more likely a mcahined part
            // than wood being cut with simple tools
            $("input[name=xzplate]").val(parseFloat((xThickness / 25.4).toFixed(3)));
            break;
    }

    calculate();
}

/**
 * X Usable Cutting Area changed
 *
 * Update calculator when X Usable changes. Should be called when the X Usable value is changed in the interface.
 */
function xwork_changed() {
    var xwork = parseFloat($("input[name=xwork]").val());
    if (!isNaN(xwork)) {
        switch (displayUnit) {
            case Units.Metric:
                xUsable = xwork;
                break;
            case Units.Imperial:
                xUsable = xwork * 25.4;
                break;
        }

        calculate();
    }
}

/**
 * Y Usable Cutting Area changed
 *
 * Update calculator when Y Usable changes. Should be called when the Y Usable value is changed in the interface.
 */
function ywork_changed() {
    var ywork = parseFloat($("input[name=ywork]").val());
    if (!isNaN(ywork)) {
        switch (displayUnit) {
            case Units.Metric:
                yUsable = ywork;
                break;
            case Units.Imperial:
                yUsable = ywork * 25.4;
                break;
        }

        calculate();
    }
}

/**
 * XZ Plate Thickness changed
 *
 * Update calculator when XZ Plate changes. Should be called when the XZ Plate Thickness value is changed in the interface.
 */
function xthickness_changed() {
    var xzthick = parseFloat($("input[name=xzplate]").val());
    if (!isNaN(xzthick)) {
        switch (displayUnit) {
            case Units.Metric:
                xThickness = xzthick;
                break;
            case Units.Imperial:
                xThickness = xzthick * 25.4;
                break;
        }

        calculate();
    }
}

/**
 * Convert to Display Units.
 *
 * Convert the supplied value to display units. Currently only affects Imperial display unit, as all values are held in memory in Metric
 *
 * @param {number}  value   value to be rounded.
 */
function convertToDisplayUnits(val) {
    if (displayUnit === Units.Imperial)
        return val / 25.4;
    else
        return val;
}

/**
 * Update Calculated values.
 *
 * Take the values in memory and update the calculator section of the page with calculated values in the correct display unit
 */
function calculate() {
    // Calculate strut plate width first, then use the strut plate dimension to calculate other values
    // since this value will be rounded up to the next mm
    var xstrut = Math.ceil(xUsable + offsets.xrail_core);
    var xbelts = xstrut + offsets.xbelt_extra;
    var xtable = xstrut + 2 * xThickness + offsets.xtable_extra;

    var yrail = yUsable + offsets.yrail_minus_work;
    var ybelts = yrail + offsets.ybelt_extra;
    var ytable = yUsable + offsets.ytable_minus_work;

    var belt_total = 1 * xbelts + 2 * ybelts;

    // handle the xrail special case where we want a little cushion to makes sure the plates don't kick out
    // we do this calculation in display units to make sure rounding errors don't cause us to be 0 or 2 increments off
    var convertedXStrut = roundUpToNearest(convertToDisplayUnits(xstrut));
    var xrails = convertedXStrut - roundUpToNearest(convertToDisplayUnits(offsets.xrail_cushion));

    $("span[name=strut]").text(convertedXStrut);
    $("span[name=xrails]").text(xrails);
    $("span[name=yrail]").text(roundUpToNearest(convertToDisplayUnits(yrail)));
    $("span[name=xbelts]").text(roundUpToNearest(convertToDisplayUnits(xbelts)));
    $("span[name=ybelts]").text(roundUpToNearest(convertToDisplayUnits(ybelts)));
    $("span[name=belt_total]").text(roundUpToNearest(convertToDisplayUnits(belt_total)));
    $("span[name=xtable]").text(roundUpToNearest(convertToDisplayUnits(xtable)));
    $("span[name=ytable]").text(roundUpToNearest(convertToDisplayUnits(ytable)));
}

// Set these up the first time.
$(window).on('load', function () {
    // Get back to mm
    $("input[value=mm]").prop('checked', true);
    $("input[value=inches]").prop('checked', false);

    to_mm();

    reset_work();
});