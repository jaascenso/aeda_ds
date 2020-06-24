from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name = "aed-ds",
    version = "0.0.1",
    author = "AED",
    author_email = "aed@autonoma.pt",
    description = "Data structures",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/amgs/aed_ds",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)