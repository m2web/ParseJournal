file = open("750 Words-export-2017-05-01.txt","r")

lineNum = 0
#Repeat for each line in the text file
for line in file:

  # aLine = line.split("------ ENTRY ------\n")

  # # if line == '------ ENTRY ------\n' :
  # #   print("line #: " + str(lineNum) + " is the new Entry!!!!")
  # # else:
  # #   print('not equal')
  
  # #Print the line
  # #print("line #: " + str(lineNum) + "\n" + aLine[0])
  # print(aLine[0])
  # lineNum += 1
  print(line)

#It is good practice to close the file at the end to free up resources   
file.close()