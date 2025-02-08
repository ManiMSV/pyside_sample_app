[app]
# title of your application
title = My Application
# project directory
project_dir = C:\Projects\pyside_sample_app\src\Main
# source file path
input_file = main.py
# directory where exec is stored
exec_directory = C:\Projects\pyside_sample_app\src\Main

[python]
# python path
python_path = C:\Projects\pyside_sample_app\venv\Scripts\python.exe
# python packages to install
# ordered-set = increase compile time performance of nuitka packaging
# zstandard = provides final executable size optimization
packages = nuitka,ordered_set,zstandard

[qt]
# comma separated path to qml files required
# normally all the qml files are added automatically
qml_files = 

[nuitka]
# (str) specify any extra nuitka arguments
# eg = extra_args = --show-modules --follow-stdlib
extra_args = --quiet

