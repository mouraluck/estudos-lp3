
import math
'''n1 = int(input())
n2 = int(input())
r = n1+n2
print("X = {}".format(r))

N = 3.14159
raio = float(input())

area = raio*raio*N

print("A={:.4f}".format(area))

n1 = float(input())
n2 = float(input())
soma = (n1*3.5)+(7.5*n2)
MEDIA = soma/11
print("MEDIA = {:.5f}".format(MEDIA))'''

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

solutionX = (x2 - x1)
solutionY = (y2 - y1)
dab = math.sqrt(solutionY** 2) + (solutionX** 2)
print(dab)