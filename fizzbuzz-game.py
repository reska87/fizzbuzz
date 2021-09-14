def print_hi(name):
    print(f'Welcome to {name}')

if __name__ == '__main__':
    print_hi('Reska fizzbuzz games')
print('please hit enter')
fizzbuzz = input()

for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print(str(fizzbuzz) + 'it\'s a fizzbuzz')
        continue
    elif fizzbuzz % 3 == 0:
        print(str(fizzbuzz) + 'it\'s a fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print(str(fizzbuzz) + 'it\'s a buzz')
        continue
    print(fizzbuzz)
for fizzbuzz in range(101):
    print(fizzbuzz)

