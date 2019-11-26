from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
<<<<<<< HEAD

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown" == self.test.log)

TestCaseTest("testTemplateMethod").run()
=======

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
>>>>>>> 576e2a41501bacc625db4b26decff016a0a0f192
