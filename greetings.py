def greetings():
    name=input("enter your name:")
    return name
def greet(call):
    call=call.capitalize()
    print(f"hello {call}.")
call=greetings()
greet(call)