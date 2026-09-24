import math

degrees=float(input("Enter your degrees: "))
radians= math.radians(degrees)

sine=math.sin(radians)
cosine=math.cos(radians)
tangent=math.tan(radians)

cosecant=1/sine
secant=1/cosine
cotangent=1/tangent

print(f"Sine: {sine:.2f}")
print(f"Cosine: {cosine:.2f}")
print(f"Tangent: {tangent:.2f}")
print(f"Cosecant: {cosecant:.2f}")
print(f"Secant: {secant:.2f}")
print(f"Cotangent: {cotangent:.2f}")
