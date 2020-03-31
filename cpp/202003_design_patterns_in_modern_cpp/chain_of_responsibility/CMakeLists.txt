cmake_minimum_required(VERSION 3.10)
project(chain_of_respo)

set(CMAKE_CXX_STANDARD 14)

enable_testing()
find_package(GTest REQUIRED)

add_executable(main
  main.cpp
)
target_link_libraries(main GTest::GTest GTest::Main)
