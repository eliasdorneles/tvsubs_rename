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


This will look for subtitle files for every .avi file in current directory,
matching episode according to commonly used patterns in filename
(like ``s01e02`` or ``1x02`` to indicate second episode of season 1) and will
rename it to match the video filename.
