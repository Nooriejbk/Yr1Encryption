alphabet="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
index=0

message= input("Enter the message you want to encrypt: \n")
key = int(input("Enter a key you would like to encrypt by: \n"))
new_message = ""

for letter in message:
    print("boop")
    index = alphabet.find(letter)
    if index != -1:
        index=alphabet.find(letter)
        new_message= new_message + alphabet[index+key]
    else:
        new_message=new_message + letter
        continue

print ("Your new message is:\n", new_message)


