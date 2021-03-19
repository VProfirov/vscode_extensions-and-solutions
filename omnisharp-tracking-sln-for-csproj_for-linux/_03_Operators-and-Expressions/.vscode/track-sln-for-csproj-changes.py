#current suggested path localdir/.vscode/*.py

from pathlib import Path

print(f'-----.sln------')

# def get_project_names_from_sln():
script_file_path = __file__
# ../.vscode/
script_parent_dir = Path(script_file_path).parent
# ../*.sln
sln_parent_dir = Path(script_parent_dir).parent

print(f'--> {sln_parent_dir}')
# print(f'--> {sln_file_dir.parent.parent}')


# print(get_project_names_from_sln())
print(f'------end-------')



#DOCUMENATION on PATH handling: https://realpython.com/python-pathlib/