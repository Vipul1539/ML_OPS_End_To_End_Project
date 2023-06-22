from setuptools import find_packages,setup
from typing import List   # Typing defines a standard notation for Python function and variable type annotations
                          # This will help to return a list of strings from requirements.txt file


HYPEN_E_DOT='-e .'         # Initialization of variables


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]     # Remove "\n" from requirements.txt file

        if HYPEN_E_DOT in requirements:             # variable to connect requirements.txt with setup.py
            requirements.remove(HYPEN_E_DOT)        # igonore that 
    
    return requirements


setup(
name='ML_OPS_End_To_End_Project',
version='0.0.1',
author='Vipul',
author_email='vipulgupta1539@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   # function to get requirements from requirements.txt.

)