import sys

processString = sys.argv[1]
processProperties = list(filter(lambda str: str != "", processString.split(" ")))
pid = processProperties[1]

print("kill {pid}".format(pid = pid))
