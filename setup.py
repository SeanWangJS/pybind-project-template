from setuptools import setup

setup(
    name="opscpp",
    version="0.0.1",
    author="seanwang",
    description="A Sample Package for C++ Binding with Pybind11",
    packages=["opscpp"],
    include_package_data=True,
    package_data={"opscpp": ["*.pyi", "*.so"]},
)