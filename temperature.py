def temperature():
    number=float(input("enter the number for temperature conversion:"))
    return number
def temperature2():
    number=float(input("enter the number for temperature conversion:"))
    return number
def celsius_convert(celsius_call):
    celsius=(celsius_call-32)*5/9
    return celsius
def fahreheith_convert(fahreheith_call):
    fahreheith=(fahreheith_call*9/5)+32
    return fahreheith
celsius_call=temperature()
fahreheith_call=temperature2()
celsius=celsius_convert(celsius_call)
fahreheith=fahreheith_convert(fahreheith_call)
print(f"the celsius is{celsius},the fahreheith is{fahreheith}")