import json
with open('382000000A-002967-001.json') as f:
    a = json.load(f)
    print(a)
    print(json.dumps(a, indent=4))