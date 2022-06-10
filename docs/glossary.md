OpenMS Glossary
==============

A glossary of common terms used throughout OpenMS documentation.

```{glossary}
```{sorted}

LC-MS
  [Liquid Chromatography(LC)](introduction.md#liquid-chromatography-lc) and [Mass Spectrometry(MS)](introduction.md#mass-spectrometry).

peptides
  A short chain of amino acids.

Octadecyl(C18)
  An alkyl radical C(18)H(37) derived from an octadecane by removal of one hydrogen atom.

Mass
  Mass is a measure of the amount of matter that an object contains. In comparison to often used term weight, which is
  a measure of the force of gravity on that object.

ion
  Any {term}`atom` or group of atoms that bears one or more positive or negative electrical charges. Positively charged are
  cations, negavtively charged anions.

atom
  An atom is the smallest unit of ordinary matter that forms a chemical element.

electrospray ionization
  A technique used in mass spectrometry to produce ions using an electrospray in which a high voltage is applied to a
  liquid to create an {term}`aerosol`.

aerosol
  An aerosol is a suspension of fine solid particles or liquid droplets in air or another gas.

time-of-flight (TOF)
  A measurement of the time taken by an object, particle of wave (be it acoustic, electromagnetic, e.t.c) to travel a
  distance through a medium.

quadrupole mass filters
  A mass filter allowing one mass channel at a time to reach the detector as the mass range is scanned.

orbitrap analyzers
  In mass spectrometry, an ion trap mass analyzer consisting of an outer barrel-like electrode and a coaxial inner
  spindle-like electrode that traps ions in an orbital motion around the spindle.
  A high resoltion mass spectrometry analyzer.

MS(1)
  First stage to get a spectra. A sample is injected into the mass spectrometer, ionized, accelerated and analyzed by
  mass spectrometry.

MS(2)
  Ions from MS1 spectra are then selectively fragmented and analyzed by a second stage of mass spectrometry (MS2) to
  generate the spectra for the ion fragments.

MS/MS
  Tandem mass spectrometry, MS^2^, a technique where two or more mass analyzers are coupled together using an additional
  reaction step to increase their abilities to analyse chemical samples.

collision-induced dissociation (CID)
  A mass spectrometry technique to induce fragmentation of selected ions in the gas phase. Also known as Collision
  induced dissociation.

TOPP
  The OpenMS Proteomics Pipeline.

TOPPAS.app
  TOPPAS allows to create, edit, open, save, and run TOPP workflows.

MSGFPlusAdapter
  Adapter for the MS-GF+ protein identification (database search) engine. More information is available [here](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_MSGFPlusAdapter.html).

LuciphorAdapter
  Adapter for the LuciPHOr2: a site localisation tool of generic post-translational modifications from tandem mass
  spectrometry data. More information is available [here](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_LuciphorAdapter.html).

pyOpenMS
  pyOpenMS is an open-source Python library for mass spectrometry, specifically for the analysis of proteomics and
  metabolomics data in Python. For pyOpenMS documentaion visit [this](https://pyopenms.readthedocs.io/en/latest/) link.

TOPP Tools
  All {term}`TOPP` tools can be found [here](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_documentation.html).

UTILS
  Besides TOPP, OpenMS offers a range of other tools. They are not included in TOPP as they are not part of typical
  analysis pipelines. More information is present in [OpenMS UTILS Documentation)(https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/UTILS_documentation.html).

TOPPView
  TOPPView is a viewer for MS and HPLC-MS data. More information is available in [TOPPView documentation](topp/toppview.md).

[Nightly Snapshot](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html)
  Untested installers and containers are known as the nightly snapshot.

proteomics
  Proteomics is the large-scale study of proteins.

proteins
  Proteins are vital parts of living organisms, with many functions, for example composing the structural fibers of
  muscle to the enzymes that catalyze the digestion of food to synthesizing and replicating DNA.

Mascot
  Identifies peptides in MS/MS spectra via Mascot. Please find more information in the {term}`TOPP` [Documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_MascotAdapter.html).

HPLC-MS
  Data produced by High performance liquid chromatography (HPLC) separates components of a mixture, whereas mass
  spectrometry (MS) offers the detection tools to identify them.

mzML
  The mzML format is an open, XML-based format for mass spectrometer output files, developed with the full participation
  of vendors and researchers in order to create a single open format that would be supported by all software.

mzData
  mzData was the first attempt by the Proteomics Standards Initiative (PSI) from the Human Proteome Organization (HUPO)
  to create a standardized format for Mass Spectrometry data.[7] This format is now deprecated, and replaced by mzML.

mzXML
  mzXML is an open data format for storage and exchange of mass spectroscopy data, developed at the SPC/Institute for
  Systems Biology.

spectra
  Singluar of spectrum.

spectrum
  A mass spectrum is a type of plot of the ion signal as a function of the mass-to-charge ratio. These spectra are used
  to determine the elemental or isotopic signature of a sample, the masses of particles and of molecules, and to
  elucidate the chemical identity or structure of molecules and other chemical compounds.

m/z
  mass to charge ratio.

RT
  Retention time (RT).

ProteoWizard
  ProteoWizard is a set of open-source, cross-platform tools and libraries for proteomics data analyses. It provides a
  framework for unified mass spectrometry data file access and performs standard chemistry and LCMS dataset computations.

OMSSA
  The Open Mass Spectrometry Search Algorithm (OMSSA) is an efficient search engine for identifying {term}`MS/MS`
  {term}`peptide` {term}`spectra` by searching libraries of known protein sequences.

PepNovo
  PepNovo is a de novo sequencing algorithm for {term}`MS/MS` {term}`spectra`.

de novo peptide sequencing
  A peptide’s amino acid sequence is inferred directly from the precursor peptide mass and tandem mass spectrum
  ({term}`MS/MS` or {term}`MS^3`) fragment ions, without comparison to a reference proteome.

TOPPAS
  An assistant for GUI-driven TOPP workflow design.
```
