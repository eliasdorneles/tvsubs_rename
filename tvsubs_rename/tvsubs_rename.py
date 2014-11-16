#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import os
import re
import glob


def find_sub_to_rename(video_id, videofile, sub_ext):
    video_dir = os.path.dirname(os.path.realpath(videofile))
    sub_files = glob.glob('%s/*%s*%s' % (video_dir, video_id, sub_ext))
    if sub_files:
        basename, _ = os.path.splitext(videofile)
        newfilename = '%s.%s' % (basename, sub_ext)
        if newfilename not in sub_files:
            return (sub_files[0], newfilename)
        else:
            return (newfilename, None)
    return (None, None)


def run(args):
    name_patterns = [
        re.compile(r'.*(\dx\d\d).*'),
        re.compile(r'.*(s\d\de\d\d).*')
    ]
    sub_ext = args.extension
    for videofile in args.video_files:
        found = False

        for pattern in name_patterns:
            match = pattern.match(videofile)
            if not match:
                continue

            video_id = match.group(1)
            oldname, newname = find_sub_to_rename(
                video_id, videofile, sub_ext)
            if oldname:
                found = True
            if newname:
                if os.path.exists(newname):
                    print('{0} already exists, skipping...'.format(newname))
                    continue
                if not args.skip_rename:
                    os.rename(oldname, newname)
                print('{oldname} -> {newname}'.format(oldname=os.path.basename(oldname),
                                                      newname=os.path.basename(newname)))

        if not found:
            print("Could not found subs for %s" % videofile)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Script to mass-rename subtitles")
    parser.add_argument('video_files', nargs='+',
                        help='List of video files to seek subtitles for')
    parser.add_argument('-n', dest='skip_rename', action='store_true',
                        help='Just print what it will do, does NOT rename anything')
    parser.add_argument('--extension', default='srt',
                        help='Subtitle extension to use (default: srt)')
    return parser.parse_args()

if '__main__' == __name__:
    run(parse_args())
