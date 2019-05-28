
def print_list(list, attributes):
    for attr in attributes:
        print("{:>30s}".format(attr), end=" ")

    print("")

    for obj in list:
        for attr in attributes:
            print("{:>30s}".format(str( getattr(obj, attr))), end=" ")

        print("")