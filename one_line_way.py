if __name__ == '__main__':
    for i in range(1,101): print("Such"*(i%3==0) + "Wow"*(i%5==0) or i)
