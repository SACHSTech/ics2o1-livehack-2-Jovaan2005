angle1 = int(input(" Enter in length of side 1:  "))
angle2 = int(input("Enter the length of side 2: "))
angle3 = int(input("Enter the length of side 3: "))

an1 = angle1**2   
an2 = angle2**2
an3 = angle3**2

if (an1+an2 == an3) or (an1+an3 == an2)  or (an2+an3 == an1):
  print("The figure is a triangle " + str(angle1) + "," +
  str(an2) + ", and " + str(an3) + " The figure is a triangle..")
else:
    print("A triangle with lengths " + str(angle1) + ", " +
    str(angle2) + ", and " + str(angle3) + " The figure is NOT a triangle.")
