from contextlib import contextmanager
import time
@contextmanager
def timer_context():
    print("Starting...")
    start = time.time()
    yield
    end = time.time()
    print(f"Finished! Took {end - start:.2f} seconds")
    
with timer_context():
    time.sleep(2)
    print("Hello, World!")
