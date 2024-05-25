import os
from pathlib import Path
from subprocess import run
from functools import partial
from shutil import copy
import glob
import sys
from contextlib import contextmanager

@contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit."""
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

def main(args):

    PROJECT_DIR = Path(__file__).parent.resolve().parent

    source_dir = PROJECT_DIR / "csrc"
    build_dir = source_dir / "build"

    build_run = partial(run, shell=True, check=True)

    ## Build the C++ library
    build_run(f"cmake -S {source_dir} -B {build_dir}")
    build_run(f"cmake --build {build_dir}")

    ## Copy the pybind library to the package directory
    pkg_dir = PROJECT_DIR / "opscpp"

    def get_pybind_lib():
        pybind_build_dir = build_dir / "pybind"
        pybind_lib = list(pybind_build_dir.glob("bindings.*.so"))
        # pybind_lib = glob.glob(f"{pybind_build_dir}/bindings.*.so")
        assert len(pybind_lib) == 1, f"Exactly one pybind library should be present: {pybind_lib}"
        return pybind_lib[0]

    copy(get_pybind_lib(), pkg_dir)

    ## Generate the pyi file
    with working_directory(pkg_dir):
        build_run(f"\"{sys.executable}\" -m pybind11_stubgen -o . bindings")

if __name__ == "__main__":
    args = None
    main(args)