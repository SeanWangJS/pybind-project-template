this is my python binding project's structure, how to write the setup.py file bind the c++ code to python code?
```
csrc/
--include/
  |--ops.h
--src/
  |--bindings.cpp
--test/
  |--test_ops.cpp
  |--CMakelists.txt
--CMakeLists.txt
python/
--__init__.py
--ops.py
scripts/
--build_wheel.py
CMakeLists.txt
README.md
setup.py
```