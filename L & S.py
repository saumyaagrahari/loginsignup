import json
from os import name
import re 
import os.path
print("** Welcome to my Login-Signup Page **")
user = input("Do you want to \n1.)Signup\n2.)Login\n:--")
file_exists = os.path.exists("/home/saumya/Desktop/PYTHON/json/login.json")
def dump(obj):
    with open ("/home/saumya/Desktop/PYTHON/json/login.json") as f:
        json.dump(obj,f,indent=2)
if user=="signup":
    user_name = input("enter your user name:")
    print("create a strong password use specail characters:")
    pass_word1=input("enter your password:")
    # f = open("login.json","r")
    # name = f.read()
    if re.search("[a-z A-Z]",pass_word1) and re.search ("[@%$#!]",pass_word1) and re.search ("[0-9]",pass_word1):
        pass_word2 = input("enter your password again:")

        if pass_word1==pass_word2:
            print("Matching")
        else:
            print("password not matching")
        list1=["username","password"]
        list2=[user_name,pass_word1]
        list3=[]
        dict={}
        i=0
        while i<=1:
            list3.append((list1[i],list2[i]))
            i+=1
        dict.update(list3)
        if user_name in name:
            print(user_name,"already exists")
            # print(dict)
        else:
            print(user_name,"you signed up successfully")
            print("please enter the following details:")
            date_of_birth = input("enter your date of birth:")
            gender = input("enter the gender:")
            hobbies = input("enter the hobbies:")
            description = input("enter the bio:")
            contact_number = int(input("enter the number:"))
            dic = {"username":user_name,"password":pass_word1,"re_password":pass_word2,"date of birth":date_of_birth,
            "gender":gender,"hobbies":hobbies,"description":description,"contact number":contact_number}
            if file_exists == True:
                with open("/home/saumya/Desktop/PYTHON/json/login.json","r") as file:
                    d=file.read()
                    p=json.loads(d)
                    p.append(dic)
                    dump(p)
            else:
                with open ("login.json","a") as file:
                    json.dump([dic],file,indent=4)
    else:
        print("weak password please use specail character")
else:
    if user == "login":
        username = input("enter your user name:")
        password = input("enter the password:")
        with open ("login.json","r") as file1:
            a=file1.read()
            b=json.loads(a)
            for i in b:
                if i in b:
                    if i["username"]==username:
                        if i["password"]==password:
                            print("login successfull")
                            print(i)
                        else:
                            print("Wrong Password")
    else:
        print("Wrong Password")