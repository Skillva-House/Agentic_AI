import csv
import json

# --- Text ---
with open("notes.txt", "w") as f:         # "w" overwrites, "a" appends, "r" reads
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# --- CSV write ---
rows = [
    {"name": "Ali", "score": 80},
    {"name": "Sara", "score": 95},
    {"name": "Hamza", "score": 60},
]
with open("scores.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

# --- CSV read + filter + write ---
with open("scores.csv", "r") as f:
    data = list(csv.DictReader(f))

passed = [r for r in data if int(r["score"]) >= 70]

with open("passed.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(passed)

# --- JSON ---
with open("data.json", "w") as f:
    json.dump(passed, f, indent=4)

with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded)

# --- Error handling ---
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Bad JSON")