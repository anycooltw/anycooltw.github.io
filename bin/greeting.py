print(" What's your name ? ")
name=input(" ")
print(" hello "+name+" ! ")

path = './whocame.txt'
f = open(path,'w')
li=[]
li.append("hello "+name+" !")
f.writelines(li)
li.pop()
f.close()
