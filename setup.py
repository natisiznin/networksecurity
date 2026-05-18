from setuptools import setup, find_packages
from typing import List

def get_requirements() -> list[str]:
    requirement_lst: list[str]=[]
    try:
        with open('requirements.txt') as file:
            lines= file.readline()
        for line in lines:
            requirement=line.strip()
            ## empty lines , ignore -e.
            if requirement and requirement != '-e.':
                requirement_lst.append(requirement)
    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt file not found.")
    return requirement_lst
setup(
    name='network_security',
    version='0.0.1',
    author='sarthak',
    author_email='sarthaknatu001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

