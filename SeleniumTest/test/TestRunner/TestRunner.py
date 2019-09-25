# test/runner.py
import unittest
# import testtools

# import your test modules
from test.Module_1 import *

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add test to the test suite
#suite.addTests(loader.loadTestsFromModule(First_Test))
suite.addTests(loader.loadTestsFromTestCase(Scenario1))
suite.addTests(loader.loadTestsFromTestCase(Scenario2))
suite.addTests(loader.loadTestsFromTestCase(Scenario3))
suite.addTests(loader.loadTestsFromTestCase(Scenario4))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=1)

result = runner.run(suite)

# Parallel Execution
# concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
# concurrent_suite.run(testtools.StreamResult())