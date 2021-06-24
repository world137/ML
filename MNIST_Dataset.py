#แสดงภาพข้อมูล
import matplotlib.pyplot as mpl
#ข้อมูลมีขนาดใหญ่ impport ผ่าน sklearn จะถูกย่อขนาดเหลือ 8*8
from sklearn import datasets
MINST = datasets.load_digits()
#print(MINST.keys())
print(MINST.target[0])
mpl.imshow(MINST.images[0],cmap = mpl.get_cmap('gray'))
mpl.show()
"""
print(MINST.target_names[0:2])
print(MINST.images[0])
print(MINST.images[0].shape)
"""