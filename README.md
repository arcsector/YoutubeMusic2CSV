# YoutubeMusic2CSV

This script takes input from a youtube music playlist copy+paste job and puts it into a `csv` for use in other places, namely Mathieu Elie's [playlist converter](https://www.playlist-converter.net/#/).

## How to use

First, copy your playlist into a text file. *Note* that only the songs have been selected for copy+paste, not the header or footer data:

<img src="https://raw.githubusercontent.com/arcsector/YoutubeMusic2CSV/master/.github/ytm.png">

Point the script at a target, and it will convert it into a csv. Output file is optional:

```shell
python ytm_to_csv.py \
       ytm_copy_paste.txt \
       optional_output_file.csv
```

You can also import the function into a script for iterative use:

```python
from ytm_to_csv import runParser

myFiles = {
    "infile1.txt": "infile1.csv",
    "infile2.txt": "infile2.csv"
}
for inFile, outFile in myFiles.items():
    runParser(inFile, outFile)
```
