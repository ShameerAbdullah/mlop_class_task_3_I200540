from main import StudentsInMLOps

def test_enrollStudents():
    obj = StudentsInMLOps()
    obj.enrollStudents(5)
    assert obj.getTotalStrength() == 5

def test_dropStudents():
    obj = StudentsInMLOps()
    obj.enrollStudents(10)
    obj.dropStudents(3)
    assert obj.getTotalStrength() == 7
