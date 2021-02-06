
#1
list=[]

while True:
 length=int(input("enter list length")) 
 if length%2==0:

  for el in range(0,length):
    element=int(input("enter element"))
    list.append(element)
  print(f"your old list: {list}") 
 
  list1=list[:len(list)//2]
  list2=list[len(list)//2:]
  list=list2+list1
  print(f"Your new list:{list}")
  break
 else:
    print("list length must be even number for doing swap")
    continue

"""
#2

i=-10
list=[]
while True:
 n=int(input("Enter a single digit integer")) 
 if -9<=n<=9:
  
  while i<n:
    i+=1
    if i%2==0:
      list.append(i)
    else:
      continue 
  break
 else:
  print("Invalid value,n must be greater than -10 and smaller than 10.Try again.")
  continue
 
print(list)

"""