#seaborn ==> ทำงานด้านสถิติ แล้วแสดงเป็นแผนภาพ ทำงานร่วมกับ pandas
import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
print(iris.head())
#สร้างแผนภาพ
sns.set()
sns.pairplot(iris , hue = 'species' , size = 2)
plt.show()