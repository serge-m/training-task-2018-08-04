cmake_minimum_required(VERSION 3.10)
project(mediator)

set(CMAKE_CXX_STANDARD 14)

enable_testing()
find_package(GTest REQUIRED)

add_executable(mediator
  mediator.cpp
)

target_link_libraries(mediator GTest::GTest GTest::Main)
