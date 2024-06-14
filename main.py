# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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
    for i in str(num):
        if int(i)%2==0:
            even+=str(i)
        else:
            odd+=str(i)
    print(''.join(sorted(odd,reverse=True)+sorted(even)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_equilateral＿triangle(9)
    print_number(417324689435)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
