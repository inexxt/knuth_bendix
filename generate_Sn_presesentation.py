import sys
import json

def generate(n: int, fname: str):
    print(f"Generating presentation to a file {fname}")
    
    relations = []
    for i in range(0, n):
        relations.append([[i, i], []])

    for i in range(1, n):
        for j in range(1, i-1):
            relations.append([[i, j], [j, i]])

    for i in range(1, n-1):
        relations.append([[i, i+1, i], [i+1, i, i+1]])

    presentation = {
        "N": n,
        "relations": relations
    }

    with open(fname, "w") as f:
        json.dump(presentation, f)

    print(json.dumps(presentation))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong number of args")
    else:
        n = int(sys.argv[1])
        generate(n, f"S{n}_presentation.json")