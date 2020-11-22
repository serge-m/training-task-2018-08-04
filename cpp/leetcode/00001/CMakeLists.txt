add_executable(t00001 test.cpp)
find_package(Catch2 REQUIRED)
set_target_properties(t00001 PROPERTIES LINKER_LANGUAGE CXX)
target_compile_features(t00001 PUBLIC cxx_std_17)
target_link_libraries(t00001 Catch2::Catch2)

add_test(NAME test_t00001 COMMAND t00001 -r junit)