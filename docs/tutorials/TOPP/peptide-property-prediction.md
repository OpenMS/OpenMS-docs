Peptide Property Prediction
===========================

You can train a model for retention time prediction as well as for the prediction of proteotypic peptides.

Two applications has been described in the following publications: Nico Pfeifer, Andreas Leinenbach, Christian G. Huber
and Oliver Kohlbacher Statistical learning of peptide retention behavior in chromatographic separations: A new
kernel-based approach for computational proteomics. BMC Bioinformatics 2007, 8:468 Nico Pfeifer, Andreas Leinenbach,
Christian G. Huber and Oliver Kohlbacher Improving Peptide Identification in Proteome Analysis by a Two-Dimensional
Retention Time Filtering Approach J. Proteome Res. 2009, 8(8):4109-15.

The predicted retention time can be used in `IDFilter` to filter out false identifications. For data from several
identification runs:

1. Align the data using MapAligner.
2. Use the various identification wrappers like `MascotAdapter`, `OMSSAAdapter`, ... to get the identifications.
3. To train a model using `RTModel` use `IDFilter` for one of the runs to get the high scoring identifications (40 to 200
   distinct peptides should be enough).
4. Use RTModel as described in the documentation to train a model for these spectra. With this model, use RTPredict
   to predict the retention times for the remaining runs. The predicted retention times are stored in the idXML files.
   These predicted retention times can then be used to filter out false identifications using the IDFilter tool.

A typical sequence of TOPP tools would look like this:

```
MapAligner -in Run1.mzML,...,Run4.mzML -out Run1_aligned.mzML,...,Run4_aligned.mzML
MascotAdapter -in Run1_aligned.mzML -out Run1_aligned.idXML -ini Mascot.ini
MascotAdapter -in Run2_aligned.mzML -out Run2_aligned.idXML -ini Mascot.ini
MascotAdapter -in Run3_aligned.mzML -out Run3_aligned.idXML -ini Mascot.ini
MascotAdapter -in Run4_aligned.mzML -out Run4_aligned.idXML -ini Mascot.ini
IDFilter -in Run1_aligned.idXML -out Run1_best_hits.idXML -pep_fraction 1 -best_hits
RTModel -in Run1_best_hits.idXML -out Run1.model -ini RT.ini
RTPredict -in Run2_aligned.idXML -out Run2_predicted.idXML -svm_model Run1.model
RTPredict -in Run3_aligned.idXML -out Run3_predicted.idXML -svm_model Run1.model
RTPredict -in Run4_aligned.idXML -out Run4_predicted.idXML -svm_model Run1.model
IDFilter -in Run2_predicted.mzML -out Run2_filtered.mzML -rt_filtering
IDFilter -in Run3_predicted.mzML -out Run3_filtered.mzML -rt_filtering
IDFilter -in Run4_predicted.mzML -out Run4_filtered.mzML -rt_filtering
```

For a file with certainly identified peptides used to train a model for RT prediction, use the IDs. Therefore, the file
has to have one peptide sequence together with the RT per line (separated by one tab or space). This can then be loaded
by RTModel using the `-textfile_input` flag:

```
RTModel -in IDs_with_RTs.txt -out IDs_with_RTs.model -ini RT.ini -textfile_input
```

The likelihood of a peptide to be proteotypic can be predicted using PTModel and PTPredict.

Assume we have a file `PT.idXML` which contains all proteotypic peptides of a set of proteins. Lets also assume, we have
a fasta file containing the amino acid sequences of these proteins called `mixture.fasta`. To be able to train PTPredict,
negative peptides (peptides, which are not proteotypic) are required. Therefore, one can use the Digestor, which is
located in the `APPLICATIONS/UTILS/` folder together with the IDFilter:

```
Digestor -in mixture.fasta -out all.idXML
IDFilter -in all.idXML -out NonPT.idXML -exclusion_peptides_file PT.idXML

```

In this example the proteins are digested in silico and the non proteotypic peptides set is created by subtracting all
proteotypic peptides from the set of all possible peptides. Then, train PTModel:

`PTModel -in_positive PT.idXML -in_negative NonPT.idXML -out PT.model -ini PT.ini`
