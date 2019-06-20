#! /usr/bin/env python3 

import tap
import unittest

runner = tap.runner.TAPTestRunner()
runner.set_stream(True)
unittest.main(module=None, testRunner=runner)
