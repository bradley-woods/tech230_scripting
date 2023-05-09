import yaml
import os
import sys

# sys.argv = terminal variables entered after python:
# e.g. 'python check_json.py example.json' = 2 variables
if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
        print("YAML is valid")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: python check_yaml.py <yamlfile.yaml>")
