people_names = []

with open("Input/Names/invited_names.txt") as names:
    for line in names:
        name = line.strip()
        people_names.append(name)

with open("Input/Letters/starting_letter.txt") as file:
    data = file.read()
    for i in people_names:
        new_letter = data.replace("[name]", i)
        with(open(f"Output/ReadyToSend/letter_for_{i}.txt", "w")) as send_letter:
            send_letter.write(f"{new_letter}")
