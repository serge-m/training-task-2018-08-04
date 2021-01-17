project(leetcode_sol)
cmake_minimum_required(VERSION 3.16)


if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else ()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif ()

enable_testing()

add_executable(t00002 00002/t00002.cpp)
target_compile_features(t00002 PUBLIC cxx_std_17)

add_subdirectory(00001)
add_subdirectory(00004)
add_subdirectory(00010)
add_subdirectory(00023)
add_subdirectory(00045)
add_subdirectory(00239)



