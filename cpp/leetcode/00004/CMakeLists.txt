add_executable(t00004 launcher.cpp)
target_compile_features(t00004 PUBLIC cxx_std_17)


add_executable(t00004_test test.cpp)
find_package(Catch2 REQUIRED)
target_compile_features(t00004_test PUBLIC cxx_std_17)
target_link_libraries(t00004_test Catch2::Catch2)

add_test(NAME t00004_test COMMAND t00004_test -r junit)