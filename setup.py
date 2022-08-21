# Modules
import os
import codecs
import pathlib
from setuptools import setup

# Grab our current path
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding = "utf-8")

# Package finder
def find_packages(dir):
    packs = []
    for p, _, __ in os.walk(dir):
        path = p.replace("\\", "/").replace("/", ".").replace(dir + ".", "")
        if "egg-info" not in path and "__pycache__" not in path:
            if path != dir:
                packs.append(path)

    return packs

# Handle versions (https://github.com/pypa/pip/blob/main/setup.py#L11)
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = "\"" if "\"" in line else "'"
            return line.split(delim)[1]

    else:
        raise RuntimeError("Unable to find version string.")

# Handle setup
setup(
    name = "phat2fa",
    version = get_version("src/phat/__init__.py"),
    description = "Simple 2FA made using USB thumbdrives",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "iiPython",
    author_email = "ben@iipython.cf",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    license = "MIT",
    python_requires = ">=3.10, <4",
    install_requires = open("reqs.txt", "r").read().splitlines(),
    package_dir = {"": "src"},
    packages = find_packages("src"),
    entry_points = """
        [console_scripts]
        phatsetup=phat.__main__:setup
    """,
)
