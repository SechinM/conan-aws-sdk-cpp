from conans import ConanFile, CMake, tools


class AwsSdkConan(ConanFile):
    name = "aws-sdk-cpp"
    version = "1.8.82"
    url = "https://github.com/SechinM/conan-aws-sdk-cpp"
    description = "Conan package for aws-sdk-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "build_s3": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    build_requires = "zlib/1.2.11", "libcurl/7.71.1"

    def configure(self):
        self.options.build_s3 = True

    def source(self):
        self.run("curl -sSL https://github.com/aws/aws-sdk-cpp/archive/" + self.version + ".tar.gz > aws-sdk-cpp.tar.gz")
        self.run("tar xf aws-sdk-cpp.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_UNITY_BUILD"] = "ON"
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.definitions["AUTORUN_UNIT_TESTS"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        cmake.configure(source_folder=self.name + "-" + self.version)
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

