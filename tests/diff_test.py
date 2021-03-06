import unittest

from beefore import diff


class TestDiff(unittest.TestCase):

    def test_add_lines(self):
        diff_list = ["diff --git a/testfile b/()", 
                     "@@ -1,4 +1,6 @@",
                     " 1", 
                     "+2", 
                     "+3", 
                     " 4", 
                     " 5", 
                     " 6"]

        self.assertEqual(diff.positions(diff_list, "testfile"), 
                         {1:3, 2:4, 3:5, 4:6, 5:7, 6:8} )

    def test_subtract_lines(self):
        diff_list = ["diff --git a/testfile b/()", 
                     "@@ -1,6 +1,2 @@",
                     " 1", 
                     "-2", 
                     "-3", 
                     " 4"]

        self.assertEqual(diff.positions(diff_list, "testfile"), {1:3, 2:6})

    def test_add_subtract(self):
        diff_list = ["diff --git a/testfile b/()",
                     " 1",
                     "@@ -2,0 +2,1 @@",
                     "+2",
                     " 3",
                     "@@ -3,7 +4,4 @@",
                     " 4", 
                     "-5", 
                     "-6", 
                     "+7",
                     " 8",
                     "-9",
                     "+10"]

        self.assertEqual(diff.positions(diff_list, "testfile"), 
                        {2:4, 3:5, 4:7, 5:10, 6:11, 7:13})

    def test_no_change(self):
        diff_list = ["1", 
                     "2", 
                     "3", 
                     "4"]

        self.assertEqual(diff.positions(diff_list, "testfile"), None )

    def test_wrong_filename(self):
        diff_list = ["1", 
                     "2", 
                     "3", 
                     "4"]

        self.assertEqual(diff.positions(diff_list, "wrong"), None )

    def test_wrong_filename(self):
        diff_list = ["1", 
                     "2", 
                     "3", 
                     "4"]

        self.assertEqual(diff.positions(diff_list, "wrong"), None )
