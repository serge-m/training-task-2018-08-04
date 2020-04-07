cmake_minimum_required(VERSION 3.10)
project(memento)

set(CMAKE_CXX_STANDARD 14)
add_compile_options(-Wall -Wextra -pedantic -Werror)

enable_testing()
find_package(GTest REQUIRED)

add_executable(memento
  memento.cpp
)


target_link_libraries(memento)
