---
orphan: true
---
OpenMS 2.0 Kernel Whitepaper
===========================

## Introduction

With the constantly increasing amount of data that needs to be handled in computational mass spectrometry we start to
reach the boundary of what is possible given the current design and implementation of the OpenMS kernel. Already in 2012
the OpenMS core team discussed and identified the need for a redesign of the OpenMS kernel with respect to it's scalability
and ease of use. So far, only partial solutions have been proposed that lack the approval of the OpenMS core team as
well as the OpenMS community.

This document summarises the discussion of the OpenMS core team, held at the OpenMS developer retreat in Izmir,
Turkey 2014.

## Detailed problem description

With modern mass spectrometry instruments and measurement techniques the amounts of data that need to be analysed in
computational mass spectrometry reach magnitudes that do not fit into the main memory of neither desktop nor clusters
machines. Therefore the OpenMS kernel has to be redesigned to decouple the algorithms from the actual implementation of
the data structures.

Here we describe the interfaces and concepts we plan to implement for OpenMS 2.0. The OpenMS team has acknowledged the
fact, that this will only be possible in an incremental way, i.e., implementing those interfaces on top of the existing
data structures and then switch the individual classes to the new design, instead of a large redesign in a separate
development line.

## Benchmarking the changes

Before we start to implement individual changes we intend to create a benchmark suite. This benchmark suite should
enable us to assess the changes in memory consumption and runtime due to the new data structures.

## Spectrum/Chromatogram interface

The first decision reached during the discussion was to abandon the `Peak` data structure. It will be replaced by a pair
of `double`s such that a spectrum/chromatogram is a combination of two `std::vector<double>`.

```cpp
class RawDataArray
{
  std::vector<double> intensities_;
  std::vector<double> positions_;
};
```

with invariant `intensities.size() == positions.size()`. This data structure will be augmented with a container to hold
position-wise meta data (see for instance `FloatDataArray`).

```cpp
class RawDataArray
{
  typedef std::vector<DataValue> MetaDataArray;
  typedef std::string MetaDataID;

  std::vector<double> intensities_;
  std::vector<double> positions_;
  std::map<MetaDataID, MetaDataArray> meta_;
};
```

Given this base class `Spectrum` and `Chromatogram` can be derived from this class, redefining `position_` to either
`m/z` or `rt`. Additionally the `Spectrum` and `Chromatogram`  will add relevant members (e.g., MS-level for `Spectrum`)
that should not be stored as meta data.

```
class Spectrum : public RawDataArray
{
  int ms_level_;
  Precursor precursor_;
  double rt_;
  int scan_id_;
};
```

The overall design is summarised in the following figure.

![](/images/research/whitepapers/summary.png)

## MSRun (was MSExperiment)

`MSExperiment` will be renamed to `MSRun`. On top of MSRun we will define an interface that hides the actual implementation
of `MSRun` from the user allowing the use of cached, on-disc, or full in-memory implementations. Direct access to
chromatograms will be hidden behind the `ISpectrumAccess` and `IChromatogramAccess` interfaces.

```cpp
class ISpectrumAccess
{
public:
  int getNrSpectra() const;
  getMetaSpectrum(int i) const;
  const ISpectrum& getSpectrum(int i) const;
  const ExpMeta& getExperimentMeta() const;
  // iterators for spectra
  SpectrumIterator spectrumBegin();
  SpectrumIterator spectrumEnd();
};

class IChromatogramAccess
{
public:
  int getNrChromatograms() const;
  getMetaSpectrum(int i) const;
  const IChromatogram& getChromatogram(int i) const;
  const ExpMeta& getExperimentMeta() const;
  // iterators for chromatograms
  ChromatogramIterator chromatogramBegin();
  ChromatogramIterator chromatogramEnd();
};
```

The overall design is summarised in the following figure.

![](/images/research/whitepapers/design-summary.png)

## Modularisation

We decided that the OpenMS library has to be modularised. Starting with SuperHirn as a proof of concept we will identify
other parts of the library that should be an independent module and move them into a separate library. Additionally we
will add a new library `libOpenMSChemistry` that should implement light-weight alternatives to the existing chemistry
data structures.

To avoid the direct integration of classes associated to UTILS into OpenMS, we will additionally support multi-file UTILS
compared to the existing TOPP like utils, that should consist of only one file.
