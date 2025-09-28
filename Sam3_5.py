memory = 'world'
string = 'hello'
counter = 0

while counter != 10:
    memory = string
    if counter < 10:
        if counter % 2 == 0:
            print(memory + " " + memory)
        else:
            print(memory)
        counter += 1

print(memory + " " + memory)