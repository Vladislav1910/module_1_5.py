immutable_var = 'Vlad', 19, 26, 64, True
print(immutable_var)

# immutable_var[1] = 'Vladislav'
# Значения элементов кортежа нельзя изменить, потому что он хранит ссылку на списаок, а не сам список.

mutable_list = ['Urban', 8, 24, 16, True]
mutable_list[0] = True
print(mutable_list)
