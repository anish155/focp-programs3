def number():
    integer=int(input("enter a number:"))
    return integer
def check_number(call):
    if call in range(1,101):
        return True
    else:
        return False
call=number()
check_call=check_number(call)
print(check_call)