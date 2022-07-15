import json

filename = 'data/eq.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)