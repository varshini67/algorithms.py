num=int(input("num: "))
sum=0
if(num>=0):
  while(num>0):
    sum=sum+num
    num=num-1
  print("sum:",sum)
else:
  print("enter positive value")
