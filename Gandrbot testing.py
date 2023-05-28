import random

token_types=[]
message = ""

while message != "quit":
    message = input("talk to gandr: ")

    if message.startswith("/EW"):
        print(random.randrange(1,11))

    elif message.startswith("/token"):
        token_type = ""
        for t in token_types:
            if message == t:
                token_type = message
        if token_type == "":
            new_token = message
            token_types.append(message)
            print("added " + message + " to the list of token types")
        print(token_type)
print("ok, bye")