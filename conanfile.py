from conans import ConanFile, CMake, tools

class AwsSdkConan(ConanFile):
    name = "aws-sdk-cpp"
    version = "1.8.82"
    license = "Apache 2.0"
    url = "https://github.com/SechinM/conan-aws-sdk-cpp"
    description = "Conan package for aws-sdk-cpp"
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"
    options = {"shared": [True, False], "build_s3": [True, False], "build_apigateway": [True, False],
               "build_core": [True, False], "build_cognito_identity": [True, False], "build_cognito_idp": [True, False],
               "build_cognito_sync": [True, False],  "build_email": [True, False], "build_events": [True, False],
               "build_iam": [True, False], "build_identity_management": [True, False], "build_lambda": [True, False],
               "build_logs": [True, False], "build_rds": [True, False], "build_secretsmanager": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "zlib/1.2.11"

#    def build_requirements(self):
#        if self.settings.os != "Macos":
#            self.requires("openssl/1.1.1h")
#        self.build_requires("libcurl/7.71.1")

    def source(self):
        tools.download("https://github.com/aws/aws-sdk-cpp/archive/%s.tar.gz" % self.version, "aws-sdk-cpp.tar.gz")
        tools.unzip("aws-sdk-cpp.tar.gz")

    def configure(self):
        self.options.build_apigateway = True
        self.options.build_core = True
        self.options.build_cognito_identity = True
        self.options.build_cognito_idp = True
        self.options.build_cognito_sync = True
        self.options.build_email = True
        self.options.build_events = True
        self.options.build_iam = True
        self.options.build_identity_management = True
        self.options.build_lambda = True
        self.options.build_logs = True
        self.options.build_rds = True
        self.options.build_s3 = True
        self.options.build_secretsmanager = True

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_ONLY"] = "core"
        cmake.definitions["ENABLE_UNITY_BUILD"] = "ON"
        cmake.definitions["ENABLE_TESTING"] = "OFF"
        cmake.definitions["AUTORUN_UNIT_TESTS"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        cmake.configure(source_folder=self.name + "-" + self.version)
#        cmake.configure(source_folder="%s/aws-sdk-cpp-%s" % (self.source_folder, self.version), build_folder=self.build_folder)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install(build_dir=self.build_folder)

    def package(self):
        self.copy("*.h", dst="include", src=self.name + "-" + self.version + "/aws-cpp-sdk-core/include")
        self.copy("*aws-sdk-cpp*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = tools.collect_libs(self)
