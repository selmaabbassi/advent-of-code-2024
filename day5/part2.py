import math

def fulfills_rule(rules, current, next):
    try:
        trailing = rules[current]
        if next in trailing:
            return True
        else:
            return False
    except:
        #print(f"{current} is not in dictionary!")
        trailing = rules[next] #Obs denna kanske inte heller finns :(
        if current in trailing:
            return False
        else:
            return True

def reorder_invalid_update(rules, update):
    size = len(update)
    is_updated = False
    for i in range(size - 1):
        for j in range(i+1, size):
            current = update[i]
            next = update[j]
            if fulfills_rule(rules, current, next):
                continue
            else:
                update[i] = next
                update[j] = current
                is_updated = True
    
    if is_updated:
        return update
            
def find_valid_updates(rules, updates):
    valid_updates = []

    for update in updates:
        valid_updates.append(reorder_invalid_update(rules, update))

    return [update for update in valid_updates if update is not None]

def get_middle(update):
    middle = math.ceil((len(update) - 1) / 2)
    return int(update[middle])

def parse_rules(rules_list):
    rules = {}
    
    for rule in rules_list:
        r = rule.split("|")
        precedent = r[0]
        trailing = r[1]
        rules.setdefault(precedent, []).append(trailing)

    return rules

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

rules = parse_rules(rules_list)
updates = parse_updates(updates_list)

valid_updates = find_valid_updates(rules, updates)

counter = 0
for update in valid_updates:
    counter += get_middle(update)

print(f"The answer is: {counter}")