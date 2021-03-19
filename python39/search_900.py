

'''
人教版小学4下53练习题P17：
()*26 + ()*64 = 900
'''


print('------------------------------------')
print('---first method: 2D search----------')

for i in range(30):
    for j in range(14):
        print('current i = %d, j = %2d,  i*26+j*64 = %d' %(i,j,i*26+j*64))
        if (i*26 + j*64 == 900):    #如果找到
            break   # j循环全部停止
    else:           # j循环完成，即if条件未实现
        continue    # 注意，该continue属于j循环体，不是由L16的break触发，指示j循环进入下轮
    break           # 当L16触发了j循环完全提前中止，那么该行执行
print('found i= ',i)
print('found j=',j)




print('------------------------------------')
print('---second method: Descartes product-')
from itertools import product

for i, j, in product(range(30), range(14)):
    print('current i = %d, j = %2d,  i*26+j*64 = %d' %(i,j,i*26+j*64))
    if (i*26 + j*64 == 900):
        print('break')
        break
print('found i= ',i)
print('found j=',j)
