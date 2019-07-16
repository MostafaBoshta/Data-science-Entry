message = "hello world"
print(message)
print(len(message))
print(message[:5])
print(message[5:])
print(message.lower())
print(message.upper())
print(message.count("l"))
print(message.find("world"))
message = message.replace("world" , "universe")
print(message)
greeting ="Hello"
name = "Mostafa"
message= "{} , {} . welcome!".format(greeting , name)
print(message)
message = greeting +" , "+name
print(message)
message = f"{greeting} , {name} . welcome! "
print(message)
