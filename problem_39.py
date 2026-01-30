# Problem 39: Merge two dictionaries
# Find and fix the error

def merge_dicts(dict1,dict2):
    return dict1|dict2
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = merge_dicts(dict1,dict2)
print(f"Merged dictionary: {merged}")
