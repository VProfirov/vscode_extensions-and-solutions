#current suggested path localdir/.vscode/*.py

from pathlib import Path
import pathlib
import os
# with open(Path(__file__).parent.parent/str('*.sln'),mode='r')


print(f'-----.sln------')

# def get_project_names_from_sln():
script_file_path = __file__
# ../.vscode/
script_parent_dir = Path(script_file_path).parent
# ../*.sln
sln_parent_dir = Path(script_parent_dir).parent

print(f'--> {sln_parent_dir}')

#files in current dir
dirs_files = Path(sln_parent_dir).iterdir()

print(f'--> --> {dirs_files}')
print(f'--> os --> {os.getcwd()}')

# print(f'--> {sln_file_dir.parent.parent}')
filestream = open(sln_parent_dir/'_03_Operators-and-Expressions.sln','r')
print(f'--> {filestream}')

# s1 = filestream.
content_file = filestream.read()
print(f'--> {content_file}')
# print(get_project_names_from_sln())
print(f'------end-------')

#DOCUMENATION on PATH handling: https://realpython.com/python-pathlib/