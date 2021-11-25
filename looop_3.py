import bai2
def nhap_a():
    a = int(input("nhap gia tri vao ban phim:"))  # nhập số n lần
    while a < 1:
        print("nhap sai vui long nhap lai")
        a = int(input("nhap gia tri vao ban phim:"))
    return a

def nhap_gia_tri():  # nhập vào thông điệp được in ra
    s = input("nhập thông điệp muốn in ra: ")
    return s

def main():
    a = nhap_a()
    s = nhap_gia_tri()

    count = 0
    while (count < a):
        bai2.giatri(s)
        count += 1

if __name__== "__main__":
  main()
