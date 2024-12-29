def temperature():
    number=input("enter the number for temperature conversion:")
    check=number[-1]
    convert=number[:-1]
    convert=int(convert)
    if check=="C":
        return convert
    else:
        print("the given input didnt have C.")
        return None

def fahreheith_convert(fahreheith_call):
    fahreheith=(fahreheith_call*9/5)+32
    return fahreheith

fahreheith_call=temperature()
fahreheith=fahreheith_convert(fahreheith_call)
print(f"the fahreheith is {fahreheith}F")