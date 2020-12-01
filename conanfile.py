from conans import ConanFile, CMake, tools


class AwsSdkConan(ConanFile):
    name = "aws-sdk-cpp"
    version = "1.8"
    url = "https://github.com/SechinM/conan-aws-sdk-cpp"
    description = "Conan package for aws-sdk-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "build_s3": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/aws/aws-sdk-cpp.git")

    def configure(self):
        self.options.build_s3 = True

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_UNITY_BUILD"] = "ON"
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.definitions["AUTORUN_UNIT_TESTS"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        cmake.configure(source_folder="aws-sdk-cpp")
        self.run("make -j4")
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="aws-sdk-cpp")
        self.copy("*aws-sdk-cpp.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["aws-sdk-cpp"]
