import os

# List of files to check
files = ["create.py", "retrieve.py", "update.py", "delete.py"]

# Check each file
for f in files:
    if os.path.isfile(f):
        print(f"{f} exists ✅")
    else:
        print(f"{f} does NOT exist ❌")

