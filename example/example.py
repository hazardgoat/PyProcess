import os
from pyprocess import pyprocess as pp

# Setup
project_dir = r'/home/USER/Desktop/MyProject'
pp.setup.Project_Folders(project_dir)

# Cleaning
files_dir = os.path.join(project_dir, 'Data')
replacements = {' +':',', '\t':','}
pp.clean.Clean_Text(files_dir, replacements, dir=True, delete_empty=True, concat_newline=True)

# Conversion
files_dir = os.path.join(files_dir, 'Cleaned_Files')
pp.convert.CSV(files_dir, sep=',', dir=True)
