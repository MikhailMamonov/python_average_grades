import pytest
from module import Student


def test_addGradeSuccess():
    grades = [5,4,3]
    expected = [5,4,3,3]

    student = Student("test", grades)
    student.addGrade(3)
    assert grades == expected

def test_addGradeSuccess():
    grades = [5,4,3]
    expected = [5,4,3,3]

    student = Student("test", grades)
    student.addGrade(3)
    assert grades == expected

def test_calculateAverageSuccess():
    grades = [5,4,3]
    expectedResult = 4

    student = Student("test", grades)
    assert student.calculate_average() == expectedResult