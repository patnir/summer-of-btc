"""
blocks - set of transactions 

Transaction: 
    fee: number
    weight: number
    parent_transactions: Transaction[]
    time: timestamp, probably? 


Miner selects Transactions[] Ordered (by time probably) where sum(Transactions.weight) < max block weight

    allow Transaction[] where Transaction.parent_transactions.all.timestamps() < specific transaction .timestamp


Goal: Miner has a block with the fattest fees lololol


Question: 
1. what is the point of the weights
2. 
"""