# Example of using Conan

## Set profile
    
    conan profile new default --detect  # Generates default profile detecting GCC and sets old ABI
    conan profile update settings.compiler.libcxx=libstdc++11 default  # Sets libcxx to C++11 ABI

## Install dependencies using Conan

    conan install . -s build_type=Debug --install-folder=cmake-build-debug
    conan install . -s build_type=Release --install-folder=cmake-build-release
    
## CMake etc.
    
    cd cmake-build-debug
    cmake ..
    cmake --build . --config Debug
   
    