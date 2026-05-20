# # ####### 102. Default Argument Trap (Real Fix)
# # Write a function log_action(action, logs=None) that:
# # Stores actions in a list
# # Never shares state between function calls
# # After doing it with list do it with dict
# def log_action(action, logs=[]):        # list born once, never dies
#     logs.append(action)
#     print(logs)
#     return logs
#
# log_action("login")   # ['login']
# log_action("logout")  # ['login', 'logout']  ← shared state leak


# # # ── FIX 1: None sentinel (idiomatic) ───────────────────
def log_action(action, logs=None): ####### list born every time
    if logs is None:     # identity check, O(1)
        logs = []        # new list every call
    logs.append(action)
    print(logs)
    return logs
log_action("login")
log_action("logout")
# # ── FIX 2: or [] shorthand (common but has a flaw) ─────
# def log_action(action, logs=None):
#     logs = logs or []    # BUG: if caller passes [], this creates a NEW list
#     logs.append(action)  # intentional empty list gets silently thrown away
#     print(logs)
#     return logs
# log_action("login")
# log_action("logout")

# # ── FIX 3: factory default via functools ───────────────
# from functools import wraps
# def with_list_default(fn):
#     @wraps(fn)
#     def wrapper(action, logs=None):
#         return fn(action, logs if logs is not None else [])
#     return wrapper
# from functools import wraps
#
# def with_list_default(fn):
#     @wraps(fn)
#     def wrapper(action, logs=None):
#         # Use a fresh list if logs is None, otherwise use the provided list
#         return fn(action, logs if logs is not None else [])
#     return wrapper
#
# # 1. Apply your decorator to a sample function
# @with_list_default
# def process_action(action, logs):
#     logs.append(f"Performed: {action}")
#     return logs
#
# # 2. Call the function and print the returned output
# output1 = process_action("Login")
# print(output1)
# # Output: ['Performed: Login']
#
# # 3. If you pass your own log list, it will append to it instead of making a new one
# existing_logs = ["System started"]
# output2 = process_action("Click Button", existing_logs)
# print(output2)
# # Output: ['System started', 'Performed: Click Button']

# # ── FIX 4: class-based (stateful across calls by design) ─
# class ActionLogger:
#     def __init__(self):
#         self.logs = []
#     def log(self, action):
#         self.logs.append(action)
#         return self.logs

# # 1. Define the class
# class ActionLogger:
#     def __init__(self):
#         self.logs = []
#     def log(self, action):
#         self.logs.append(action)
#         return self.logs
#
# # 2. Create an instance of the class
# logger = ActionLogger()
#
# # 3. Call the method and print the returned list
# print(logger.log("User logged in"))
# # Output: ['User logged in']
#
# # 4. Call it again (the state is preserved inside the instance)
# print(logger.log("Button clicked"))
# # Output: ['User logged in', 'Button clicked']
#
# # 5. You can also view the state directly at any time
# print(logger.logs)
# # Output: ['User logged in', 'Button clicked']
