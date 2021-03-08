n = 9
count = 0
n1 = 0
n2 = 1


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # Nilai Fibonacci pertama 0
    elif n == 1:
        return 0
    # Nilai Fibonacci kedua 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print("Bilangan fibonacci yang ke", n, "adalah", Fibonacci(n))
list_fibonacci = []
while count < n:
    list_fibonacci.append(n1)
    bil_akhir = n1 + n2
    n1 = n2
    n2 = bil_akhir
    count += 1

print(list_fibonacci)

daftar_string = [str(angka) for angka in list_fibonacci]
deret_string = ', '.join(daftar_string)
print('Deret fibonacci dengan banyak bilangan {} adalah:\n{}'. format(
    n, ', '.join(daftar_string)))
