import hashlib
def hashGenerator(data):  #helper function to generate SHA256 hash
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:    
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
        hashlast=hashGenerator('gen_last')
        hashstart=hashGenerator('gen_hash')
    
        genesis=Block('gen_data',hashstart,hashlast)
        self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)
    
ad=Blockchain()
ad.add_block('1')
ad.add_block('2')
ad.add_block('3')  # 3 block system

for block in ad.chain:
    print(block.__dict__)  