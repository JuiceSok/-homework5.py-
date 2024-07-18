immutable_var = 1,2,3,'a','b','c'
print(immutable_var)
#immutable_var[2] = 4
# Кортежи в Python являются неизменяемыми структурами данных поэтому если изменить их будет выдавать ошибку.
mutable_list = [ 16, 23, 42,'a','b', 'world',]
print(mutable_list)
mutable_list[0] = "sport"
mutable_list[1] = 77
mutable_list[2] = "windows"
mutable_list[5] = 33
print(mutable_list)
