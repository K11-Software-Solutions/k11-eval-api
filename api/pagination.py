def paginate(query, limit=20, offset=0):
    return query.offset(offset).limit(limit)
