import hashlib
import time

def proof_of_work_with_adjustment(target_time, initial_difficulty=4):
    difficulty = initial_difficulty
    target = '0' * difficulty
    nonce = 0
    
    while True:
        start_time = time.time()
        while True:
            hash_result = hashlib.sha256(f'{nonce}'.encode()).hexdigest()
            if hash_result[:difficulty] == target:
                elapsed_time = time.time() - start_time
                print(f'Block found! Nonce: {nonce}, Hash: {hash_result}, Time taken: {elapsed_time:.2f} seconds')
                break
            nonce += 1
      
        if elapsed_time < target_time:
            difficulty += 1
            print(f'Increasing difficulty to {difficulty}')
        elif elapsed_time > target_time:
            difficulty = max(1, difficulty - 1)
            print(f'Decreasing difficulty to {difficulty}')
        
        target = '0' * difficulty

proof_of_work_with_adjustment(target_time=2)
