from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="fakefarsi",
    version="0.0.4",
    author="Mahan Rahmani",
    author_email="mahanrahmani777@gmail.com",
    description="A package for generate a fake iranian person information",
    long_description=readme,
    url="https://github.com/mhnrhmni/FakeFarsi/",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Mit License",
        "Operating System :: OS Independent",
    ],
)