#project:caesar cipher encryption and decryption
#plaintext converting to ciphertext
alphabet=['a','b','c','d','e','f','g','h'
          ,'i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z']

#for encryption
def encryption(text,key):
    cipher_text=''
    for char in text:
        position=alphabet.index(char)
        new_position=(position+key)%26
        cipher_text+=alphabet[new_position]
    print(f"here is your encrypted test:{cipher_text}")

#for decryption
def  decryption(text,key) :
     decryption_text='' 
     for char in text:
         position=alphabet.index(char)
         new_position=(position-key)%26
         decryption_text+=alphabet[new_position]
     print(f"here is your decrypted text:{decryption_text}")

      
text=input("enter your text(lower case only):").lower()
key=int(input("enter your key:"))
print("What do you want to do?(1.Encrypt,2.Decrypt)")
choice=int(input())
if choice==1:
    encryption(text,key)
elif choice==2:
    decryption(text,key)    
