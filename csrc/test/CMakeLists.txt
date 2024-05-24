project(test_ops LANGUAGES CXX)

find_package(GTest REQUIRED)

add_executable(test_ops test.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include)

target_link_libraries(${PROJECT_NAME} PRIVATE GTest::GTest GTest::Main)
target_link_libraries(${PROJECT_NAME} PRIVATE ops)

