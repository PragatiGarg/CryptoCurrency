import os

from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client.crypto
testC = db['testCentralUser']

from Crypto.PublicKey import RSA

def defineUser(userName):
    directory = "/home/pragati/nsProject/cryptoCurrency/centralised/users/"+userName
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        return -1
    privateKey, publicKey = generate_RSA();
    privateKeyFile = directory + "/privateKey.pem"
    f = open(privateKeyFile, 'wb')
    f.write(privateKey)
    f.close()
    publicKeyFile = directory + "/publicKey.pem"
    f = open(publicKeyFile, 'wb')
    f.write(publicKey)
    f.close()
    dbResult = testC.insert_one({
    'userName': userName,
    'publicKey': publicKeyFile,
    'privateKey': privateKeyFile
    })
    return dbResult


def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    newKey = RSA.generate(bits, e=65537)
    publicKey = newKey.publickey().exportKey("PEM")
    privateKey = newKey.exportKey("PEM")
    return privateKey, publicKey


# privateKey, publicKey = generate_RSA();
# print (privateKey,publicKey)

flag = defineUser("test3");
if flag != -1:
    print("Done")
else:
    print("UserName already exists")
