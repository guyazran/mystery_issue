import setuptools
import os


setuptools.setup(
    name="some-pkg-myuser",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A package with `config`",
    packages=setuptools.find_packages(where=os.path.dirname(__file__)),
)