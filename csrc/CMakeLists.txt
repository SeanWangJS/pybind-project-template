cmake_minimum_required(VERSION 3.24)

project(ops LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(OPS_PYBIND_MODULE bindings)

add_definitions(-DOPS_PYBIND_MODULE=${OPS_PYBIND_MODULE}) ##pybind11

find_package(pybind11 REQUIRED)  ##pybind11
find_package (Python3 COMPONENTS Interpreter Development) ##pybind11

file(GLOB SOURCES src/*.cpp)

add_library(${PROJECT_NAME} SHARED ${SOURCES})
pybind11_add_module(${OPS_PYBIND_MODULE} ${SOURCES}) ##pybind11

target_include_directories(${PROJECT_NAME} PUBLIC include)
target_include_directories(${PROJECT_NAME} PUBLIC ${pybind11_INCLUDE_DIR} ${Python3_INCLUDE_DIRS}) ##pybind11

target_include_directories(${OPS_PYBIND_MODULE} PUBLIC include) ##pybind11

target_link_libraries(${PROJECT_NAME} ${Python3_LIBRARIES} util)

add_subdirectory(test)
enable_testing()