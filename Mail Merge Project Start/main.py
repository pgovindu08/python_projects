names = []

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

letter_contents = ""

with open("./Input/Letters/starting_letter.txt") as starter_file:
    letter_contents = starter_file.read()

for guest_name in names:
    stripped_name = guest_name.strip()

    new_letter = letter_contents.replace("[name]", stripped_name)

    with open(f"./Output/{stripped_name}_invitation.txt", "w") as invitation_letter:
        invitation_letter.write(new_letter)
