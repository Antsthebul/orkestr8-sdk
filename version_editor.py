import re
import sys

lines = []
args = sys.argv
tag = args[1]
message = args[2]

if not bool(message.strip()):
    raise Exception("message required")

with open("./pyproject.toml") as f:
    for line in f.readlines():
        if line.startswith("version="):
            if not re.search(r"v\d{1,3}\.\d{1,3}\.\d{1,3}", tag):
                raise Exception(f"'{tag}' is not a correct SemVer tag")
            tag = tag.replace("v", "")
            line = "version=" + f'"{tag}"\n'
        lines.append(line)

with open("./pyproject.toml", "w") as f:
    f.writelines(lines)
