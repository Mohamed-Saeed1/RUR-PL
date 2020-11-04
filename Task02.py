def show_menu():
    x = int(input('Choose an operation\n[0] Check Palindrome \t [1] Check if Prime\n[99] Exit\n'))
    return x


def is_prime(num):
    temp = 1
    p = 0
    while temp <= num:
        if num % temp == 0:
            p += 1
        temp += 1
    if p == 2:
        print(num, 'is a prime number')
    else:
        print(num, 'is not prime')


def is_palindrome():
    word = input('Enter the word you want to check ')
    if word == word[::-1]:
        print('YES')
    else:
        print('NO')


x = 0
while x != 99:
    print('')
    x = show_menu()
    if x == 99:
        break
    elif x == 0:
        is_palindrome()
    elif x == 1:
        n = int(input('Enter the number '))
        is_prime(n)
    else:
        print('Invalid choice, please try again')