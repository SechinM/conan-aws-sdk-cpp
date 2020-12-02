from conans import ConanFile, CMake, tools


class AwsSdkConan(ConanFile):
    name = "aws-sdk-cpp"
    version = "1.8.82"
    url = "https://github.com/SechinM/conan-aws-sdk-cpp"
    description = "Conan package for aws-sdk-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "build_access_management": [True, False], "build_acm": [True, False],
               "build_amplify": [True, False], "build_apigateway": [True, False], "build_appstream": [True, False],
               "build_cloudformation": [True, False], "build_cloudfront": [True, False], "build_codebuild": [True, False],
               "build_codecommit": [True, False], "build_codedeploy": [True, False], "build_codepipeline": [True, False],
               "build_cognito_identity": [True, False], "build_cognito_idp": [True, False],
               "build_cognito_sync": [True, False], "build_config": [True, False], "build_dynamodb": [True, False],
               "build_dynamodbstreams": [True, False], "build_ec2": [True, False], "build_ecr": [True, False],
               "build_ecs": [True, False], "build_eks": [True, False], "build_email": [True, False],
               "build_events": [True, False], "build_iam": [True, False], "build_identity_management": [True, False],
               "build_kafka": [True, False], "build_lambda": [True, False], "build_logs": [True, False],
               "build_machinelearnings": [True, False], "build_polly": [True, False], "build_pricing": [True, False],
               "build_queues": [True, False], "build_quicksight": [True, False], "build_ram": [True, False],
               "build_rds": [True, False], "build_resource_groups": [True, False], "build_route53": [True, False],
               "build_route53domains": [True, False], "build_s3": [True, False], "build_sagemaker": [True, False],
               "build_sdb": [True, False], "build_secretsmanager": [True, False], "build_serverlessrepo": [True, False],
               "build_servicecatalog": [True, False], "build_servicediscovery": [True, False],
               "build_shield": [True, False], "build_signer": [True, False], "build_sms": [True, False],
               "build_sns": [True, False], "build_storagegateway": [True, False], "build_support": [True, False],
               "build_transfer": [True, False], "build_translate": [True, False], "build_waf": [True, False],
               "build_workdocs": [True, False], "build_workmail": [True, False], "build_worklink": [True, False],
               "build_workspaces": [True, False], "build_xray": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    build_requires = "zlib/1.2.11", "libcurl/7.71.1"

    def configure(self):
        self.options.build_access_management = True
        self.options.build_acm = True
        self.options.build_amplify = True
        self.options.build_apigateway = True
        self.options.build_appstream = True
        self.options.build_cloudformation = True
        self.options.build_cloudfront = True
        self.options.build_codebuild = True
        self.options.build_codecommit = True
        self.options.build_codedeploy = True
        self.options.build_codepipeline = True
        self.options.build_cognito_identity = True
        self.options.build_cognito_idp = True
        self.options.build_cognito_sync = True
        self.options.build_config = True
        self.options.build_dynamodb = True
        self.options.build_dynamodbstreams = True
        self.options.build_ec2 = True
        self.options.build_ecr = True
        self.options.build_ecs = True
        self.options.build_eks = True
        self.options.build_email = True
        self.options.build_events = True
        self.options.build_iam = True
        self.options.build_identity_management = True
        self.options.build_kafka = True
        self.options.build_lambda = True
        self.options.build_logs = True
        self.options.build_machinelearnings = True
        self.options.build_polly = True
        self.options.build_pricing = True
        self.options.build_queues = True
        self.options.build_quicksight = True
        self.options.build_ram = True
        self.options.build_rds = True
        self.options.build_resource_groups = True
        self.options.build_route53 = True
        self.options.build_route53domains = True
        self.options.build_s3 = True
        self.options.build_sagemaker = True
        self.options.build_sdb = True
        self.options.build_secretsmanager = True
        self.options.build_serverlessrepo = True
        self.options.build_servicecatalog = True
        self.options.build_servicediscovery = True
        self.options.build_shield = True
        self.options.build_signer = True
        self.options.build_sms = True
        self.options.build_sns = True
        self.options.build_storagegateway = True
        self.options.build_support = True
        self.options.build_transfer = True
        self.options.build_translate = True
        self.options.build_waf = True
        self.options.build_workdocs = True
        self.options.build_workmail = True
        self.options.build_worklink = True
        self.options.build_workspaces = True
        self.options.build_xray = True 

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
