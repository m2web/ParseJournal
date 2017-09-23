with open("750 Words-export-2017-05-01.txt", mode="r") as journalFile:
    reader = journalFile.read()
    for i,part in enumerate(reader.split("------ ENTRY ------\n")):
        with open("File_" + str(i+1), mode="w") as newfile:
            newfile.write("New Entry"+part)