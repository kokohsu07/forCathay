def print_equilateral＿triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for k in range(2*i+1):
            if i==n-1:
                if k%2==0:
                    print('*', end='')
                else:
                    print(' ',end='')
            elif k==0 or k==2*i:
                print('*',end='')
            else:
                print(' ',end='')
        print('')

def print_number(num):
    odd=''
    even=''
    for i in num:
        if int(i)%2==0:
            even+=str(i)
        else:
            odd+=str(i)
    print(''.join(sorted(odd,reverse=True)+sorted(even)))


if __name__ == '__main__':

    print_equilateral＿triangle(9)
    print_number('00000000')


