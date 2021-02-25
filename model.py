import re
def read_all():
    with open("db.txt",'r') as f:
        return f.read()
def read(message):
    out=[]
    with open("db.txt",'r') as f:
        for i in f.readlines():
            if message.upper() in i:
                out+=i.rstrip().split('-')
        return out
def create(student):
    string=''
    if student:
        for i in student:
            string+=i+'-'
        string=string[:-1]
        with open('db.txt','a') as f:
            f.write(string+'\n')
        return string
    else:
        return 'not enough data'
def update(old,new):
    with open("db.txt",'r+') as f:
        text=f.read()
        text=re.sub(old,new,text)
        f.seek(0)
        f.write(text)
def delete(student):
    student=[x.upper() for x in student]
    with open("db.txt",'r') as f:
        lines=f.readlines()
    with open("db.txt",'w') as f:
        for line in lines:
            if not all([i in line for i in student]):
                f.write(line)



# st=['ANOTHER','NAME']
# delete(st)
# update('seconduser@supermail.com','newemail@gmail.com')


