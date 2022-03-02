a = [1,2,3,[11,22,33]]
b = a.copy()
print(b)   #[1, 2, 3, [11, 22, 33]]
b[3][2] = 'aaa'
print(a)    #[1, 2, 3, [11, 22, 'aaa']]
print(b)    #[1, 2, 3, [11, 22, 'aaa']]

a[0] = 0
print(a)    #[0, 2, 3, [11, 22, 'aaa']]
print(b)    #[1, 2, 3, [11, 22, 'aaa']]
print(id(a)==id(b))        #False
print(id(a[3])==id(b[3]))  #True
import copy
b=copy.deepcopy(a)




