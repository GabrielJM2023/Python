from math import sqrt
xi = int(input("X1: "))
yi = int(input("Y1: "))
xii = int(input("X2: "))
yii = int(input("Y2: "))

print("%.6f"%xi)
dist = sqrt(((xi - xii)**2)+((yi - yii)**2))
print("%.6f"%dist)