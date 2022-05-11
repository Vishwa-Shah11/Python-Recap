def isSymmetricBad(L):
    try:
        while len(L) > 0:
            if L.pop(0) != L.pop(-1):
                return False
        return True
    except IndexError:
        print("IndexError")

    except:
        print("some other exception occurred")

    else:
        print("No exception occurred")

L = [2, 4, 6]
L = [1, 2, 3, 4, 3, 2, 1]
L = [2, 2, 2, 2, 2, 2]
L = [1, 1, 1, 1, 1, 1, 1]
L = [8]
print(isSymmetricBad(L))