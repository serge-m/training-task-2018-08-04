cmake_minimum_required(VERSION 3.10)
project(observer)

set(CMAKE_CXX_STANDARD 14)
add_compile_options(-Wall -Wextra -pedantic -Werror)

enable_testing()
find_package(GTest REQUIRED)

add_executable(observer
        observer.cpp
        )


target_link_libraries(observer GTest::GTest GTest::Main)
