letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    ciper_text=""
    for char in text:
        if char in letters:
            position=letters.index(char)
            new_position=(position+shift_key)%26
            ciper_text+=letters[new_position]
        else:
            ciper_text+=char
    print(f"Encrypted text : {ciper_text}")


def decryption(ciper_text,shift_key):
    plain_text=""
    for char in text:
        if char in letters:
            position=letters.index(char)
            new_position=(position-shift_key)%26
            plain_text+=letters[new_position]
        else:
            plain_text+=char
    print(f"Decrypted text : {plain_text}")

end=False
while not end :
    what_to_do=input("Type 'encrypt' for encryption and type 'decrypt' for decryption : ")
    text=input("Enter ur text : ").lower()
    shift_key=int(input("Enter shift key : "))
    if what_to_do=="encrypt":
        encryption(text,shift_key)
    elif what_to_do=="decrypt":
        decryption(text,shift_key)
    play_again=input("Type 'yes' to continue and 'no' to exit : ")
    if play_again=='no':
        end=True
        print("Well played Bye......") 