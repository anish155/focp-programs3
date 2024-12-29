def temperature():
    while True:
        numbers=input("enter the celsuis value:")
        if numbers=="":
            print("program terminated.")
            return None
        else:
            return float(numbers)

def fahrenheith_convert(call):
    fahrenheith=(call*9/5)+32
    return fahrenheith

call=temperature()
if call is not None:
    fahrenheith_call=fahrenheith_convert(call)
    print(f"the fahrenheith of {call} is {fahrenheith_call}F.")