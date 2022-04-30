import hashlib
import json
from time import time

class Eth_trf(object):
    def __init__(self):
        self.queue = []
        self.transaction_queue = []

        self.new_block(previous_hash="1", proof=100)

        # Let's create a new block using dictionary data structure of storing the block information in key/value pairs

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.queue) + 1,
            'timestamp': time(),
            'transactions': self.transaction_queue,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.queue[-1]),
        }
        self.transaction_queue = []
        self.queue.append(block)

        return block

#Functions to help to create new transactions and retrive the latest block 

  #lets search if there is a node existing already from the recent block. 

    @property
    def last_block(self):
 
        return self.queue[-1]

#if the block is emtpy lets add the transaction with the information to the block - chain that we are creating the nodes for. It shows the list of the pending the tx's if exists 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.transaction_queue.append(transaction)
        return self.last_block['index'] + 1

#lets convert our string that we pass into uniocdes (for hashing purposes)

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)#converts the string to hash code using sha256 algorithm 
   
        hex_hash = raw_hash.hexdigest()#it converts the raw hash sha256 value to hex values

        return hex_hash
# parsing the values for the input
blocknodes = Eth_trf() 
User1 = blocknodes.new_transaction('Savanth','Mark','4 Eth')
User2 = blocknodes.new_transaction('Mark','Nicholas','10 ETH')
User3 = blocknodes.new_transaction('Nicholas','Savanth','100 ETH')
blocknodes.new_block(12345) #assigning the addrress to the block 

User1 = blocknodes.new_transaction('Savanth','Steyn','6 Eth')
User2 = blocknodes.new_transaction('Steyn','FAF','49 ETH')
blocknodes.new_block(687) #assigning the addrress to the block 

print("The Block Nodes computation: ",blocknodes.queue)
