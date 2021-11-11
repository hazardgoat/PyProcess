# PyProcess
A Python library for setting up projects using tabular data. It can create project folders, standardize delimiters, and convert files to CSV from either individual files or a directory.

## Setup
### Functions
`setup.Project_Folders`: Sets up project folders. Creates the main project folder, as well as Data, Methods, and Results folders within it.
### Parameters
`main_dir`: Path to the project directory. Can be an existing folder or one yet to be created.

## Clean
### Functions
`clean.Correct_Delimiter`: Standardizes the delimiter between columns in tabular data files.
### Parameters
`data_in`: File, or directory of files, to be cleaned up <File/Directory Path>

`replacements`: Dictionary of elements to be replaced <to be replaced>:<replacment>, example: {"\t":","}
  
`dir`: Sets whether to process a single file or a directory of files <True/False>
  
`concat_nl`: Sets whether to merge new line delimiters with the last element of each line so as to remove trailing commas <True/False>

## Conversion
### Functions
`convert.CSV`: Converts common tabular data files such as TXT and TSV files to CSV.
### Parameters
`data_in`: File, or directory of files, to be converted <File/Directory Path>
  
`sep`: Delimiter used in the input file, e.g. <",">
  
`dir`: Sets whether to process a single file or a directory of files <True/False>
