cmake_minimum_required(VERSION 3.10)
project(iterator)

set(CMAKE_CXX_STANDARD 14)

enable_testing()
find_package(GTest REQUIRED)

add_executable(iterator
  iterator.cpp
)

target_link_libraries(iterator GTest::GTest GTest::Main)
