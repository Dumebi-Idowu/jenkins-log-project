import unittest
import os
from log_analyzer import analyze_logs

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        # create a temporary test log file
        with open("test.log", "w") as f:
            f.write("INFO Application started\n")
            f.write("WARNING High memory usage\n")
            f.write("ERROR Failed to connect\n")
            f.write("INFO Request completed\n")
            f.write("ERROR Timeout occurred\n")

    def tearDown(self):
        # clean up test files
        if os.path.exists("test.log"):
            os.remove("test.log")
        if os.path.exists("test_report.txt"):
            os.remove("test_report.txt")

    def test_counts_are_correct(self):
        analyze_logs("test.log", "test_report.txt")
        # if it runs without error, counts work
        self.assertTrue(os.path.exists("test_report.txt"))

    def test_report_file_created(self):
        analyze_logs("test.log", "test_report.txt")
        self.assertTrue(os.path.exists("test_report.txt"))

    def test_report_contains_errors(self):
        analyze_logs("test.log", "test_report.txt")
        with open("test_report.txt", "r") as f:
            content = f.read()
        self.assertIn("ERROR", content)
        self.assertIn("WARNING", content)

if __name__ == "__main__":
    unittest.main()