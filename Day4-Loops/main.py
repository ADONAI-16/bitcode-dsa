if __name__ == '__main__':

    n=int(input("type any number: "))

    for i in range(n):
        print(i * i)

    # sum of n numbers:

    n=int(input("type any number: "))

    # 0 upto n-1
    total=0

    for i in range(n):
        total=total + i
        print(total)

      #1 upto n-1
    n=int(input("type any number: "))

    total=0

    for i in range(1,n+1):

        total=total + i
        print(total)