add_executable(catch2_test maintest.cpp catch2_test.cpp)
find_package(Catch2 REQUIRED)
target_link_libraries(catch2_test func_lib Catch2::Catch2)
target_include_directories(catch2_test PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_SOURCE_DIR}/lib)

add_test(NAME catch2_test
        COMMAND cache_test -r junit)