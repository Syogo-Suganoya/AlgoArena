N = input()

match int(N[-1]):
    case 2 | 4 | 5 | 7 | 9:
        print("hon")
    case 0 | 1 | 6 | 8:
        print("pon")
    case 3:
        print("bon")
