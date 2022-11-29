user_number = int(input())

number = []
s = 0

while True:
    for i in range(len(number)+1):
        s = s * i
        if s == user_number:
            print("yes")
            break
        if s > user_number:
            print("no")
            exit()
