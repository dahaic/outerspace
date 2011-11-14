#!/usr/bin/python

#
#  Copyright 2001 - 2011 Ludek Smid [http://www.ospace.net/]
#
#  This file is part of IGE - Outer Space.
#
#  IGE - Outer Space is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  IGE - Outer Space is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with IGE - Outer Space; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

# tweak PYTHONPATH
import sys
import os

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(basepath, "client-pygame/lib"))
sys.path.insert(0, os.path.join(basepath, "client-pygame/lib/osci"))

for item in ("libsrvr", "server/lib"):
    path = os.path.join(basepath, item)
    if os.path.exists(path):
        sys.path.insert(0, path)
        break

#configure gc
#import gc
#gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE |
#	gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)

# start application
import ai_main

# profiling
#import profile
#profile.run('import osci.main', 'profile.txt')
