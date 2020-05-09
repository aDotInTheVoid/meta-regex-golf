#!/usr/bin/env python3

x=""

while True:
    try:
        x = x + input() + "\n"
    except EOFError:
        break
    
groups = x.split('\n\n')

print("|  | Real | User | Sys |")
print("|--|------|------|-----|")
for i in map(lambda x: x.split('\n'), groups):
    try:
        print(f"| {' '.join(i[0].split()[1:-1])} | {i[1].split()[1]} | {i[2].split()[1]} | {i[3].split()[1]} |") 
    except IndexError:
        break
    
