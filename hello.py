from math import sqrt,pow
#b1: Cho 2 điểm A,B.Lập chương trình tính toán khoảng cách giữa 2 điểm này:
#nhập tọa độ điểm x1,x2
x1 = float(input("nhập tọa độ x1: "))
y1 = float(input("nhập tọa độ y1: "))
#nhập tọa độ điểm y1,y2
x2 = float(input("nhập tọa độ x2: "))
y2 = float(input("nhập tọa độ y2: "))
# Công thức tính khoảng cách giữa 2 điểm A,B:
_length_of_vector = math.sqrt ( pow (x2-x1, 2)+ pow (y2-y1, 2))
print(f'Khoảng cách giữa 2 điểm A ( {x1} , {y1} ),B ( {x2 , y2} ) is: {_length_of_vector}')
