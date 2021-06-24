from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.algorithms import mode
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("Weather.csv")
print(data.head)
data.plot(x = 'MinTemp' , y = 'MaxTemp', style = "x" ,color = 'green') # style กำหนดสัญลักษณ์ในกราฟ
print(data.describe()) # ดูภาพรวมของข้อมูล
#train & test set
x = data["MinTemp"].values.reshape(-1,1)
y = data["MaxTemp"].values.reshape(-1,1)
# แบ่งข้อมูล 80:20
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
# training
model = LinearRegression()
model.fit(x_train,y_train)
#test
y_predict = model.predict(x_test) #ดูข้อมูลที่ทำนายว่าตรงกับที่มีหรือไม่
'''
plt.scatter(x_test,y_test)
plt.plot(x_test,y_predict, color = "pink",linewidth = 2)
plt.show()
'''
#compare ==> เปรียบเทียบข้อมูลที่คาดเดากับข็อมูลจริง
df = pd.DataFrame({'Actually':y_test.flatten(),'Predict': y_predict.flatten()}) # flatten ==> แปลงข้อมูลบให้เป็น 1D
print(df)
print("shape" , df.shape)
df1 = df.head(20) # ข้อมูล 20 ตัวแรก
df1.plot(kind = "bar" , figsize = (16,10), color = {"Actually": "pink", "Predict": "lightblue"}) # ข้อมูลเป็น bar chart
plt.show()

'''
plt.title('Min & Max Temp')
plt.xlabel('Min temp')
plt.ylabel('Max temp')
plt.show()
'''