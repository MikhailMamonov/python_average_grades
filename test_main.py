import pytest
import csv
from module import Student
from main import *


def test_init_Success():
    grades = [5,4,3]
    student = Student("Test Testov", grades)
    assert student.student_name == "Test Testov"
    assert student.grades == grades

def test_init_Fail():
    grades = [5,4,'3']
    with pytest.raises(TypeError):
        student = Student("Test Testov", grades)


def test_addGrade_Success():
    grades = [5,4,3]
    expected = [5,4,3,3]

    student = Student("Test Testov", grades)
    student.addGrade(3)
    assert grades == expected

def test_addGrade_Fail():
    grades = [5,4,3]

    student = Student("Test Testov", grades)
    with pytest.raises(TypeError):
        student.addGrade('3')
        
def test_calculateAverage_Success():
    grades = [5,4,3]
    expected = 4

    student = Student("Test Testov", grades)
    assert student.calculate_average() == expected

def test_calculateAverage_emptyList():
    expected = 0
    student = Student("Test Testov")
    assert student.calculate_average() == expected

def test_getStudents_Success():
    expected_student_len = 2

    rows = [
            ['Белов Станислав', 'Алгебра', 'Белова Светлана', '2023-10-18', '5'],
            ['Морозов Петр', 'Литература', 'Белова Светлана', '2023-10-18', '3']
            ]
    students = get_students(rows)
    assert len(students) == expected_student_len
    assert 'Белов Станислав' in students
    assert 'Морозов Петр' in students

def test_getStudents_similarStudentName():
    expected_len = 2
    rows = [
        ['Белов Станислав', 'Литература', 'Белова Светлана', '2023-10-18', '4'],
        ['Белов Станислав', 'Алгебра', 'Белова Светлана', '2023-10-18', '5'],
        ['Морозов Петр', 'Литература', 'Белова Светлана', '2023-10-18', '3']
            ]
    students = get_students(rows)
    assert len(students) == expected_len
    assert len(students['Белов Станислав'].grades) ==expected_len


def test_getRows_Success():
    files =[ 'students1.csv', 'students2.csv']
    rows = get_rows(files)

    assert len(rows)>0

def test_getRows_fail_FileNotFound():
    files =[ 'students.csv']

    with pytest.raises(FileNotFoundError):
        rows = get_rows(files)

def test_parseArgs_Success():
    args = ['main.py', '--files', 'students1.csv', 'students2.csv', '--report', 'student-performance']
    parsed_args = parse_args(args)
    assert len(parsed_args.files) ==2
    assert parsed_args.report == 'student-performance'

def test_parseArgs_fail_argumentError():
    args = ['main.py', '--files', 'students1.csv', 'students2.csv', '--report']
    with pytest.raises(Exception):
        parsed_args = parse_args(args)

def test_write_to_csv_Success():
    rows = {'Белов Станислав': Student('Белов Станислав', [5,4]),
             'Морозов Петр': Student('Морозов Петр', [3, 4])}
    filename = 'student_performance'
    expected_count = sum(1 for line in rows)+1

    write_to_csv(filename,rows)
    with open(f'{filename}.csv') as f:
        file_line_count=sum(1 for line in f)
        assert file_line_count == expected_count


