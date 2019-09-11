def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline low"
    else:
        return "low"


def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif 130 <= LDL <= 159:
        return "Borderline high"
    elif 159 < LDL <= 189:
        return "High"
    else:
        return "Very High"


def check_TLC(TLC):
    if TLC < 200:
        return "Normal"
    elif 200 <= TLC <= 239:
        return "Borderline high"
    else:
        return "High"


def cholestoral_interface():
    print("Cholesterol check")
    chol_input = input("Enter your cholesterol test result: ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The HDL cholesterol level is {}.".format(result))
    elif chol_data[0] == "LDL":
        results = check_LDL(int(chol_data[1]))
        print("The LDL cholesterol level is {}.".format(results))
    elif chol_data[0] == "TLC":
        results = check_TLC(int(chol_data[1]))
        print("The total cholesterol level is {}.".format(results))


def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("Option: ")
        print("1 - Cholesterol Checks")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
           keep_running = False
        elif choice == '1':
            cholestoral_interface()
            
    return
        

if __name__ == "__main__":
    interface()