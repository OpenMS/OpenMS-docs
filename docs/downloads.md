# OpenMS Installers
::::{tab-set}

:::{tab-item} release
:sync: release
| Platform | Name | SHA256 Hash |
|----------|------|-------------|
| Windows   | {{ '[OpenMS-{0}-Win64.exe](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/{0}/OpenMS-{0}-Win64.exe)'.format(version) }} | `d203985c7042b885ac1085c30a2d9f36d7609b47`|
| macOS | [OpenMS-2.8.0-macOS.dmg](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-macOS.dmg) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| GNU/Linux | [OpenMS-2.8.0-Debian-Linux-x86_64.deb](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-Debian-Linux-x86_64.deb) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| Source | [OpenMS-2.8.0-src.tar.gz](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-src.tar.gz) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
:::

:::{tab-item} RC
:sync: RC
| Platform | Name | SHA256 Hash |
|----------|------|-------------|
| Windows   | {{ '[OpenMS-{0}-Win64.exe](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/{0}/OpenMS-{0}-Win64.exe)'.format(version) }} | `d203985c7042b885ac1085c30a2d9f36d7609b47`|
| macOS | [OpenMS-2.8.0-macOS.dmg](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-macOS.dmg) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| GNU/Linux | [OpenMS-2.8.0-Debian-Linux-x86_64.deb](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-Debian-Linux-x86_64.deb) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| Source | [OpenMS-2.8.0-src.tar.gz](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-src.tar.gz) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
:::

:::{tab-item} nightly
:sync: nightly
| Platform | Name | SHA256 Hash |
|----------|------|-------------|
| Windows   | {{ '[OpenMS-{0}-Win64.exe](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/{0}/OpenMS-{0}-Win64.exe)'.format(version) }} | `d203985c7042b885ac1085c30a2d9f36d7609b47`|
| macOS | [OpenMS-2.8.0-macOS.dmg](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-macOS.dmg) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| GNU/Linux | [OpenMS-2.8.0-Debian-Linux-x86_64.deb](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-Debian-Linux-x86_64.deb) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
| Source | [OpenMS-2.8.0-src.tar.gz](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/2.8.0/OpenMS-2.8.0-src.tar.gz) | `d203985c7042b885ac1085c30a2d9f36d7609b47` |
:::

::::

# Workflows

| Workflow | Description | Download Link |
|----------|-------------|---------------|
|`ProteomicsLFQ_tool_and_MSstats_postprocessing` | Label-free identification and quantification using the comet search engine, the ProteomicsLFQ tool and statistical down-stream processing using MSstats. Compared to the other proteomics LFQ workflows, it is less complex as it combines quantification and inference steps in a single ProtemicLFQ tool. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/ProteomicsLFQ_tool_and_MSstats_postprocessing.knwf?raw=true) |
|`DIAMetAlyzer` | Metabolomics assay library construction with decoy generation from DDA data and targeted DIA analysis using OpenSWATH and pyprophet for statistical validation. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/DIAMetAlyzer.knwf?raw=true) |
|`Identification_quantification_with_inference_isobaric_epifany_MSstatsTMT` | Identification and quantification for isobaric experiments using MSGFPlus as search engine, epifany for inference and MSstatsTMT for statistical down-stream analysis. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Identification_quantification_with_inference_isobaric_epifany_MSstatsTMT.knwf?raw=true) |
|`labelfree_with_protein_quantification` | Label-free with protein quantification steps implemented using individual OpenMS tools | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/labelfree_with_protein_quantification.knwf?raw=true) |
|`Metabolite_Adduct_Grouping` | Quantification and identification via accurate mass based on multiple adduct grouping steps (adducts, neutral losses). | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Metabolite_Adduct_Grouping.knwf?raw=true) |
|`Metabolite_DeNovoID` | Quantification and identification via adduct grouping and de-novo identification using SIRIUS/CSI:FingerID. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Metabolite_DeNovoID.knwf?raw=true) |
|`Metabolite_ID` | Quantification and identification via accurate mass based with downstream processing and visualisation. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Metabolite_ID.knwf?raw=true) |
|`Metabolite_SpectralID` | Identification via spectral library search for small molecules. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Metabolite_SpectralID.knwf?raw=true) |
|`MSstats_statPostProcessing_iPRG2015` | Post processing workflow for using MSstats based on "Example_OneTool_ProteomicsLFQ_MSstats.knwf" | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/MSstats_statPostProcessing_iPRG2015.knwf?raw=true) |
|`MSstatsTMT` | Post processing workflow for using MSstatsTMT based on "Identification_quantification_with_inference_isobaric_epifany_MSstatsTMT". | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/MSstatsTMT.knwf?raw=true) |
|`OpenSWATH` | Targeted extraction and scoring of transitions in DIA data based on an (iRT) assay library. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/OpenSWATH.knwf?raw=true) |
|`Phosphoproteomics_ID` | Identification of Phosphorilation sites. | [Download](https://github.com/OpenMS/Tutorials/blob/master/Workflows/Phosphoproteomics_ID.knwf?raw=true) |

# OpenMS Releases

| Release                                                |  Installers |
|--------------------------------------------------------|-------------|
| Stable release     | [Archive Link](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/) |
| Release candidates | [Archive Link](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/RC/) |
| Nightly release    | [Archive Link](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/) |

# Other Resources

| Name | Description | Download Link |
|------|-------------|---------------|
| Schemas | Documented schemas of the OpenMS formats | [Download](https://github.com/OpenMS/OpenMS/tree/develop/share/OpenMS/SCHEMAS)|
| iPRG2016 data | Dataset mxMLs, Fasta database, Identification file (idXML), Big Data (idXML) | [Download](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Tutorials/Data/iPRG2016/) |
