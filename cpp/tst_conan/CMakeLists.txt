cmake_minimum_required(VERSION 2.8.12)
project(tst_conan)

set(CMAKE_CXX_STANDARD 17)

if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else ()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif ()

enable_testing()


# Initial example with poco dependency
add_subdirectory(app_with_external_dependency)

# example of a library with tests and a client app
add_subdirectory(lib)

add_executable(app app/app.cpp)
target_link_libraries(app func_lib)
target_include_directories(app PRIVATE ${CMAKE_SOURCE_DIR}/lib)

add_subdirectory(tests)
