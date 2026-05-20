# # ##########  115.Deep Merge Two Dictionaries
# # Write a function:
# # def deep_merge_dicts(d1: dict, d2: dict) -> dict:
# #     pass
# # Rules
# # Merge d2 into d1
# # If a key exists in both:
# # If both values are dicts → merge recursively
# # Otherwise → value from d2 overrides
# # The function must:
# # NOT mutate d1 or d2
# # Work for arbitrary nesting
# # No external libraries
# # Handle mixed value types safely
# # 🧪 Example
# # d1 = {
# #     "a": 1,
# #     "b": {
# #         "x": 10,
# #         "y": 20
# #     },
# #     "c": 3
# # }
# # d2 = {
# #     "b": {
# #         "y": 99,
# #         "z": 50
# #     },
# #     "d": 4
# # }
# # deep_merge_dicts(d1, d2)
# # —------------------------------------------
# # ✅ Output
# # {
# #     "a": 1,
# #     "b": {
# #         "x": 10,
# #         "y": 99,
# #         "z": 50
# #     },
# #     "c": 3,
# #     "d": 4
# # }
# #######    Manually solving
# d1 = {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}
# d2 = {"b": {"y": 99, "z": 50}, "d": 4}
# merged = d1.copy()
# merged = merged | d2
# merged["b"] = d1["b"] | d2["b"]
# print(merged)

def deep_merge_dicts(d1: dict, d2: dict) -> dict:
    # 1. Safe copy to prevent mutating the original d1
    merged = d1.copy()
    merged = merged | d2

    for key in d2:
        try:
            # Instead of |, we call deep_merge_dicts here to handle infinite levels of nesting safely
            merged[key] = deep_merge_dicts(d1[key], d2[key])
        except:
            # If d1[key] or d2[key] is a number/string instead of a dict, it fails and keeps d2's value
            pass

    return merged


# 🧪 Test the Challenge Example
d1 = {
    "a": 1,
    "b": {
        "x": 10,
        "y": 20
    },
    "c": 3
}
d2 = {
    "b": {
        "y": 99,
        "z": 50
    },
    "d": 4
}

print(deep_merge_dicts(d1, d2))
