import hashlib
import json
from time import time

class Eth_trf(object):
    def __init__(self):
        self.queue = []
        self.transaction_queue = []

        self.new_block(previous_hash="1", proof=100)

        # Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the queue.

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

#Write Functions to Create New Transactions & Get the Last Block

#Search the blockqueue for the most recent block.


    @property
    def last_block(self):
 
        return self.queue[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.transaction_queue.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blocknodes = Eth_trf() 
User1 = blocknodes.new_transaction('Savanth','Mark','4 Eth')
User2 = blocknodes.new_transaction('Mark','Nicholas','10 ETH')
User3 = blocknodes.new_transaction('Nicholas','Savanth','100 ETH')
blocknodes.new_block(12345) #assigning the addrress to the block 

User1 = blocknodes.new_transaction('Savanth','Steyn','6 Eth')
User2 = blocknodes.new_transaction('Steyn','FAF','49 ETH')
blocknodes.new_block(687) #assigning the addrress to the block 

print("The Block Nodes computation: ",blocknodes.queue)