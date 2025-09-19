import argparse
import sys
import csv
from module import Student
from tabulate import tabulate

def parse_args(args):
    parser = argparse.ArgumentParser(description="Пример использования argparse")
    parser.add_argument("--files", nargs="*", help="Список файлов для обработки")
    parser.add_argument("--report", help="Отчет")
    return parser.parse_args(sys.argv[1:])

def get_rows(files):
    rows = []
    for file in files:
        with open(file,encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader) 
            for row in reader:
                rows.append(row) 
    return rows

def get_students(rows):
    studentsDict = {}
    for row in rows:
        if not row[0] in studentsDict:
            studentsDict[row[0]] = Student(row[0], [int(row[-1])])
        else:
            studentsDict[row[0]].addGrade(int(row[-1]))
    return studentsDict
    
def write_to_csv(filename,rows):
    studentGradePairs = {}
    field = ["student_name", "grade"]

    for key in rows:
        studentGradePairs[key] = rows[key].calculate_average()
    sortedStudentGradePairs = dict(sorted(studentGradePairs.items(), key=lambda item: item[1], reverse=True))
    
    print(tabulate([(k, v) for k, v in sortedStudentGradePairs.items()], tablefmt="grid", headers=field))
    with open(f'{filename}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(field)
        for key in sortedStudentGradePairs:
            writer.writerow([key, sortedStudentGradePairs[key]])

def main():
    
    args = parse_args(sys.argv)
    rows = get_rows(args.files)
    students = get_students(rows)
    write_to_csv(args.report,students)

if __name__ == "__main__":
    main()