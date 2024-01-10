from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

        
REPO_NAME = "Book-Recommender-System"
AUTHOR_USER_NAME = "rachitdani"
SRC_REPO = "src"


setup(
    name="SRC_REPO",
    version='0.0.1',
    author='Rachit',
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email='rachitdani2014@gmail.com',
    install_requires= get_requirements('requirements.txt'),
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7"

)