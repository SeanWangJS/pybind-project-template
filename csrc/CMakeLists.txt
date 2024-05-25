cmake_minimum_required(VERSION 3.24)

project(ops LANGUAGES CXX)

option(BUILD_PYBIND "Build Python bindings" ON)

set(CMAKE_CXX_STANDARD 17)

find_package (Python3 COMPONENTS Interpreter Development) ##pybind11

set(API_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)

message(STATUS "API_INCLUDE_DIR: ${API_INCLUDE_DIR}")

file(GLOB SOURCES src/*.cpp)
add_library(${PROJECT_NAME} SHARED ${SOURCES})
# target_include_directories(${PROJECT_NAME} PUBLIC include)
include_directories(${API_INCLUDE_DIR})

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