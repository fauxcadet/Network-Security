'''
this setiup.py file is a n essential part of packaging and distributing pytho projects. it is used bty setup tools
to define and cofiguration of project '''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """this fnx will return list of requirements"""
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
        ##read lines from the file
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirement=line.strip()
                ## ingrnore the empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found'")                
    return requirement_list    

setup(
    name="Network Security",
    version="0.0.1",
    author="Sourav",
    author_email="chouhansourav4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)
