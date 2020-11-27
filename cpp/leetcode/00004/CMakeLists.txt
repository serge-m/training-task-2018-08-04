add_executable(t00004 test.cpp)
find_package(Catch2 REQUIRED)
set_target_properties(t00004 PROPERTIES LINKER_LANGUAGE CXX)
target_compile_features(t00004 PUBLIC cxx_std_17)
target_link_libraries(t00004 Catch2::Catch2)

add_test(NAME test_t00004 COMMAND t00004 -r junit)