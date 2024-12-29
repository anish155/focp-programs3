def name():
    character=input("enter the string:")
    return character
def remove_last_character(call):
    remove=call[:-1]
    print(remove)
call=name()
remove_last_character(call)