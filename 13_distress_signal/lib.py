import json
from math import prod

def compare(left, right):
    cursor = 0
    result = None
    while(True):
        l = None
        r = None
        if cursor < len(left):
            l = left[cursor]
        if cursor < len(right):
            r = right[cursor]

        #  print(f"{cursor}.", l, r)

        if l == None and r == None:
            return result
        elif l == None and r != None:
            return True
        elif l != None and r == None:
            return False
        elif type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                result = None
        elif type(l) == list and type(r) == int:
            result = compare(l, [r])
        elif type(l) == int and type(r) == list:
            result = compare([l], r)
        elif type(l) == list and type(r) == list:
            result = compare(l, r)
        if result == None:
            cursor +=1
            continue
        else:
            return result

def ex1(input_path):
    data = []
    with open(input_path, "r") as file:
        for pair in [line.strip() for line in file.read().split("\n\n")]:
            left, right = [json.loads(packet) for packet in pair.splitlines()]
            data.append(compare(left, right))
    return sum([i + 1 for i, value in enumerate(data) if value == True])

def ex2(input_path):
    divider_packets = [[[2]],[[6]]]
    data = []
    with open(input_path, "r") as file:
        head, *packets = [json.loads(line) for line in file.read().split("\n") if line.strip() != ""]
        data.append(head)
        packets += divider_packets
        while len(packets):
            index = len(data)
            packet = packets.pop(0)
            for i, target in enumerate(data):
                if compare(packet, target) == True:
                    index = i
                    break
            data.insert(index, packet)
    return prod([data.index(value) + 1 for value in divider_packets])

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
