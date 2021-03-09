if __name__ == '__main__':
    for x in range(1, 101):
        if not x % 5 and not x % 3:
            print("SuchWow")
        elif not x % 5:
            print("Wow")
        elif not x % 3:
            print("Such")
        else:
            print(x)

