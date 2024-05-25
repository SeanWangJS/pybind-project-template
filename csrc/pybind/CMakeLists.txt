## Find pybind11 CMake directory
execute_process(
  COMMAND ${Python3_EXECUTABLE} "-c"
          "import pybind11 as pb11; print(pb11.get_cmake_dir(),end='');"
  RESULT_VARIABLE PYBIND_CMAKE_DIR_RET
  OUTPUT_VARIABLE PYBIND_CMAKE_DIR)

if(PYBIND_CMAKE_DIR_RET MATCHES 0)
  list(APPEND CMAKE_PREFIX_PATH "${PYBIND_CMAKE_DIR}")
else()
  message(ERROR "pybind11 CMake directory not found.")
endif()

find_package(pybind11 REQUIRED)  

set(OPS_PYBIND_MODULE bindings) 
add_definitions(-DOPS_PYBIND_MODULE=${OPS_PYBIND_MODULE}) 

set(SRCS bindings.cpp)
pybind11_add_module(${OPS_PYBIND_MODULE} ${SRCS}) 
