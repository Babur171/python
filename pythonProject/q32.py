def palindrome(string):
    string = string.lower()
    string = string.replace(" ","").replace("\n","")
    tem = ['.',',','!','?','\"', "\'"]
    for i in tem:
        string = string.replace(i,"")
    tmp = ''
    length = len(string)
    for i in range(length):
        tmp += string[length-1]
        length -= 1
    if string == tmp:
        return True
    else:
        return False


print("Enter your filename with extension : ")
file_name = input(">>")
with open(file_name,'r') as f:
    for item in f.readlines():
        print(palindrome(item))