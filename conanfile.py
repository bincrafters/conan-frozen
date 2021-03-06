import os
from conans import ConanFile, CMake, tools


class FrozenConan(ConanFile):
    name = "frozen"
    version = "20181020"
    description = "A header-only, constexpr alternative to gperf for C++14 users."
    homepage = "https://github.com/serge-sans-paille/frozen"
    url = "https://github.com/bincrafters/conan-frozen"
    license = "Apache-2.0"
    exports_sources = ("CMakeLists.txt", "frozen.patch")
    generators = "cmake"
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    _commit_id = "5d59c0ad8a9358ce537c39dff3728dace5e1f00e"

    def source(self):
        tools.get("{0}/archive/{1}.zip".format(self.homepage, self._commit_id))
        extracted_dir = "frozen-" + self._commit_id
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = CMake(self)
        cmake.configure()
        # write_basic_package_version_file is not portable on Windows
        tools.replace_in_file(file_path=os.path.join(self.build_folder, self._source_subfolder, "frozenConfigVersion.cmake"),
                              search='# check that the installed version has the same',
                              replace="return() #")
        cmake.install()

    def package_id(self):
        self.info.header_only()
