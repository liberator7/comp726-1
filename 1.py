import hashlib
import time

def proof_of_work(difficulty):
    target = '0' * difficulty
    nonce = 0
    while True:
        hash_result = hashlib.sha256(f'{nonce}'.encode()).hexdigest()
        if hash_result[:difficulty] == target:
            print(f'Block found! Nonce: {nonce}, Hash: {hash_result}')
            return nonce
        nonce += 1

start_time = time.time()
proof_of_work(difficulty=4)
print(f'Time taken: {time.time() - start_time} seconds')

start_time = time.time()
proof_of_work(difficulty=5)
print(f'Time taken: {time.time() - start_time} seconds')
