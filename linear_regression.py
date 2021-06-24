# y = ax + b
# x = ตัวแปรอิสระ
# y = ตัวแปรตาม
# a = ความชัน
# b = ระยะตัดแกน y
import numpy as np
import matplotlib.pyplot as plt
a = 2
b = 1
x = np.linspace(-5,5,100)#linspace(x,y,z)สร้างข้อมูลที่มีค่าระหว่าง x,y เป็นจำนวน z ตัว 
y = a*x + b

plt.plot(x,y,'-r', label = 'y=2x+1') #แสดงข้อมูลแบบเส้น
plt.xlabel('x') # ตั้งชื่อแกน x
plt.ylabel('y') # ตั้งชื่อแกน y
plt.grid() # ใส่ตารางในกราฟ
plt.legend(loc = "upper left") # ตั้งว่าให้ชื่ออยู่ที่ตำแหน่งไหน(title)
plt.title("graph y = 2x + 1") # ตั้งว่าให้สิ่งที่แสดงชื่ออะไร
plt.show()