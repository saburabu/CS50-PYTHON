import time
import numpy as np

start_time = time.time()

# Doing the exact same math, but optimized
total = np.sum(np.arange(10_000_000, dtype=np.int64))

end_time = time.time()
print(f"Optimized time: {end_time - start_time:.4f} seconds!")
