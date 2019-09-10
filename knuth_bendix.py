import sys
import json


def less_than(xs, ys):
    if xs == ys:
        return False

    if len(xs) != len(ys):
        return len(xs) < len(ys)

    for x, y in zip(xs, ys):
        if x != y:
            return x < y


def mins(x, y):
    return x if less_than(x, y) else y 


def maxs(x, y):
    return y if less_than(x, y) else x


def print_rules(rules, ith):
    print(f"After {ith} iteration:")
    for e, r in enumerate(sorted(list(rules))):
        print(f"{e}-th rule is {r}")
    print()


def is_suffix_prefix(x1, x2):
    for i in range(0, len(x1)-1):
        if x2.startswith(x1[i:]):
            abc = x1[:i] + x2
            return True, abc
    return False, None


def is_prefix_suffix(x1, x2):
    for i in range(len(x1), 0, -1):
        if x2.endswith(x1[:i]):
            abc = x2 + x1[i:]
            return True, abc
    return False, None


def is_contained_in(x1, x2):
    if x1 in x2:
        return True, x2
    return False, None


def are_disjoint(r1, r2):
    x1, _ = r1
    x2, _ = r2

    dsj, abc = is_suffix_prefix(x1, x2)
    if dsj:
        # print(f"Yes, is_suffix_prefix, {abc}, {r1}, {r2}")
        return False, abc

    dsj, abc = is_prefix_suffix(x1, x2)
    if dsj:
        # print(f"Yes, is_prefix_suffix, {abc}, {r1}, {r2}")
        return False, abc

    dsj, abc = is_contained_in(x1, x2)
    if dsj:
        # print(f"Yes, is_contained_in, {abc}, {r1}, {r2}")
        return False, abc
    
    # print("Not")
    return True, None    


def confluent(abc, r1, r2):
    abc1 = abc.replace(*r1).replace(*r2)
    abc2 = abc.replace(*r2).replace(*r1)

    return abc1, abc2


def check(r1, r2, reductions):
    dsj, abc = are_disjoint(r1, r2)

    if not dsj:
        abc1, abc2 = confluent(abc, r1, r2)
        if abc1 != abc2:
            # print(f"{abc1} and {abc2} are not confluent")
            new_rule = (maxs(abc1, abc2), mins(abc1, abc2))
            # print(f"New rule: {new_rule}")
            
            return new_rule
    return None


def red(x, y, reductions):
    for rx, ry in reductions:
        if (x, y) != (rx, ry):
            oldx, oldy = x, y
            x = x.replace(rx, ry)
            y = y.replace(rx, ry)
            # print(f"Moving {(oldx,oldy)} to {(x,y)} using {rx, ry}")
    return (x, y)


def do_step(reductions):
    new_rules = set()
    for r1 in reductions:
        for r2 in reductions:
            if r1 != r2:
                new_rule = check(r1, r2, reductions)
                if new_rule and new_rule[0] != '':
                    new_rules.add(new_rule) 
    
    return new_rules


def generate_rules(fname: str):
    with open(fname, "r") as f:
        dd = json.load(f)

    n = dd["N"] # not used
    relations = dd["relations"]
    relations = [("".join(map(str, x)), "".join(map(str, y))) 
                 for x, y in relations]

    reductions = {(maxs(x, y), mins(x, y)) 
                  for x, y in relations}

    print_rules(reductions, -1)

    reductions = {red(x, y, reductions)
                  for x, y in reductions}

    print_rules(reductions, 0)

    old_reductions = None
    ith = 0
    while old_reductions != reductions:
        old_reductions = reductions.copy()
        new_rules = do_step(reductions)

        # print(f"Old rules: {reductions}")
        # print(f"New rules: {new_rules}")

        for x, y in new_rules:
            if all((rx not in x) for rx, ry in reductions):
                reductions.add((x, y)) 
                reductions = {(x, y) for x, y in reductions 
                              if all((rx not in x) or ((x, y) == (rx, ry)) for rx, ry in reductions)}

        # print_rules(reductions, ith)
        ith += 1
    return reductions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("wrong number of args")
    else:
        rules = generate_rules(sys.argv[1])
        print_rules(rules, -0)