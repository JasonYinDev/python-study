result=1
for i in range(1,11):
  result*=i
  print(result)  
print(result)  

result=1
def recursion(i):
  global result
  if(i<11 and i>0):
    result=result*i
    print(result)
    recursion(i-1)
    
recursion(10)


