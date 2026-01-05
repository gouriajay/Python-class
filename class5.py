
python_students = {"Anu", "Ravi", "Meera"}
data_science_students = {"Ravi", "Kiran", "Sneha"}


python_students.add("Arjun")


data_science_students.remove("Sneha")


both_courses = python_students.intersection(data_science_students)


only_python = python_students.difference(data_science_students)


all_students = python_students.union(data_science_students)


course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_counts.items()}


print( python_students)
print( data_science_students)
print( both_courses)
print( only_python)
print( all_students)
print( expected_growth)
