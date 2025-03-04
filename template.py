import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

project_structure = {
    ".github/workflows": [".gitkeep"],
    "src/components": ["__init__.py"],
    "src/utils": ["__init__.py"],
    "src/config": ["__init__.py", "configuration.py"],
    "src/pipeline": ["__init__.py"],
    "src/entity": ["__init__.py"],
    "src/constants": ["__init__.py"],
    "config": ["config.yaml"],
    "research": ["trails.ipynb"],
    "templates": ["index.html"],
}

root_files = ["dvc.yaml", "params.yaml", "requirements.txt", "setup.py"]


for directory, files in project_structure.items():
    os.makedirs(directory, exist_ok=True) 
    for file in files:
        filepath = os.path.join(directory, file)
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass  
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")


for file in root_files:
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, "w") as f:
            pass  
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"File already exists: {file}")

logging.info("Project structure setup is complete!")
