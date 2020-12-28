add_executable(00045 launcher.cpp)
target_compile_features(00045 PUBLIC cxx_std_17)


add_executable(00045_test test.cpp)
find_package(Catch2 REQUIRED)
target_compile_features(00045_test PUBLIC cxx_std_17)
target_link_libraries(00045_test Catch2::Catch2)

add_test(NAME 00045_test COMMAND 00045_test -r junit)