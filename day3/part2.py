import re

def chunk_string(s):
    chunks = []
    i = 0

    while i<len(s):
        chunk_start = i
        if s[i:].startswith("don't()"):
            while i<len(s) and not s[i:].startswith("do()"):
                i += 1
            chunks.append(s[chunk_start:i])
        elif s[i:].startswith("do()"):
            while i<len(s) and not s[i:].startswith("don't()"):
                i += 1
            chunks.append(s[chunk_start:i])
        else:
            while i<len(s) and not s[i:].startswith("don't()") and not s[i:].startswith("do()"):
                i += 1
            chunks.append(s[chunk_start:i])

    return [chunk for chunk in chunks if chunk]

def filter_chunks(chunks):
    return [chunk for chunk in chunks if not chunk.startswith("don't()")]

if __name__ == "__main__":
    with open("day3.txt", "r") as file:
        data = file.read()

#print(data)

chunks = chunk_string(data)
do_chunks = filter_chunks(chunks)
#print(chunks)
#print(f"DO_CHUNKS {do_chunks}")

do_matches = []
for chunk in do_chunks:
    #print(chunk)
    matches = re.findall(r"mul(\(\d*,\d*\))", chunk)
    #print(matches)
    do_matches.append(matches)
    
#print(f"DO_MATCHES {do_matches}")

counter = 0

for match in do_matches:
    for m in match:
        #print(m)
        numbers = re.match(r"\((\d*),(\d*)\)", m).groups()
        #print(numbers)
        counter += (int(numbers[0]) * int(numbers[1]))

print(f"The answer is: {counter}")
