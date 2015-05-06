#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to mass-rename subtitles"""


from __future__ import print_function
import os
import glob
import itertools
import re


NAME_PATTERNS = [
    re.compile(r'.*(?P<season>\d)x(?P<episode>\d\d).*', re.IGNORECASE),
    re.compile(r'.*s(?P<season>\d\d)e(?P<episode>\d\d).*', re.IGNORECASE)
]

SUB_EXTENSIONS = ['sub', 'srt']

VERBOSE = False


def replace_extension(filename, ext):
    ext = ext[1:] if ext[0] == '.' else ext
    basename, _ = os.path.splitext(filename)
    return '%s.%s' % (basename, ext)


def get_file_info(filename):
    for pattern in NAME_PATTERNS:
        match = pattern.match(filename)
        if match:
            return dict((k, int(v, base=10))
                        for k, v in match.groupdict().items())


def find_all_subs(dirpath):
    return itertools.chain(*[glob.glob('%s/*.%s' % (dirpath, ext))
                             for ext in SUB_EXTENSIONS])


def find_sub_for_video(videofile, file_info):
    video_dir = os.path.dirname(os.path.abspath(videofile))
    for subfile in find_all_subs(video_dir):
        sub_info = get_file_info(os.path.basename(subfile))
        if sub_info == file_info:
            return subfile


def find_existing_subtitle_for_video(videofile):
    for sub_ext in SUB_EXTENSIONS:
        sub_file = replace_extension(videofile, sub_ext)
        if os.path.exists(sub_file):
            return sub_file


def debug(mesg):
    if VERBOSE:
        print(mesg)


def find_and_rename_subtitle_for(videofile, skip_rename):
    subtitle = find_existing_subtitle_for_video(videofile)
    if subtitle:
        debug('{0} already exists, skipping...'.format(subtitle))
        return

    file_info = get_file_info(videofile)
    if not file_info:
        debug("Could not find file info for file:  %s" % videofile)
        return

    subtitle = find_sub_for_video(videofile, file_info)
    if subtitle:
        _, sub_ext = os.path.splitext(subtitle)
        newname = replace_extension(videofile, sub_ext)

        if not skip_rename:
            os.rename(subtitle, newname)

        print('{oldname} -> {newname}'.format(oldname=os.path.basename(subtitle),
                                              newname=os.path.basename(newname)))
    else:
        debug("Could not found subs for %s" % videofile)


def run(args):
    global VERBOSE
    if args.verbose:
        VERBOSE = True

    for videofile in args.video_files:
        find_and_rename_subtitle_for(videofile, skip_rename=args.skip_rename)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video_files', nargs='+',
                        help='List of video files to seek subtitles for')
    parser.add_argument('-n', '--skip-rename', action='store_true',
                        help='Just print what it will do, does NOT rename anything')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print verbose information')
    return parser.parse_args()


if '__main__' == __name__:
    run(parse_args())
