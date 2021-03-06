#!/usr/bin/env python2.5

# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script runs the Mobiperf server unit tests.

Install the Python unittest2 package before you run this script.
See: http://pypi.python.org/pypi/unittest2
"""

__author__ = 'mdw@google.com (Matt Welsh)'

import optparse
import os
import sys
import unittest2


def main(sdk_path, test_path):
  # Get the appserver on the path
  sys.path.insert(0, sdk_path)
  import dev_appserver
  dev_appserver.fix_sys_path()

  # Get correct Django version
  from google.appengine.dist import use_library
  use_library('django', '1.2')

  suite = unittest2.loader.TestLoader().discover(test_path,
                                                 pattern='*_test.py')
  unittest2.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
  devapp_server_path = None
  path = os.environ['PATH'].split(':')
  for directory in path:
    dev_appserver_path = os.path.join(directory, 'dev_appserver.py')
    if os.path.exists(dev_appserver_path):
      dev_appserver_path = os.path.dirname(os.path.realpath(dev_appserver_path))
      break
  if not dev_appserver_path:
    print >>sys.stderr, 'Can\'t find dev_appserver.py on your PATH.'
    sys.exit(1)
  print 'Using appserver path ' + dev_appserver_path
  main(dev_appserver_path, 'gspeedometer')
