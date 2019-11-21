# --------------
##File path for the file 
file_path 
def read_file(path):    
    file = open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence
sample_message=read_file(file_path)
print(sample_message)


#Code starts here


# --------------
#Code starts here

file_path_1  
file_path_2  

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)

print(message_1)
print(message_1)

def fuse_msg(message_a,message_b):
    quotient=message_b//message_a
    return str(quotient)
import os

secret_msg_1=fuse_msg(int(message_1),int(message_2))
print(secret_msg_1)





# --------------
#Code starts here
file_path_3 
message_3=read_file(file_path_3)
print(message_3)
def substitute_msg(message_c ) :
    sub=''
    print('In substitute_msg ' + message_c)
    if  message_c == 'Red' :
        sub='Army General'
    elif message_c == 'Green' :
        sub='Data Scientist'
    elif message_c =='Blue' :
         sub='Marine Biologist'
    else:
         sub='Nothing'   
    print(sub)
    return sub

secret_msg_2= substitute_msg(message_3)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)

print(message_4)
print(message_5)

def compare_msg(message_d ,message_e):
    a_list = message_d.split()
    print('a_list is ' + str(a_list))
    b_list = message_e.split()
    print('b_list is ' + str(b_list))
    c_list=[]
    for i in range(0,len(a_list)) :
        match=False
        for j in range(0,len(b_list)):
            print('     a_list[' + str(i) + '] is ' +  str(a_list[i])  + ' b_list[' + str(j) + '] is ' +  str(b_list[j]))
            if str(b_list[j]) == str(a_list[i]):
                match=True
                break
        if (not match) : 
            c_list.append(a_list[i])
    print(c_list)    
    final_msg =" ".join(c_list)
    return final_msg 
    
secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)






# --------------
#Code starts here
file_path_6
message_6=read_file(file_path_6)
print(message_6) 

even_word = lambda data:(len(data)%2==0)
def extract_msg(message_f):
    a_list=message_f.split()
    b_list=[]    
    b_list=filter(even_word,a_list) 
    final_msg =" ".join(b_list)
    print(final_msg)
    return final_msg


def filter(even_word,a_list):
        print('In filter ' + str(a_list))     
        b_list=[]
        for i in range(0, len(a_list)):
            if even_word(a_list[i]):
                b_list.append(a_list[i])
        return b_list
secret_msg_4= extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

#Combining the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode
    file = open(path, 'a+')

#     #Writing to the file
    file.write(secret_msg)

#     #Closing the file
    file.close()

# #Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here


