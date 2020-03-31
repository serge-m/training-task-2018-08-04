cmake_minimum_required(VERSION 3.10)
project(interpreter)

set(CMAKE_CXX_STANDARD 14)

enable_testing()
find_package(GTest REQUIRED)

add_executable(interpreter
  interpreter.cpp
)

target_link_libraries(interpreter GTest::GTest GTest::Main)
