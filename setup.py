from setuptools import setup

setup(
    name="ops-pybind",
    version="0.0.1",
    author="seanwang",
    description="A Sample Package for C++ Binding with Pybind11",
    packages=["ops_pybind"],
    include_package_data=True,
    package_data={"ops_pybind": ["*.pyi", "*.so"]},
)