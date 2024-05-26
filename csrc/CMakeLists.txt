cmake_minimum_required(VERSION 3.24)

project(ops LANGUAGES CXX)

option(BUILD_PYBIND "Build Python bindings" ON)

set(CMAKE_CXX_STANDARD 17)

find_package (Python3 COMPONENTS Interpreter Development)

set(API_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)
set(TARGET_NAME ops)
set(SHARED_TARGET ${TARGET_NAME})

file(GLOB SOURCES src/*.cpp)
add_library(${SHARED_TARGET} SHARED ${SOURCES})
include_directories(${API_INCLUDE_DIR}) ## 

if(BUILD_PYBIND)
  message(STATUS "Building Python bindings")
  add_subdirectory(pybind)
endif()

## add test if find google test
find_package(GTest)
if(GTest_FOUND)
  message(STATUS "Google Test found") 
  add_subdirectory(test)
  enable_testing()
endif()