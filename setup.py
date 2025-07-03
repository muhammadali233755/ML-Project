from setuptools import setup,find_packages
from typing import List

HYFEN_E_DOT = " -e ."


def get_requirements(file_path:str) ->List[dict]:
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)
        return requirements


setup(
    name="MachinelearningProject",
    version="0.0.1",
    author="M.Ali",
    author_email= "muhammadali233755@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
    
)


