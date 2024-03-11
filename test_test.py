import unittest
from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):
    def setUp(self):
        # Create an instance of the StudentsInMLOps class
        self.students = StudentsInMLOps()

    def test_enrollStudents(self):
        # Test the enrollStudents function
        self.students.enrollStudents(5)
        self.assertEqual(self.students.getTotalStrength(), 5)

    def test_dropStudents(self):
        # Test the dropStudents function
        self.students.enrollStudents(10)
        self.students.dropStudents(3)
        self.assertEqual(self.students.getTotalStrength(), 7)

    def test_getTotalStrength(self):
        # Test the getTotalStrength function
        self.students.enrollStudents(8)
        self.assertEqual(self.students.getTotalStrength(), 8)

    def test_getClassName(self):
        # Test the getClassName function
        self.assertEqual(self.students.getClassName(), "StudentsInMLOps")

if __name__ == '__main__':
    unittest.main()