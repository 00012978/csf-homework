def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


number = int(
    input("Please, input the number you want to start the count from: "))
print(number)
if number >= 0:
    countdown(number)
else:
    countup(number)
