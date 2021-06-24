import matplotlib.pyplot as plt
#import ข้อมูลผ่านไฟล์ที่โหลด ได้ภาพที่มีรายละเอียดมากกว่า
from numpy import msort
from scipy.io import loadmat
from scipy.io.matlab.mio5_utils import csc_matrix
mnist_raw = loadmat("mnist-original.mat")
mnist = {
    #.T == transpose array
    'data':mnist_raw["data"].T,
    'target':mnist_raw['label'][0]
}
k = 24101 # กำหนดเลขที่ต้องการให้แสดง
x = mnist["data"]
y = mnist['target']
number = x[k]#ได้เลข 2 แต่มองงจากภาพอาจดูไม่ออก ==> แสดงเป็นตัวอักษรเพื่อบอกค่าด้วย
number_image = number.reshape(28,28)
print(y[k])#โปรแกรม output เลข 2
plt.imshow(number_image , cmap = plt.cm.binary , interpolation = 'nearest')
plt.show()