# YoutubeMusic2CSV

This script takes input from a youtube music playlist copy+paste job and puts it into a `csv` for use in other places, namely Mathieu Elie's [playlist converter](https://www.playlist-converter.net/#/).

## How to use

Point the script at a target, and it will convert it into a csv. Output file is optional:

```shell
python ytm_to_csv.py ytm_copy_paste.txt optional_output_file.csv
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
