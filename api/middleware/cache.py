# BUG: sets no-cache on all routes including public static
def cache_middleware(response):
    response.headers['Cache-Control'] = 'no-store'
    return response
