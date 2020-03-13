
#if we open the file in 'with' it closes itself
#we must write the encoding 'cp1252' for windows, 'utf-8' for linux
#r means read only
#w means write(also deletes everything) if file does not exist create a new file 
#x Open a file for exclusive creation. If the file already exists, the operation fails. (What is exclusive creation ?)
#a Open for appending at the end of the file without truncating it. Creates a new file if it does not exist. (Look this up too)
#t open in text mode (try this)
#b Open in binary mode (can try this to)
#+ Open a file for updating (reading and writing)

#We can also use try blocks for opening files

with open("test.txt",'w',encoding = 'cp1252') as f:
    f.write("hello world \n")
    f.write("My name is Serkan ")
    f.write("And welcome \n")
    f.write("next Line")

#seek goes to the line we write
#tell gives us our position
#f.readline reads the line takes the '\n' to
#f.readlines takes all
#if we are at the end this functions return empty

with open("test.txt",'r',encoding = 'cp1252') as f:
    print(f.read(4)) #reads only the first 4
    print(f.read(4))
    print(f.tell()) 
    f.seek(0)
    print(f.read()) #read all
    f.seek(0)
    print(f.readline(),end="")
    st=f.readlines() #takes the \n to so watch out in string operations
    print(st)
    #print(f.read())
    f.seek(0)
    #We can also use for to read lines
    for line in f:
        print(line,end="") # if we dont use end="" it gives to empty lines because of print(print has automatic \n)
    
#We have many functions to use in file operations (check out file streams)
"""close() closes the file
detach() ?
fileno() ? Return an integer number (file descriptor) of the file(probably gives file a number)
flush() ?
isatty() ?
read(n) reads all or n number of characters
readable() return true if file stream is readable
readline(n) readline or n bytes from a line
readlines(n) read all or n lines
seek(offset,from=SEEK_SET) start, current, end
seekable() return true if file stream supports random access
tell() tell the position 
truncate(size=None) Resize the file stream to size bytes. If size is not specified, resize to current location. ?
writable() returns true if file stream is writable
write(s)
writelines() writes a list of lines (try this one)
"""


