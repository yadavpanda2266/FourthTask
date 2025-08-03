#write a python program that
'''
opens and read a text file named sample.txt,
prints its content line by line
Handles error gracefully if the file does not exist.
'''
this Is first Question 
'''try:
    file1 =  open('sample.txt', 'w')
    writing_file = file1.write('Reading File Content:\nLine1: This is a sample text file.\nLine2: It contains multiple lines.')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    file1.close()


file1 = open('sample.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()'''

//And This Is Second Question 

user_input = input("Enter some data to write to the file: ")
file1 = open('output.txt','w')
writing_file1 = file1.write(user_input + '\n')
file1.close()

additional_data = "This is some additional data."
file1 = open('output.txt', 'a')
writing_file1=file1.write (additional_data + '\n')
file1.close()

file1 = open('output.txt', 'r')
content = file1.read()
print("Final content of the file:")

print(content)
