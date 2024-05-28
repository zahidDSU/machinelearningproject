from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    """
    This functional will return the list of requirements
    """
    
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements ]
    return requirements

    

setup(
    
    name = "mlproject",
    version="0.01",
    description="first ml project",
    author="Zahid Hussain",
    author_email="zahid.hussain@dsu.edu.pk",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)