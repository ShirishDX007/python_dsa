#Find two numbers that adds upto num n

def find_num(lst,n):

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == n and i !=j:
                return [lst[i], lst[j]]

if __name__ == '__main__':
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    n = 81
    print(find_num(lst, n))

    