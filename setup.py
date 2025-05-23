# setup.py
from setuptools import find_packages, setup

setup(
    name="mlproject",
    version="0.0.1",
    author="SUMEDHA SINGH",
    author_email="sumedhasinghpaliwal@gamil.com",
    packages=find_packages(),
    install_requires=[],
)
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements
