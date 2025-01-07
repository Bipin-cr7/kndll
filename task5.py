'''
5. Reading and Writing to Files (Data I/O)
Task: Write a Python program that reads a text file, counts the number of lines, words, and characters, and then writes this information into a new file.
Skills to Practice: File handling, reading and writing files, string manipulation.
Example Steps:

Create a sample text file (can be done manually or in the program).
Read the file line by line, and count the number of lines, words, and characters.
Write the counts to a new file.

'''
with open("file.txt") as f:
   countlines=f.readlines()
   length= len(countlines)
  

   words_length=0
   char_length=0


   for line in countlines:
      words_length += len(line.split())
      char_length+= len(line)

with open("new_file","w")as f:
   f.write(f" number of lines={length}\n numbers of words={words_length} \n number of characters={char_length}")

