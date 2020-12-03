add_executable(00023 launcher.cpp)
target_compile_features(00023 PUBLIC cxx_std_17)


add_executable(00023_test test.cpp)
find_package(Catch2 REQUIRED)
target_compile_features(00023_test PUBLIC cxx_std_17)
target_link_libraries(00023_test Catch2::Catch2)

add_test(NAME 00023_test COMMAND 00023_test -r junit)