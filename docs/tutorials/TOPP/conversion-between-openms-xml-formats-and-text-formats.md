Conversion Between OpenMS XML Formats and Text Formats
=====================================================

## Export of OpenMS XML formats

As TOPP offers no functionality for statistical analysis, this step is normally done using external statistics packages.
In order to export the OpenMS XML formats into an appropriate format for these packages the TOPP **TextExporter** can be
used.

It converts the the following OpenMS XML formats to text files:

- featureXML
- idXML
- consensusXML

The use of the **TextExporter** is is very simple:

`TextExporter -in infile.idXML -out outfile.txt`

## Import of feature data to OpenMS

OpenMS offers a lot of visualization and analysis functionality for feature data.
Feature data in text format, e.g. from other analysis tools, can be imported using the **TextImporter**. The default
mode accepts comma separated values containing the following columns: RT, m/z, intensity. Additionally meta data
columns may follow. If meta data is used, meta data column names have to be specified in a header line. Without headers:

```
1201	503.123	1435000
1201	1006.246	1235200
```

Or with headers:

```
RT	m/z	Int	isHeavy	myMeta
1201	503.123	1435000	true	2
1201	1006.246	1235200	maybe	1
```

Example invocation:

`TextImporter -in infile.txt -out outfile.featureXML`

The tool also supports data from msInspect,SpecArray and Kroenik(Hardkloer sibling), just specify the -mode option
accordingly.

## Import of protein/peptide identification data to OpenMS

Peptide/protein identification data from several identification engines can be converted to idXML format using the
**IDFileConverter** tool.

It can currently read the following formats:
- Sequest output folder
- pepXML file
- idXML file

It can currently write the following formats:

- pepXML
- idXML

This example shows how to convert pepXML to idXML:

`IDFileConverter -in infile.pepXML -out outfile.idXML`
