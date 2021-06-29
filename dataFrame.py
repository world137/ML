from IPython.display import display
import pandas as pd
import numpy as np
data1 = [[10,20,30,40], #list,array2D =>เอาไปเรียงใน df ตรงๆ
        [22,11,33,44],
        [123,232,442,112]]

data2 = {'x1' : [10,20,30,40], #dic => เอาไปเรียงเป็น col
        'x2' : [22,11,33,44], #ใช้ np.random.randint(x,y,z.....)แทนได้
        'x4' : [123,232,442,112]}

# data1 = data2 transpose

a = {'p1' : 10 , 'p2' :  20}

b = {'p1' : 11 , 'p2' : 22}

data3 = {'a' : a , 'b' : b}

df = pd.DataFrame(data1 , columns = list('abcd'),
                    index = ['one' , 'two' , 'three'])
                    #ใส่ index,columns เกิน => ขึ้น nan ในตาราง

df2 = pd.DataFrame(data2 , index = list('abcd') , dtype = int)

df3 = pd.DataFrame(data3)

display(df , '\n')
display(df2 , '\n')
display(df3) 