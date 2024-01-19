import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s] : %(message)s:')

project_name = 'Image_Data_Harvesting' # Change the project Name while creating the tempalte

list_of_files = [
    ".github/workfolws/.gitkeep",
    f"src/{project_name}/__init__.py",
    #f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    #'dvc.yaml',
    #'params.yaml'
    'requirements.txt',
    #'setup.py',
    'research/trails.ipynb',
    '.gitignore',
    '.env'
]


for item in list_of_files:
    filepath = Path(item)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok= True)
        logging.info(f'creating directory: {filedir} for file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f'Creating empty file: {filename}')
    else:
        logging.info(f"{filename} is already exists")