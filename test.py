import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    obj = StudentsInMLOps()
    obj.enrollStudents(10)
    assert obj.getTotalStrength() == 10

def test_dropStudents():
    obj = StudentsInMLOps()
    obj.enrollStudents(10)
    obj.dropStudents(5)
    assert obj.getTotalStrength() == 5

def test_getClassName():
    obj = StudentsInMLOps()
    assert obj.getClassName() == "StudentsInMLOps"
