// sample from
// https://blog.jetbrains.com/clion/2019/05/getting-started-with-the-conan-clion-plugin/
#include "Poco/MD5Engine.h"
#include "Poco/DigestStream.h"
#include <iostream>
int main(int argc, char** argv)
{
    Poco::MD5Engine md5;
    Poco::DigestOutputStream ds(md5);
    ds << "123123123";
    ds.close();
    std::cout << Poco::DigestEngine::digestToHex(md5.digest()) << std::endl;
    return 0;
}