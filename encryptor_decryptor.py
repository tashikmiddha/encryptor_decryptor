import rsa
#create public and private keys of 1024 bytes
# public_key,private_key=rsa.newkeys(1024)



#to create a file and store the public and private key in pem(privacy-enhanced mail) format
# with open("public_key.pem",'wb') as f:
#     f.write(public_key.save_pkcs1("PEM"))

# with open("private_key.pem",'wb')as f:
#     f.write(private_key.save_pkcs1("PEM"))


#read the keys from the files 
with open("public_key.pem",'rb')as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())

with open("private_key.pem",'rb')as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())

#signature 
message_sign="hello my name is tashik "
signature=rsa.sign(message_sign.encode(),private_key,"SHA-256")

with open("signature",'wb')as f:
    f.write(signature)

print(rsa.verify(message_sign.encode(),signature,public_key))  


#now input the message 
msg=input("enter the message here: ")

encrypted_message=rsa.encrypt(msg.encode(),public_key)


print(f"the encrypted message is: {encrypted_message}")


with open("encrypted.message",'wb')as f:
    f.write(encrypted_message)

clear_message=rsa.decrypt(encrypted_message,private_key)

print(f"The decrypted message is :{clear_message.decode()}")






