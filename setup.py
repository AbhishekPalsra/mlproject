####building our application as a package itself.
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .' # trigger setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # replacing \n by blanks
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Abhishek',
author_email='abhipalsra@gmail.com',
package=find_packages(), # find packages used
install_requires=get_requirements('requirements.txt')



) 