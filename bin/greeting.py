
name=input("What's your name ?  ")
print("hello "+name+" !")

path = './whocame.txt'
f = open(path,'w')
li=[]
li.append("hello "+name+" !")
f.writelines(li)
li.pop()
f.close()
