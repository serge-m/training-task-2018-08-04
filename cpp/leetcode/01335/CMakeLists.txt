set(CUR_DIR ${CMAKE_CURRENT_SOURCE_DIR})
get_filename_component(NAME ${CUR_DIR} NAME)
add_executable(${NAME} solution.cpp)
target_compile_features(${NAME} PUBLIC cxx_std_17)
