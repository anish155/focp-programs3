def name_input():
    name=input("enter your name:")
    return name
def character_count(call):
    print(f"the letter {call} has:")
    uppercase=0
    lowercase=0
    for char in call:
        if char.isupper():
            uppercase+=1
        if char.islower():
            lowercase+=1   
    return uppercase,lowercase
call=name_input()
count=character_count(call)
print(count)
