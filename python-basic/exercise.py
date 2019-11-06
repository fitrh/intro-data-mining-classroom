nums = [2, 3, 4, 5, 10]

x = int(input("X : "))
n = int(input("N : "))


def is_in_list(n, list):
    for i in list:
        if(i == n):
            return True
    return False


def gen_fact(n):
    count_of_factor = 0
    for i in range(1, n+1):
        if(n % i == 0):
            print(i, sep=' ', end=' ')
            count_of_factor += 1
    print("\nCount of Factor :", count_of_factor)


def is_prime(n):
    i = 2
    while i*i <= n:
        if (n % i == 0):
            return False
        i += 1
    return n > 1


print("is %d in list? %s" % (x, is_in_list(x, nums)))
print("Factor of %d : " % x, end=' ')
gen_fact(x)
print("Is Prime :", is_prime(x))
count_of_prime = 0
for i in range(x, n+1):
    if is_prime(i):
        print(i, sep=" ", end=' ' if i < n else '\n')
        count_of_prime += 1
print("\nCount of Prime :", count_of_prime)
