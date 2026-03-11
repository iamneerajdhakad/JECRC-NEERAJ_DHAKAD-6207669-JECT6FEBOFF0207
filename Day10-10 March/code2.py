'''
        FILE HANDLING

file is a type of cintainer in which we contain or store some data.

By using extension name, we can identify what type of data is there insisde of it.
ex.     .py, .mp4, .html, .mp3, .png, .jpg, .jpeg, etc

Before handling any file, taking permission is very much important.

open(): 
    open('filename.ext'/'absolute_path', mode)

close():
    var_name.close()

** here total 3 different modes are present,
    1. write(w),
    2. read(r),
    3. append(a),

write mode:
    1. only write (w)
    2. write + read (w+)
    3. write binary(wb)
    4. write & read binary (wb+)

read mode: If the file is not present and then also you try to read the file then we will get an error file not found
    1. Only read (r)
    2. read + write (r+)
    3. read binary (rb)
    4. read & write binary (rb+)

append mode:
    1. Only append (a)
    2. append + read (a+)
    3. append binary (ab)
    4. append & read binary (ab+)

For write operation,
    1. write(str_data): single line of data.
    2. writelines([ line1, line2, line3,....., linen ]): Multiple line of data. 

NOTE:
    
    1. In this, if the file is not present, it will create one then perform write operation.
    2. If the file is already present, them it will oerride the prev data with the new one.


'''

file = open('temp.txt','w+')

# file.write('I am the first line') 
# file.write('I am the second line')

file.writelines([
    'I am the 1st line',
    '\nI am the 2nd line',
    '\nI am the 3rd line',
    '\nI am the 4th line',
    '\nI am the 5th line',

])

file.seek(0)
print(file.read())

file.close()
