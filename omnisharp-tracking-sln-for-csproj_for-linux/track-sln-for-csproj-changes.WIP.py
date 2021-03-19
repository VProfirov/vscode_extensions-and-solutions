#current suggested path localdir/.vscode/*.py

from pathlib import Path

def get_project_names_from_sln():
    # sln_file_dir = Path.abspath
    # print(f'PATH: {sln_file_dir}')
    print(__file__/'..')
    sln_file = open(__file__/'..'/'*.sln','r')
    return sln_file


print(f'-----.sln------')
print(get_project_names_from_sln())
print(f'------end-------')