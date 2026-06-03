from collections import defaultdict
import time
RATE_LIMIT = 100
WINDOW = 60
counters = defaultdict(list)
def check_rate_limit(ip: str) -> bool:
    now = time.time()
    counters[ip] = [t for t in counters[ip] if now - t < WINDOW]
    if len(counters[ip]) >= RATE_LIMIT:
        return False
    counters[ip].append(now)
    return True
