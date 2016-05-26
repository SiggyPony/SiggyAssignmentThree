import unittest
import io
import sys

from BadSmellThree.BadSmellThreeRefactored.Main import Controller


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_checkLoadAndSaveProjects(self):
        # Setup
        self.output = io.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output
        # sys.stdout = open('file', 'w')
        self.saved_stdin = sys.stdin
        sys.stdin = open('input_loadsave', 'r')
        with open('output_loadsave', 'r') as tempTestResults:
            testresults = tempTestResults.read()
        # Test
        cmd_temp = Controller()
        cmd_temp.cmdloop()
        print("\n")
        self.assertEqual(self.output.getvalue(), testresults)
        # Teardown
        # sys.stdout.close()
        sys.stdout = self.saved_stdout
        sys.stdin.close()
        sys.stdin = self.saved_stdin

    def test_checkLoadData(self):
        # Setup
        self.output = io.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output
        # sys.stdout = open('file', 'w')
        self.saved_stdin = sys.stdin
        sys.stdin = open('input_checkloaddata', 'r')
        with open('output_checkloaddata', 'r') as tempTestResults:
            testresults = tempTestResults.read()
        # Test
        cmd_temp = Controller()
        cmd_temp.cmdloop()
        print("\n")
        self.assertEqual(self.output.getvalue(), testresults)
        # Teardown
        # sys.stdout.close()
        sys.stdout = self.saved_stdout
        sys.stdin.close()
        sys.stdin = self.saved_stdin

    def test_checkNoArguments(self):
        # Setup
        self.output = io.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output
        # sys.stdout = open('file', 'w')
        self.saved_stdin = sys.stdin
        sys.stdin = open('input_checknoparam', 'r')
        with open('output_checknoparam', 'r') as tempTestResults:
            testresults = tempTestResults.read()
        # Test
        cmd_temp = Controller()
        cmd_temp.cmdloop()
        print("\n")
        self.assertEqual(self.output.getvalue(), testresults)
        # Teardown
        # sys.stdout.close()
        sys.stdout = self.saved_stdout
        sys.stdin.close()
        sys.stdin = self.saved_stdin

if __name__ == '__main__':

    unittest.main()
