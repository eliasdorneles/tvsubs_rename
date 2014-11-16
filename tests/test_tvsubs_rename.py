#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tvsubs_rename
----------------------------------

Tests for `tvsubs_rename` module.
"""

import unittest
import tempfile
import shutil
import os
import glob
from tvsubs_rename import tvsubs_rename
from collections import namedtuple


ScriptArgs = namedtuple('ScriptArgs', 'video_files skip_rename extension')


def create_file(filepath):
    open(filepath, 'w').close()


class TestTvSubsRenameEndToEnd(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def test_simple_rename(self):
        # setup:
        create_file(os.path.join(self.tempdir, 'ep-s01e01.avi'))
        create_file(os.path.join(self.tempdir, 'ep-s01e02.avi'))
        create_file(os.path.join(self.tempdir, 'my-crazy-sub-s01e01.srt'))
        create_file(os.path.join(self.tempdir, 'another-crazy-sub-s01e02.srt'))
        # when:
        tvsubs_rename.run(
            ScriptArgs(
                video_files=glob.glob(os.path.join(self.tempdir, '*.avi')),
                skip_rename=False,
                extension='srt'))
        # then:
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e01.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e02.srt')))

    def tearDown(self):
        shutil.rmtree(self.tempdir)

if __name__ == '__main__':
    unittest.main()
