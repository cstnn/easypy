
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EasyPy",
    version="0.0.1",
    author="Costin Nadolu",
    author_email="costin.nadolu@gmail.com",
    description="An entry level library to help beginner users with some quick functions.",
    long_description="An entry level library to help beginner users with some quick functions that otherwise are a bit difficult to remember how to use or are cumbersome to write frequently.",
    long_description_content_type="text/markdown",
    url="https://github.com/cstn/easy_py",
    packages=setuptools.find_packages(),
    install_requires=['DateTime',                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)