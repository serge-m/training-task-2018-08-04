add_executable(t00010 launcher.cpp)
target_compile_features(t00010 PUBLIC cxx_std_17)


add_executable(t00010_test test.cpp)
find_package(Catch2 REQUIRED)
target_compile_features(t00010_test PUBLIC cxx_std_17)
target_link_libraries(t00010_test Catch2::Catch2)

add_test(NAME t00010_test COMMAND t00010_test -r junit)