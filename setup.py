import setuptools

__version__ = "0.0.1"
__author__ = "Tyler Bruno"


with open("README.md", "r", encoding="utf-8") as file:
    README = file.read()

with open("requirements.txt", "r") as file:
    INSTALL_REQUIRES = file.read().splitlines()

setuptools.setup(
    name="parsers",
    version=__version__,
    author=__author__,
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="python parsers",
    url="https://github.com/tybruno/parsers",
    license="MIT",
    package_data={"parsers": ["py.typed"]},
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
