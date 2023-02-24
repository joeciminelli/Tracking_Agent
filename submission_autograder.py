#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
