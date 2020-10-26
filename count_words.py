import sys
from rich import print
from pyinspect._colors import mocassin, green, orange

num_lines = sum(1 for line in open(sys.argv[1]) for w in line.split(" "))

print(
    f"[{mocassin}]Found [{orange}]{num_lines}[/{orange}] words in [{green}]{sys.argv[1]}\n"
)
