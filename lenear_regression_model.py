import numpy as np
import matplotlib.pyplot as plt
# import linearRegression
from sklearn.linear_model import LinearRegression
ran = np.random

# จำลองข้อมูล
a = ran.rand(50)*10
b = ran.rand(50)*10 # rand(x) ==> สุ่มเลขมา x ตัว โดยเป็นจำนวนบวก
x = ran.randn(50)*10 # randn(x) ==> สุ่มเลขมา x ตัว โดยเป็นจำนวนลบ
y = a*x + b

# linear regression model
model = LinearRegression()
x_new = x.reshape(-1,1)  # ทำให้เป็น array 2D เพื่อใส่ใน model
# train ข้อมูลลงใน model
model.fit(x_new,y)
# แสดงประสิทธิภาพของโมเดล
print("R-squre" , model.score(x_new,y)*100) # ==> หาค่า R-squre ==> สปส แสดงการตัดสินใจ พยากรณ์หาค่า y โดยมีต่าระหว่าง 1-100
print("intrercept" , model.intercept_) # ==> จุดตัดแกน
print("coef" , model.coef_) # ==> สปส(ค่าของ y ตอนที่ x เป็น 0)
# test model
x_test = np.linspace(-1,11)
x_test_re = x_test.reshape(-1,1) # reshape ==> array 2D
print("shape" , x_test_re.shape)
y_test = model.predict(x_test_re)
# analysis model
plt.scatter(x,y)
plt.plot(x_test,y_test)
plt.show()
