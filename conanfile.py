#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class FrozenConan(ConanFile):
    name = "frozen"
    version = "20181020"
    description = "A header-only, constexpr alternative to gperf for C++14 users."
    homepage = "https://github.com/serge-sans-paille/frozen"
    url = "https://github.com/bincrafters/conan-frozen"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "Apache-2.0"
    exports = ["LICENSE.md"]
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    _commit_id = "5d59c0ad8a9358ce537c39dff3728dace5e1f00e"

    def source(self):
        tools.get("{0}/archive/{1}.zip".format(self.homepage, self._commit_id))
        extracted_dir = "frozen-" + self._commit_id
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
