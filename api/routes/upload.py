async def upload(file):
    # BUG: no file size limit
    content = await file.read()
    return {'size': len(content)}
