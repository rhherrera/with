if __name__ == '__main__':
    for x in range(1, 101):
        to_print = ""
        if  not x % 3:
            to_print += "Such"
        if not x % 5:
            to_print += "Wow"
        if to_print:
            print(to_print)
        else:
            print(x)
