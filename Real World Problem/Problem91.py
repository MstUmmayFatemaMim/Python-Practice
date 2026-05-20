#########       Convert list of student marks into grade dictionary.
students = {
    "Mim":   85,
    "Rahim": 72,
    "Karim": 55,
    "Sana":  91,
    "Rafi":  40
}
result = {}

for name, mark in students.items():
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"
    result[name] = grade

print(result)

# ##########  Way 2 — Dictionary comprehension + helper function (clean)
# def get_grade(mark):
#     if mark >= 90: return "A+"
#     elif mark >= 80: return "A"
#     elif mark >= 70: return "B"
#     elif mark >= 60: return "C"
#     elif mark >= 50: return "D"
#     else: return "F"
#
# result = {name: get_grade(mark) for name, mark in students.items()}
#
# print(result)

# ##########  Way 3 — Using a grade table + loop (no long if/elif chain)
# grade_table = [
#     (90, "A+"),
#     (80, "A"),
#     (70, "B"),
#     (60, "C"),
#     (50, "D"),
#     (0,  "F")
# ]
# result = {}
# for name, mark in students.items():
#     for min_mark, grade in grade_table:
#         if mark >= min_mark:          # first match wins
#             result[name] = grade
#             break                     # stop checking once grade is found
#
# print(result)

# ###############     Way 4 — Using bisect (advanced, very fast)
# import bisect
# boundaries = [50, 60, 70, 80, 90]
# grades     = ["F", "D", "C", "B", "A", "A+"]
# result = {}
# for name, mark in students.items():
#     index = bisect.bisect_left(boundaries, mark)  # finds position in sorted list
#     result[name] = grades[index]
# print(result)
#
# ##########      Way 5 — Show marks AND grades together (bonus)
# def get_grade(mark):
#     if mark >= 90: return "A+"
#     elif mark >= 80: return "A"
#     elif mark >= 70: return "B"
#     elif mark >= 60: return "C"
#     elif mark >= 50: return "D"
#     else: return "F"
#
# result = {name: {"mark": mark, "grade": get_grade(mark)} for name, mark in students.items()}
#
# for name, info in result.items():
#     print(f"{name:10} → Mark: {info['mark']}  Grade: {info['grade']}")