r = float(input("Enter the radius : "))
if r>=0 and r<100.0:
  area=3.14*r*r
  print(f"area of circle ={area:.6f}")
else:
  print("Enter a positive value upto 100")
