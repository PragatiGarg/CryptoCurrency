import datetime;
from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client.crypto
testUser = db['testCentralUser']
testCoin = db['testCentralCoin']
def initialiseCoin(userName, coinValue):
    serialNumber = 0
    ts = datetime.datetime.now().timestamp()
    # print(ts)
    coinId = int(ts*65537)
    byteCoinId = (coinId).to_bytes((coinId.bit_length() + 8), byteorder='big')
    serialNumber = serialNumber + 1
    coin = str(coinId)+"-"+str(serialNumber);
    signature = signUsingKey(userName,b64encode(byteCoinId))
    dbResult = testCoin.insert_one({
    'userName': userName,
    'coinId': coinId,
    'coin': coin,
    'coinValue': coinValue,
    'signature': signature
    })


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

def signUsingKey(userName,data):
    user = testUser.find_one({'userName':userName})
    privateKeyFile = user['privateKey']
    publicKeyFile = user['publicKey']
    privateKey = open(privateKeyFile, "r").read()
    # print(privateKey)
    rsakey = RSA.importKey(privateKey)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
    digest.update(b64decode(data))
    sign = signer.sign(digest)
    return b64encode(sign)


initialiseCoin("test1",2.5)
