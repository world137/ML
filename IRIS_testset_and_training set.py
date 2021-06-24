from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split # ใช้แบ่งข้อมูล
iris = load_iris()
print(iris.data.shape) # ==> print (150,4) ==> ข้อมูลมี 150 แถว
#จะแบ่งข้อมูล training set เป็นกี่ % เช่น 75% ==> 112 , testset 25% ==> 38
#แบ่งแกน x y ถ้าไม่ระบุระบบจะแบ่ง 75 25 เอง
x_train,x_test,y_train,y_test = train_test_split(iris["data"],
iris["target"],test_size = 0.2,random_state = 0)
#test_size ==> กำหนดส่วนแบ่ง 0.2 ==> test = 20%

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
