# BUG: pool not closed on shutdown
pool = None
async def get_pool():
    global pool
    if pool is None:
        pool = await create_pool()
    return pool
