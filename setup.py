import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="silu", 
    version="0.0.1",
    author="Dai Hongbin", 
    author_email="pipdax@126.com", 
    description="SILU, a new way to develop risk models.",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/pipdax/silu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
