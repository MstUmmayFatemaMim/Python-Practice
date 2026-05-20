############3       Build a mini student management system using list + dict.
students = [
    {"name": "Mim",   "age": 20, "grade": 85},
    {"name": "Rahim", "age": 22, "grade": 72},
    {"name": "Karim", "age": 21, "grade": 90},
    {"name": "Sana",  "age": 23, "grade": 65},
]

# Add student
def add_student(name, age, grade):
    for s in students:                          # O(n) — check duplicate
        if s["name"].lower() == name.lower():
            print(f"'{name}' already exists!")
            return
    students.append({"name": name,             # O(1) — append
                     "age": age,
                     "grade": grade})
    print(f" '{name}' added successfully.")

# Remove student
def remove_student(name):
    for i, s in enumerate(students):           # O(n)
        if s["name"].lower() == name.lower():
            students.pop(i)                    # O(n) — shifts elements
            print(f" '{name}' removed.")
            return
    print(f"'{name}' not found!")

# Search student
def search_student(name):
    for s in students:                         # O(n)
        if s["name"].lower() == name.lower():
            print(f"\nFound: {s}")
            return
    print(f"'{name}' not found!")

# Show all
def show_all():
    print("\n===== Student List =====")
    print(f"{'Name':<12} {'Age':>5} {'Grade':>7}")
    print("-" * 26)
    for s in students:                         # O(n)
        print(f"{s['name']:<12} {s['age']:>5} {s['grade']:>7}")

# Average grade
def average_grade():
    total = sum(s["grade"] for s in students)  # O(n)
    return total / len(students)

# ---- Test ----
add_student("Rafi", 21, 78)
remove_student("Sana")
search_student("Karim")
show_all()
print(f"\nAverage Grade: {average_grade():.1f}")

# ##########      Way 2 — Dictionary of Dictionaries (faster search)
# # name → key for O(1) lookup
# students = {
#     "Mim":   {"age": 20, "grade": 85},
#     "Rahim": {"age": 22, "grade": 72},
#     "Karim": {"age": 21, "grade": 90},
#     "Sana":  {"age": 23, "grade": 65},
# }
#
# def add_student(name, age, grade):
#     if name in students:                        # O(1) — dict lookup
#         print(f"'{name}' already exists!")
#         return
#     students[name] = {"age": age,              # O(1)
#                       "grade": grade}
#     print(f"✅ '{name}' added.")
#
# def remove_student(name):
#     if name in students:                        # O(1)
#         del students[name]                      # O(1)
#         print(f"🗑️ '{name}' removed.")
#     else:
#         print(f"'{name}' not found!")
#
# def update_student(name, age=None, grade=None):
#     if name not in students:                    # O(1)
#         print(f"'{name}' not found!")
#         return
#     if age:
#         students[name]["age"]   = age           # O(1)
#     if grade:
#         students[name]["grade"] = grade         # O(1)
#     print(f"✅ '{name}' updated: {students[name]}")
#
# def search_student(name):
#     if name in students:                        # O(1) ⚡
#         info = students[name]
#         print(f"\n🔍 {name} → Age: {info['age']}, Grade: {info['grade']}")
#     else:
#         print(f"'{name}' not found!")
#
# def show_all():
#     print("\n===== Student List =====")
#     print(f"{'Name':<12} {'Age':>5} {'Grade':>7}")
#     print("-" * 26)
#     for name, info in students.items():         # O(n)
#         print(f"{name:<12} {info['age']:>5} {info['grade']:>7}")
#
# def average_grade():
#     total = sum(info["grade"]
#                 for info in students.values())  # O(n)
#     return total / len(students)
#
# def top_student():
#     name = max(students,
#                key=lambda k: students[k]["grade"])  # O(n)
#     print(f"\n🏆 Top Student: {name} → {students[name]['grade']}")
#
# def bottom_student():
#     name = min(students,
#                key=lambda k: students[k]["grade"])  # O(n)
#     print(f"\n⚠️ Lowest: {name} → {students[name]['grade']}")
#
# # ---- Test ----
# add_student("Rafi", 21, 78)
# update_student("Mim", grade=92)
# search_student("Karim")
# show_all()
# top_student()
# bottom_student()
# print(f"\nAverage: {average_grade():.1f}")


# ###########     Way 3 — With subject wise grades (nested structure)
# students = {
#     "Mim": {
#         "age": 20,
#         "grades": {"Math": 85, "English": 90, "Science": 78}
#     },
#     "Rahim": {
#         "age": 22,
#         "grades": {"Math": 72, "English": 68, "Science": 80}
#     },
#     "Karim": {
#         "age": 21,
#         "grades": {"Math": 90, "English": 85, "Science": 92}
#     },
# }
#
# def add_student(name, age, grades):
#     if name in students:                            # O(1)
#         print(f"'{name}' already exists!")
#         return
#     students[name] = {"age": age, "grades": grades}# O(1)
#     print(f"✅ '{name}' added.")
#
# def student_average(name):
#     if name not in students:                        # O(1)
#         print(f"'{name}' not found!")
#         return
#     grades = students[name]["grades"]
#     avg    = sum(grades.values()) / len(grades)     # O(s) s=subjects
#     return avg
#
# def add_subject_grade(name, subject, grade):
#     if name not in students:                        # O(1)
#         print(f"'{name}' not found!")
#         return
#     students[name]["grades"][subject] = grade       # O(1)
#     print(f"✅ '{subject}': {grade} added for '{name}'.")
#
# def show_all():
#     print("\n========= Student Report =========")
#     for name, info in students.items():             # O(n*s)
#         avg = student_average(name)
#         print(f"\n👤 {name} (Age: {info['age']})")
#         print(f"   {'Subject':<12} {'Grade':>6}")
#         print(f"   {'-'*20}")
#         for subject, grade in info["grades"].items():
#             print(f"   {subject:<12} {grade:>6}")
#         print(f"   {'Average':<12} {avg:>6.1f}")
#
# def class_topper():
#     topper = max(students,
#                  key=lambda k: student_average(k)) # O(n*s)
#     avg = student_average(topper)
#     print(f"\n🏆 Class Topper: {topper} → Avg: {avg:.1f}")
#
# def subject_topper(subject):
#     best = max(students,
#                key=lambda k: students[k]["grades"].get(subject, 0))  # O(n)
#     score = students[best]["grades"].get(subject, 0)
#     print(f"\n🥇 {subject} Topper: {best} → {score}")
#
# # ---- Test ----
# add_student("Sana", 23, {"Math": 95, "English": 88, "Science": 91})
# add_subject_grade("Mim", "History", 82)
# show_all()
# class_topper()
# subject_topper("Math")

# ########        Way 4 — Full system with menu + history + grades (real project)
# from collections import defaultdict
#
# students  = {}
# history   = []
#
# def add_student(name, age, grade):
#     if name in students:                        # O(1)
#         print(f"'{name}' already exists!")
#         return
#     students[name] = {"age": age,
#                       "grade": grade,
#                       "status": "Active"}       # O(1)
#     history.append(f"ADDED   → {name}")
#     print(f"✅ '{name}' added.")
#
# def remove_student(name):
#     if name not in students:                    # O(1)
#         print(f"'{name}' not found!")
#         return
#     students.pop(name)                          # O(1)
#     history.append(f"REMOVED → {name}")
#     print(f"🗑️ '{name}' removed.")
#
# def update_student(name, age=None, grade=None):
#     if name not in students:                    # O(1)
#         print(f"'{name}' not found!")
#         return
#     if age:
#         students[name]["age"]   = age           # O(1)
#     if grade is not None:
#         students[name]["grade"] = grade         # O(1)
#     history.append(f"UPDATED → {name}")
#     print(f"✅ '{name}' updated.")
#
# def search_student(name):
#     match = {k: v for k, v in students.items() # O(n) — partial match
#              if name.lower() in k.lower()}
#     if match:
#         print(f"\n🔍 Search results for '{name}':")
#         for n, info in match.items():
#             print(f"   {n} → Age:{info['age']} "
#                   f"Grade:{info['grade']} "
#                   f"Status:{info['status']}")
#     else:
#         print(f"No match found for '{name}'.")
#
# def assign_letter_grade(grade):                 # O(1)
#     if grade >= 90: return "A+"
#     elif grade >= 80: return "A"
#     elif grade >= 70: return "B"
#     elif grade >= 60: return "C"
#     elif grade >= 50: return "D"
#     else: return "F"
#
# def show_all():
#     if not students:
#         print("No students!")
#         return
#
#     sorted_students = sorted(students.items(),
#                              key=lambda x: x[1]["grade"],
#                              reverse=True)      # O(n log n)
#     total = sum(info["grade"]
#                 for info in students.values())  # O(n)
#     avg   = total / len(students)
#
#     print("\n=========== Student Management System ===========")
#     print(f"{'Rank':<6}{'Name':<12}{'Age':>5}"
#           f"{'Grade':>7}{'Letter':>8}{'Status':>10}")
#     print("-" * 50)
#
#     for rank, (name, info) in enumerate(sorted_students, 1):
#         letter = assign_letter_grade(info["grade"])
#         bar    = "█" * (info["grade"] // 10)
#         print(f"{rank:<6}{name:<12}{info['age']:>5}"
#               f"{info['grade']:>7}{letter:>8}"
#               f"{info['status']:>10}  {bar}")
#
#     print("-" * 50)
#     print(f"{'Total Students:':<20} {len(students)}")
#     print(f"{'Class Average:':<20} {avg:.1f}")
#     print(f"{'Highest Grade:':<20} "
#           f"{sorted_students[0][0]} "
#           f"({sorted_students[0][1]['grade']})")
#     print(f"{'Lowest Grade:':<20} "
#           f"{sorted_students[-1][0]} "
#           f"({sorted_students[-1][1]['grade']})")
#
# def show_history():
#     print("\n------- Action History -------")
#     for i, action in enumerate(history, 1):     # O(h)
#         print(f"  {i}. {action}")
#
# def show_menu():
#     print("\n====== Student Management ======")
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. Update Student")
#     print("4. Search Student")
#     print("5. Show All Students")
#     print("6. Show History")
#     print("0. Exit")
#     print("================================")
#
# # ---- Test without menu loop ----
# add_student("Mim",   20, 85)
# add_student("Rahim", 22, 72)
# add_student("Karim", 21, 90)
# add_student("Sana",  23, 65)
# add_student("Rafi",  21, 78)
#
# update_student("Mim", grade=95)
# remove_student("Sana")
# search_student("ra")        # partial search → finds Rahim, Karim, Rafi
#
# show_all()
# show_history()