import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    ml_class = StudentsInMLOps()
    ml_class.enrollStudents(5)
    assert ml_class.getTotalStrength() == 5

def test_dropStudents():
    ml_class = StudentsInMLOps()
    ml_class.enrollStudents(10)
    ml_class.dropStudents(3)
    assert ml_class.getTotalStrength() == 7
