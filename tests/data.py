import json

with open('C:/paras_shah/python_scripts/hybrid_framework/tests/data.json', 'r') as f:
    data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)
print(type(data))
x22 = (data['a'])
print(x22)
print(type(x22))
res = list(x22)
print(type(res))
print(res)


