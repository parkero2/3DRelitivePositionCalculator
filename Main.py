def calcuu():
    chosen = input("======================================\n"
          "Welcome!\n"
          "------\n"
          "Relative position calculator!\n"
          "------\n"
          "This calculator can calculate relative positions!\n"
          "Use the command 'sp' to calculate from your position to another!\n"
          "Or, use 'ip' to increase your position by a specified amount!\n"
          "======================================\n"
          "Choice: ")
    if chosen.upper() == "SP" or chosen.upper() == "IP":
        px = int(input("Player X position: "))
        py = int(input("Player Y position: "))
        pz = int(input("Player Z position: "))
        print("======================================")
        if chosen.upper() == "SP":
            x = int(input("Second X position: "))
            y = int(input("Second Y position: "))
            z = int(input("Second Z position: "))
            print("Difference between the 2 sets of Coordinates:\n"
                  "X:{}, Y:{}, Z:{}".format(x-px, y-py, z-pz))
        elif chosen.upper() == "IP":
            x = int(input("Increase x by: "))
            y = int(input("Increase Y by: "))
            z = int(input("Increase Z by: "))
            print("Difference between the 2 sets of Coordinates:\n"
                  "X:{}, Y:{}, Z:{}".format(x + px, y + py, z + pz))
    else:
        print("Invalid choice! Please select again!")
    calcuu()
calcuu()