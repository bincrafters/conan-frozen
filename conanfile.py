#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class FrozenConan(ConanFile):
    name = "frozen"
    version = "20181020"
    description = "A header-only, constexpr alternative to gperf for C++14 users."
    url = "https://github.com/serge-sans-paille/frozen"
    license = "Apache-2.0"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    _commit_id = "5d59c0ad8a9358ce537c39dff3728dace5e1f00e"

    def source(self):
        source_url = "https://github.com/serge-sans-paille/frozen"
        tools.get("{0}/archive/{1}.zip".format(source_url, self._commit_id))
        extracted_dir = "frozen-" + self._commit_id
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
