PLACEHOLDER = "[name]"
with open("Input\Aname\inames.txt") as nom:
    names = nom.readlines()

with open("Input\Letters\starting_letter.txt", mode="r") as toedit:
    file_to_edit = toedit.read()

    for name in names:
        strippedname = name.strip()

        new_letter = file_to_edit.replace(PLACEHOLDER, strippedname)

        with open(f"Output\ReadyToSend\letter_for_{strippedname}.txt", mode="w") as final_file:
            final_file.write(new_letter)
