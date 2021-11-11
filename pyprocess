import os
import re
import pandas as pd
from pathlib import Path


# Class holding functions for setting up a new project
class Setup():
    
    '''
    Sets up project folders

    main_dir: path to the project directory. Can be an existing folder or one yet to be created.
    '''
    def Project_Folders(self, main_dir):

        data_folder = os.path.join(main_dir, 'Data')
        methods_folder = os.path.join(main_dir, 'Methods')
        results_folder = os.path.join(main_dir, 'Results')

        directories = [main_dir, data_folder, methods_folder, results_folder]

        # Iterates through the list of directories and creates them if they don't already exist
        for directory in directories:
            os.makedirs(directory, exist_ok = True)
        
setup = Setup()



# Class holding functions for cleaning tabluar data such as text and csv files
class Clean():
    
    '''
    Standardizes the delimiter between columns.

    data_in: file, or directory of files, to be cleaned up <File/Directory Path>
    replacements: dictionary of elements to be replaced <to be replaced>:<replacment>, example: {"\t":","}
    dir: sets whether to process a single file or a directory of files <True/False>
    concat_nl: sets whether to merge new line delimiters with the last element of each line so as to remove trailing commas <True/False>
    '''
    def Correct_Delimiter(self, data_in, replacements, dir=False, concat_nl=False):
        out_dir = os.path.join(data_in, 'Cleaned_Files')
        os.makedirs(out_dir, exist_ok = True)

        if dir == False:
            self.Process_Delimiter_Correction(replacements, data_in, out_dir, concat_nl)  

        else:
            for f_name in os.listdir(data_in):
                if os.path.isfile(os.path.join(data_in, f_name)):

                    f_in = os.path.join(data_in, f_name)

                    self.Process_Delimiter_Correction(replacements, f_in, out_dir, concat_nl)    


    # Preforms the delimiter standardization called in the Correct_Delimiter function so as to reduce code duplication.
    def Process_Delimiter_Correction(self, replacements, out_dir, f_in, concat_nl):
        with open(f_in, 'r') as f:
            data = f.read()

        # subsitutes text using the patterns in "replacements"
        for key, value in replacements.items():
            data = re.sub(key, value, data)

        p = Path(data)
        f_out = os.path.join(out_dir, p.stem+'_cleaned'+p.suffix)

        with open(f_out, 'w') as f:
            f.write(data)
            
        self.Remove_Empty_Columns(f_out)

        if concat_nl == False:
            pass
        else:
            self.Concatonate_New_Line(f_out) 


    # Removes any empty columns that get created when the delimiter is standardized (file specific). Has no effect if no empty columns are created.
    def Remove_Empty_Columns(self, f_out):
        with open(f_out, 'r') as f:
            data = f.readlines()

        with open(f_out, 'w') as f:            
            pass
        
        for line in data:
            split_data = line.split(',')
            i = -1
            for element in split_data:
                if element == '':
                    i += 1
                    split_data.pop(i)
                    
                else:
                    i += 1

            rejoined_line = ','.join(split_data)

            with open(f_out, 'a') as f:            
                f.write(rejoined_line)


    # Merges new line delimiters with the last element of each line so as to remove trailing commas
    def Concatonate_New_Line(self, f_out):
        with open(f_out, 'r') as f:
            data = f.readlines()

        with open(f_out, 'w') as f:
            pass

        for line in data:
            split_data = line.split(',')
            if split_data[-1] == '\n':
                split_data.pop(-1)
                split_data[-1] = split_data[-1]+'\n'

            rejoined_line = ','.join(split_data)
            with open(f_out, 'a') as f:
                f.write(rejoined_line)

clean = Clean()



# Class holding functions for converting tabluar data files to other file types
class Conversion():

    '''
    Converts common tabular data files to CSV.

    data_in: file, or directory of files, to be converted <File/Directory Path>
    sep: delimiter used in the input file, e.g. <",">
    dir: sets whether to process a single file or a directory of files <True/False>
    '''
    def CSV(self, data_in, sep=',', dir=False):

        if dir == False:
            df_data_in = pd.read_csv(data_in, sep=sep)

            p = Path(data_in)
        
            out_dir = os.path.join(p.parent, 'CSV_Converted')
            os.makedirs(out_dir, exist_ok = True)

            file_name = p.stem

            save_name = os.path.join(out_dir, '{}.csv').format(file_name)

            df_data_in.to_csv(save_name, sep=',', index=False)

        else:
            out_dir = os.path.join(data_in, 'CSV_Converted')
            os.makedirs(out_dir, exist_ok = True)

            for f_name in os.listdir(data_in):
                if os.path.isfile(os.path.join(data_in, f_name)):
                    
                    f_in = os.path.join(data_in, f_name)

                    df_f_in = pd.read_csv(f_in, sep=sep)

                    p = Path(f_in)

                    file_name = p.stem

                    save_name = os.path.join(out_dir, '{}.csv').format(file_name)

                    df_f_in.to_csv(save_name, sep=',', index=False)

convert = Conversion()
