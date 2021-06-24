# y = ax + b
# x = ตัวแปรอิสระ
# y = ตัวแปรตาม
# a = ความชัน
# b = ระยะตัดแกน y
import numpy as np
import matplotlib.pyplot as plt
ran = np.random
a = ran.rand(50)*10
b = ran.rand(50)*10 # rand(x) ==> สุ่มเลขมา x ตัว โดยเป็นจำนวนบวก
x = ran.randn(50)*10 # randn(x) ==> สุ่มเลขมา x ตัว โดยเป็นจำนวนลบ
y = a*x + b

plt.scatter(x,y) # แสดงข้อมูลแบบจุด
plt.xlabel('x') # ตั้งชื่อแกน x
plt.ylabel('y') # ตั้งชื่อแกน y
plt.grid() # ใส่ตารางในกราฟ
plt.show()