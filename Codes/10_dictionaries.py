# ========================================
# Dictionaries in Python - Examples (Nested Dictionaries)
# ========================================


# ========================================
# 1. Basic Dictionary Structure
# ========================================
student = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

print(student)

# Output: {'name': 'John', 'age': 20, 'city': 'New York'}


# ========================================
# 2. Access Single Value Using Key
# ========================================
student = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")

# Output:
# Name: John
# Age: 20
# City: New York


# ========================================
# 3. Accessing Nested Dictionary
# ========================================
student = {
    "personal": {
        "name": "John",
        "age": 20
    },
    "academic": {
        "grade": "A",
        "major": "Computer Science"
    }
}

print(student["personal"]["name"])
print(student["personal"]["age"])
print(student["academic"]["grade"])
print(student["academic"]["major"])

# Output:
# John
# 20
# A
# Computer Science


# ========================================
# 4.0 Basic Nested Dictionary for Students
# ========================================
students = {
    "roll_001": {
        "name": "John",
        "age": 20,
        "grade": "A"
    },
    "roll_002": {
        "name": "Alice",
        "age": 21,
        "grade": "B"
    },
    "roll_003": {
        "name": "Bob",
        "age": 19,
        "grade": "A"
    }
}

print(students)

# Output:
# {'roll_001': {'name': 'John', 'age': 20, 'grade': 'A'},
#  'roll_002': {'name': 'Alice', 'age': 21, 'grade': 'B'},
#  'roll_003': {'name': 'Bob', 'age': 19, 'grade': 'A'}}


# ========================================
# 4. Complete Student Database with Multiple Information
# ========================================
students = {
    "roll_101": {
        "name": "John Smith",
        "age": 20,
        "grade": "A",
        "course": "Computer Science",
        "cgpa": 3.8,
        "city": "New York"
    },
    "roll_102": {
        "name": "Alice Johnson",
        "age": 21,
        "grade": "B",
        "course": "Mathematics",
        "cgpa": 3.5,
        "city": "Los Angeles"
    },
    "roll_103": {
        "name": "Bob Williams",
        "age": 19,
        "grade": "A",
        "course": "Physics",
        "cgpa": 3.9,
        "city": "Chicago"
    },
    "roll_104": {
        "name": "Diana Brown",
        "age": 20,
        "grade": "C",
        "course": "Chemistry",
        "cgpa": 2.8,
        "city": "Houston"
    },
    "roll_105": {
        "name": "Charlie Davis",
        "age": 22,
        "grade": "B",
        "course": "Computer Science",
        "cgpa": 3.6,
        "city": "Phoenix"
    }
}

# Display all students
print("STUDENT DATABASE")
print("=" * 50)

for roll_no, info in students.items():
    print(f"\nRoll No: {roll_no}")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print(f"  Grade: {info['grade']}")
    print(f"  Course: {info['course']}")
    print(f"  CGPA: {info['cgpa']}")
    print(f"  City: {info['city']}")

# Output:
# STUDENT DATABASE
# ==================================================
#
# Roll No: roll_101
#   Name: John Smith
#   Age: 20
#   Grade: A
#   Course: Computer Science
#   CGPA: 3.8
#   City: New York
#
# Roll No: roll_102
#   Name: Alice Johnson
#   Age: 21
#   Grade: B
#   Course: Mathematics
#   CGPA: 3.5
#   City: Los Angeles
#
# Roll No: roll_103
#   Name: Bob Williams
#   Age: 19
#   Grade: A
#   Course: Physics
#   CGPA: 3.9
#   City: Chicago
#
# Roll No: roll_104
#   Name: Diana Brown
#   Age: 20
#   Grade: C
#   Course: Chemistry
#   CGPA: 2.8
#   City: Houston
#
# Roll No: roll_105
#   Name: Charlie Davis
#   Age: 22
#   Grade: B
#   Course: Computer Science
#   CGPA: 3.6
#   City: Phoenix


# ========================================
# 4.1 Adding New Student
# ========================================
students = {
    "roll_101": {"name": "John", "age": 20, "grade": "A"},
    "roll_102": {"name": "Alice", "age": 21, "grade": "B"}
}

print("BEFORE ADDING:")

for roll, info in students.items():
    print(f"{roll}: {info['name']}, {info['age']}, {info['grade']}")

# Add new student
students["roll_103"] = {
    "name": "Bob",
    "age": 19,
    "grade": "A"
}

print("\nAFTER ADDING:")

for roll, info in students.items():
    print(f"{roll}: {info['name']}, {info['age']}, {info['grade']}")

# Output:
# BEFORE ADDING:
# roll_101: John, 20, A
# roll_102: Alice, 21, B
#
# AFTER ADDING:
# roll_101: John, 20, A
# roll_102: Alice, 21, B
# roll_103: Bob, 19, A


# ========================================
# 4.2 Updating Student Information
# ========================================
students = {
    "roll_101": {
        "name": "John Smith",
        "age": 20,
        "grade": "B",
        "cgpa": 3.2
    }
}

print("ORIGINAL DATA:")
print(f"Name: {students['roll_101']['name']}")
print(f"Age: {students['roll_101']['age']}")
print(f"Grade: {students['roll_101']['grade']}")
print(f"CGPA: {students['roll_101']['cgpa']}")

# Update age
students["roll_101"]["age"] = 21

print("\nAFTER AGE UPDATE:")
print(f"Age: {students['roll_101']['age']}")

# Update grade
students["roll_101"]["grade"] = "A"

print("AFTER GRADE UPDATE:")
print(f"Grade: {students['roll_101']['grade']}")

# Update cgpa
students["roll_101"]["cgpa"] = 3.8

print("AFTER CGPA UPDATE:")
print(f"CGPA: {students['roll_101']['cgpa']}")

# Add new field
students["roll_101"]["city"] = "New York"

print("\nAFTER ADDING CITY:")
print(f"City: {students['roll_101']['city']}")

# Output:
# ORIGINAL DATA:
# Name: John Smith
# Age: 20
# Grade: B
# CGPA: 3.2
#
# AFTER AGE UPDATE:
# Age: 21
# AFTER GRADE UPDATE:
# Grade: A
# AFTER CGPA UPDATE:
# CGPA: 3.8
#
# AFTER ADDING CITY:
# City: New York


# ========================================
# 4.3 Deleting Student or Student Field
# ========================================
students = {
    "roll_101": {
        "name": "John",
        "age": 20,
        "grade": "A",
        "city": "New York"
    },
    "roll_102": {
        "name": "Alice",
        "age": 21,
        "grade": "B",
        "city": "Los Angeles"
    }
}

print("ORIGINAL DATABASE:")

for roll, info in students.items():
    print(f"{roll}: {info}")

# Delete a specific field from a student
del students["roll_101"]["city"]

print("\nAFTER REMOVING CITY FROM ROLL_101:")
print(f"roll_101: {students['roll_101']}")

# Delete entire student
del students["roll_102"]

print("\nAFTER DELETING ROLL_102:")

for roll, info in students.items():
    print(f"{roll}: {info}")

# Output:
# ORIGINAL DATABASE:
# roll_101: {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'New York'}
# roll_102: {'name': 'Alice', 'age': 21, 'grade': 'B', 'city': 'Los Angeles'}
#
# AFTER REMOVING CITY FROM ROLL_101:
# roll_101: {'name': 'John', 'age': 20, 'grade': 'A'}
#
# AFTER DELETING ROLL_102:
# roll_101: {'name': 'John', 'age': 20, 'grade': 'A'}


# ========================================
# 4.4 Searching Students
# ========================================
students = {
    "roll_101": {"name": "John Smith", "course": "CS", "cgpa": 3.8},
    "roll_102": {"name": "Alice Johnson", "course": "Math", "cgpa": 3.5},
    "roll_103": {"name": "Bob Williams", "course": "CS", "cgpa": 3.9},
    "roll_104": {"name": "Diana Brown", "course": "Physics", "cgpa": 2.8},
    "roll_105": {"name": "Charlie Davis", "course": "CS", "cgpa": 3.6}
}

print("STUDENT SEARCH SYSTEM")
print("=" * 40)

# Search by roll number
search_roll = "roll_103"

if search_roll in students:
    info = students[search_roll]

    print(f"\nStudent found with roll {search_roll}:")
    print(f"  Name: {info['name']}")
    print(f"  Course: {info['course']}")
    print(f"  CGPA: {info['cgpa']}")
else:
    print(f"\nRoll number {search_roll} not found!")

# Search by course (using loop)
search_course = "CS"

print(f"\nAll students in {search_course} course:")

for roll, info in students.items():
    if info['course'] == search_course:
        print(f"  {roll}: {info['name']} (CGPA: {info['cgpa']})")

# Output:
# STUDENT SEARCH SYSTEM
# ========================================
#
# Student found with roll roll_103:
#   Name: Bob Williams
#   Course: CS
#   CGPA: 3.9
#
# All students in CS course:
#   roll_101: John Smith (CGPA: 3.8)
#   roll_103: Bob Williams (CGPA: 3.9)
#   roll_105: Charlie Davis (CGPA: 3.6)


# ========================================
# Example 5: Country Data
# ========================================
countries = {
    'pakistan': {
        'capital': 'Islamabad',
        'cities': ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad'],
        'population': 241000000,
        'language': 'Urdu'
    },
    'china': {
        'capital': 'Beijing',
        'cities': ['Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen', 'Tianjin'],
        'population': 1412000000,
        'language': 'Mandarin'
    }
}

# Access specific data
print("ACCESSING SPECIFIC DATA")
print("=" * 40)

# Get capital of Pakistan
print(f"Capital of Pakistan: {countries['pakistan']['capital']}")

# Get second city of China
print(f"Second largest city in China: {countries['china']['cities'][1]}")

# Get population of Pakistan
print(f"Population of Pakistan: {countries['pakistan']['population']:,}")

# Get language of China
print(f"Language spoken in China: {countries['china']['language']}")

# Get all cities of Pakistan
print(f"\nAll cities in Pakistan:")

for city in countries['pakistan']['cities']:
    print(f"  - {city}")

# Output:
# ACCESSING SPECIFIC DATA
# ========================================
# Capital of Pakistan: Islamabad
# Second largest city in China: Beijing
# Population of Pakistan: 241,000,000
# Language spoken in China: Mandarin
#
# All cities in Pakistan:
#   - Karachi
#   - Lahore
#   - Islamabad
#   - Rawalpindi
#   - Faisalabad
