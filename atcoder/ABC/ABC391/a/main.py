D = input()

match D:
    case "N":
        print("S")
    case "E":
        print("W")
    case "W":
        print("E")
    case "S":
        print("N")
    case "NE":
        print("SW")
    case "NW":
        print("SE")
    case "SE":
        print("NW")
    case "SW":
        print("NE")
