def mean(*args):

    return sum(args) / len(args)

if __name__ == "__main__":
    print(mean(1, 2, 3, 4, 5))
    print(mean(10, 20))

