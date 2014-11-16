===============================
TV Subs Rename
===============================

.. image:: https://badge.fury.io/py/tvsubs_rename.png
    :target: http://badge.fury.io/py/tvsubs_rename

.. image:: https://travis-ci.org/eliasdorneles/tvsubs_rename.png?branch=master
        :target: https://travis-ci.org/eliasdorneles/tvsubs_rename

.. image:: https://pypip.in/d/tvsubs_rename/badge.png
        :target: https://pypi.python.org/pypi/tvsubs_rename


Script for mass-renaming TV subtitles for a given set of video files

* Free software: BSD license
* Documentation: https://tvsubs_rename.readthedocs.org.

Usage
-----

::

    tvsubs_rename *.avi


This will look for subtitle files matching the episode numbers for all the \*.avi
files in current directory and rename them to match the video filenames.


How it works
------------

It matches episode filenames looking for commonly used patterns in TV-series
episode files (like ``s01e02`` or ``1x02`` to indicate second episode of season 1)
and will rename it to match the video filename.
