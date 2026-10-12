def celsius_to_fahrenheit(temp):
    return temp * 1.8 + 32

celsius_temp=[0,10,37,100]
fahrenheit_temp=list(map(celsius_to_fahrenheit,celsius_temp))

print(fahrenheit_temp)