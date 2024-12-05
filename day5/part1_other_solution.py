from collections import defaultdict, deque
import re
import math

def find_valid_updates(ordered_rules, updates):
    valid_updates = []
    for update in updates:
        regex = '.*'+'.*'.join(update)+'.*'
        if re.match(regex, ordered_rules):
            valid_updates.append(update)

    return valid_updates

def get_middle(update):
    middle = math.ceil((len(update) - 1) / 2)
    return int(update[middle])

def parse_rules(rules):
    graph = defaultdict(list)
    in_dregree = defaultdict(int)
    nodes = set()

    for rule in rules:
        a, b = rule.split("|")
        graph[a].append(b)
        in_dregree[b] += 1
        nodes.update([a,b])

    print(f"Graph: {graph}")

    queue = deque([node for node in nodes if in_dregree[node] == 0])
    ordered_list = []

    while queue:
        current = queue.popleft()
        ordered_list.append(current)

        for neighbor in graph[current]:
            in_dregree[neighbor] -= 1
            if in_dregree[neighbor] == 0:
                queue.append(neighbor)

    print(f"Queue: {queue}")

    print(f"Ordered List: {ordered_list}")
    ordered_string = ''.join(ordered_list)
    return ordered_string

def parse_updates(updates_list):
    updates = []
    
    for string in updates_list:
        update = string.split(",")
        updates.append(update)

    return updates    

if __name__ == "__main__":
    with open("day5.txt", "r") as file:
        data = file.read()

test = data.split("\n\n")

rules_list = test[0].split("\n")
updates_list = test[1].split("\n")

ordered_rules = parse_rules(rules_list)
updates = parse_updates(updates_list)
print(f"Ordered string: {ordered_rules}")

valid_updates = find_valid_updates(ordered_rules, updates)
#print(f"Valid updates: {valid_updates}")


counter = 0
for update in valid_updates:
    counter += get_middle(update)

print(f"The answer is: {counter}")