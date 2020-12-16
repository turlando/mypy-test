from datetime import datetime

# should not type check
def now() -> str:
    return datetime.now()
