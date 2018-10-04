from conans import ConanFile, CMake

class CMakeServerConan(ConanFile):
    name = "wg21"
    version = "1.0"
    requires = "uselatex/2.4.9@mmha/stable"
    generators = "cmake_paths"
    no_copy_source = True
    exports_sources = "*", "!build/*", "!.git/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()
        cmake.install()
