alphabet="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
index=0

def encrypt():
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
    ent=input("Press enter to continue")


def decrypt():
    message= input("Enter the message you want to decrypt: \n")
    word = input("Enter a word that appears in coded message: \n")
    key=0
    new_message = ""
    coded_word= ""

    for i in range (len(alphabet)):
        for letter in word:
            index = alphabet.find(letter)
            if index != -1:
                index=alphabet.find(letter)
                coded_word= coded_word + alphabet[index+i]
            else:
                coded_word=coded_word + letter
                continue
        check = message.find(coded_word)
        if check == -1:
            continue
        else:
            key = i

    for letter in message:
        index = alphabet.find(letter)
        if index != -1:
            index=alphabet.find(letter)
            new_message= new_message + alphabet[index-key]
        else:
            new_message=new_message + letter
            continue

    print ("Your message is:\n", new_message)
    input("Press enter to continue")


entry = 0
while entry == 0:
    choice = input("Enter 'e' for encode, 'd' for decode or 'q' for quit: \n")

    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
    elif choice == 'q':
        entry = 1
        print ("Goodbye")
    else:
        entry = 0
