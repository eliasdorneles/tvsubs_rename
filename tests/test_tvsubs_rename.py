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


ScriptArgs = namedtuple('ScriptArgs', 'video_files skip_rename extension verbose')


def create_file(filepath):
    open(filepath, 'w').close()


class TvSubsRenameEndToEndTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def test_simple_rename(self):
        # setup:
        create_file(os.path.join(self.tempdir, 'ep-s01e01.avi'))
        create_file(os.path.join(self.tempdir, 'ep-s01e02.avi'))
        create_file(os.path.join(self.tempdir, 'my-crazy-sub-s01e01.srt'))
        create_file(os.path.join(self.tempdir, 'another-crazy-sub-s01e02.srt'))
        # when:
        args = ScriptArgs(video_files=glob.glob(os.path.join(self.tempdir, '*.avi')),
                          skip_rename=False,
                          verbose=False,
                          extension='srt')
        tvsubs_rename.run(args)
        # then:
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e01.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e02.srt')))

    def test_rename_considering_different_patterns(self):
        # setup:
        create_file(os.path.join(self.tempdir, 'ep-s01e01.avi'))
        create_file(os.path.join(self.tempdir, 'ep-s01e02.avi'))
        create_file(os.path.join(self.tempdir, 'my-crazy-sub-s01e01.srt'))
        create_file(os.path.join(self.tempdir, 'another-crazy-sub-1x02.sub'))
        # when:
        args = ScriptArgs(video_files=glob.glob(os.path.join(self.tempdir, '*.avi')),
                          skip_rename=False,
                          verbose=False,
                          extension='srt')
        tvsubs_rename.run(args)
        # then:
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e01.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'ep-s01e02.sub')))

    def tearDown(self):
        shutil.rmtree(self.tempdir)


class UtilsTest(unittest.TestCase):
    def test_replace_extension(self):
        self.assertEquals('file.srt', tvsubs_rename.replace_extension('file.avi', 'srt'))
        self.assertEquals('file.srt', tvsubs_rename.replace_extension('file.avi', '.srt'))


if __name__ == '__main__':
    unittest.main()
