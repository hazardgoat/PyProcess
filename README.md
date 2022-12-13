# PyProcess
A Python package for setting up projects using tabular data. It can create project folders, standardize delimiters, and convert files to CSV from either individual files or a directory.

# Documentation
To install, navigate to the directory holding your Python libraries, then copy the "pyprocess" folder into it. The pyrocess folder should contain the `pyprocess.py` and `__init__.py` files.

Example path: `C:\Users\<user>\miniconda3\envs\<user envs>\Lib\site-packages\pyprocess`

## Class - Setup
#### Functions
`setup.Project_Folders`: Sets up project folders. Creates the main project folder, as well as *Data*, *Methods*, and *Results* folders within it.
#### Parameters
`proj_dir`: Path to the project directory. Can be an existing folder or one yet to be created.

## Class - Clean
#### Functions
`clean.Clean_Text`: Cleans up text in files, with parameters for further cleaning up files when standarizing delimiters in tabular data. Saves the cleaned files to a folder named *Cleaned_Files* within the input directory.
#### Parameters
`data_in`: File, or directory of files, to be cleaned up. *file/directory path*

`replacements`: Dictionary of elements to be replaced. *to-be-replaced:replacement*, Example: replacements={"\t":","}
  
`dir`: Sets whether to process a single file or a directory of files. *True/False*
  
`delete_empty`: Removes any empty columns that get created when the delimiter is standardized (file specific). Has no effect if no empty columns are created. *True/False*

`concat_newline`: Sets whether to merge new line delimiters with the last element of each line so as to remove trailing commas. *True/False*

## Class - Conversion
#### Functions
`convert.CSV`: Converts common tabular data files such as TXT and TSV files to CSV. Saves the converted files to a folder named *CSV_Converted* within the input directory.
#### Parameters
`data_in`: File, or directory of files, to be converted. *file/directory path*
  
`sep`: Delimiter used in the input file. Example: sep=","
  
`dir`: Sets whether to process a single file or a directory of files. *True/False*
