import math
angle_tuple=(0,30,45,90)
trig_value_list=[]
for angles in angle_tuple:
    radians=math.radians(angles)
    sin_value=round(math.sin(radians),4)
    cos_value=round(math.cos(radians),4)
    trig_value_list.append((sin_value,cos_value))
    print(trig_value_list)


