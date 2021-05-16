from pprint import pprint

from main import Blockchain

blockchain = Blockchain()
t1 = blockchain.new_transaction("Seneca", "Yassine", "5 BTC")
t2 = blockchain.new_transaction("Cesar", "Julien", "2 BTC")
t3 = blockchain.new_transaction("Louette", "Yassine", "10 BTC")
blockchain.new_block(12345)

t1 = blockchain.new_transaction("Pierre", "Tristan", "5 BTC")
t2 = blockchain.new_transaction("Julien", "Hamza", "2 BTC")
t3 = blockchain.new_transaction("Tristan", "Yassine", "10 BTC")
blockchain.new_block(6789)

pprint(blockchain.chain)
