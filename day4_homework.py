

def prime(a,b):
   list=[]
   for sayi in range(a,b+1):
      if sayi>1:
       for i in range(2,sayi):
         if sayi%i==0:
            break
       else: 
            list.append(sayi)
   return list          
   
a=int(input("enter first number ")) #1 
b=int(input("enter last number ")) #100    
print(f" Prime numbers {prime(a,b)}")