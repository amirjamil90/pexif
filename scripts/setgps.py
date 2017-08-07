#!/usr/bin/env python
from pexif import JpegFile
import sys

usage = """Usage: setgps.py filename.jpg lat lng"""

latitude = 23.432
longitude= 46.555
name=["2.jpg","amir.jpg"]
if len(sys.argv)==1:
    for i in name:        
        try:
            ef = JpegFile.fromFile(i)
            ef.set_geo(latitude,longitude)
        except IOError:
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error opening file:", value
        except JpegFile.InvalidFile:
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error opening file:", value
        try:
            ef.writeFile(i)
        except IOError:
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error saving file:", value
else:

    try:
        ef = JpegFile.fromFile(sys.argv[1])
        ef.set_geo(float(sys.argv[2]), float(sys.argv[3]))
    except IOError:
        type, value, traceback = sys.exc_info()
        print >> sys.stderr, "Error opening file:", value
    except JpegFile.InvalidFile:
        type, value, traceback = sys.exc_info()
        print >> sys.stderr, "Error opening file:", value

    try:
        ef.writeFile(sys.argv[1])
    except IOError:
        type, value, traceback = sys.exc_info()
        print >> sys.stderr, "Error saving file:", value
sys.exit(1)
