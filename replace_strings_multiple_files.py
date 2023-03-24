import os, fnmatch

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

# findReplace("some_dir", "find this", "replace with this", "*.txt")

findReplace(".", "Giulia", "Andrea", "test.txt")


from pathlib import Path
import re

rootdir = Path("C:\\test")
pattern = r'REGEX for the text you want to replace'
replace = r'REGEX for what to replace it with'

for file in [ f for f in rootdir.glob("**.php") ]: #modify glob pattern as needed
  file_contents = file.read_text()
  new_file_contents = re.sub(f"{pattern}", f"{replace}", file_contents)
  file.write_text(new_file_contents)