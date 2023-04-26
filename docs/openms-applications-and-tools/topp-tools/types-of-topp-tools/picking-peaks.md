---
orphan: true
---
Picking Peaks
============

For low resolution data, consider to smooth the data first ([Smoothing raw data](../../../topp-command-line-tools/smoothing-raw-data.md)) and subtract
the baseline ([Subtracting a baseline from a spectrum](../../../topp-command-line-tools/subtracting-a-baseline-from-a-spectrum.md)) before peak picking.

There are two types of PeakPickers: the **PeakPickerWavelet** and one especially suited for high resolution data (**PeakPickerHiRes**). This tutorial explains the PeakPickerWavelet. Use the file `peakpicker_tutorial_2.mzML` from the examples data (select **File** > **Open example data**).

The main parameters are the peak width and the minimal signal to noise ratio for a peak to be picked. If you don't know
the approximate `fwhm` of peaks, use the estimation included in the PeakPickerWavelet, set the flag `estimate_peak_width`
to `true`. After applying the PeakPickerWavelet, observe which peak width was estimated and used for peak picking in the
log window.

To estimate the peak width, use the measuring tool <a href="../../visualize-with-openms/display-modes-and-view-options.html">Action Modes and Their Uses</a> to determine
the fwhm of one or several representative peaks.

If the peak picker delivers only a few peaks even though the `peak_with` and `signal_to_noise` parameters are set to
good values, consider changing the advanced parameter `fwhm_lower_bound_factor` to a lower value. All peaks with a lower
`fwhm` than `fwhm_lower_bound_factor` \* `peak_width` are discarded.

The following image shows a part of the spectrum with the picked peaks shown in green, the estimated peak width in the
log window and the measured peak width.

![TOPPView tools pp\_picked](/images/tutorials/topp/TOPPView_tools_pp_picked.png)
