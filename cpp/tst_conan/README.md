# Example of using Conan


## Installing 

Set profile
    
    conan profile new default --detect  # Generates default profile detecting GCC and sets old ABI
    conan profile update settings.compiler.libcxx=libstdc++11 default  # Sets libcxx to C++11 ABI

Install dependencies using Conan

    conan install . -s build_type=Debug --install-folder=cmake-build-debug
    conan install . -s build_type=Release --install-folder=cmake-build-release
    
CMake etc.
    
    cd cmake-build-debug
    cmake ..
    cmake --build . --config Debug
   
## More info about conan

* [https://docs.conan.io/en/latest/getting_started.html](https://docs.conan.io/en/latest/getting_started.html)
* [https://docs.conan.io/en/latest/integrations/ide/clion.html](https://docs.conan.io/en/latest/integrations/ide/clion.html)
* [https://blog.jetbrains.com/clion/2019/05/getting-started-with-the-conan-clion-plugin/](https://blog.jetbrains.com/clion/2019/05/getting-started-with-the-conan-clion-plugin/)

## See also

* inspired by [example-catch2-conan](https://github.com/jw3/example-catch2-conan)