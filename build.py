from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86_64',
        'build_type': 'Release'})
    builder.run()