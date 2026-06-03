import uuid
def add_request_id(request, call_next):
    request.state.id = str(uuid.uuid4())
    response = call_next(request)
    response.headers['X-Request-ID'] = request.state.id
    return response
