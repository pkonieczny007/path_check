import os
#import os.path


#sciezka do pliku
a=os.path.abspath(os.getcwd())

#dołożenie ścieżki
b=a +'\\bak'
print(b)

input("\n\nAby zakonczyc ENTER")



'''
import os.path
save_path = 'C:/example/'
name_of_file = raw_input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file+".txt")         
file1 = open(completeName, "w")
toFile = raw_input("Write what you want into the field")
file1.write(toFile)
file1.close()

'''
print(os.path)
