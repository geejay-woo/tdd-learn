from TestCase import TestCase


class WasRun(TestCase):

    def __init__(self, name) -> None:
        self.log = None
        TestCase.__init__(self, name)

    def testBrokenMethod(self):
        raise Exception

    def testMethod(self):
        self.log = self.log+"testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

