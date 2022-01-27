def validate_files(request, field, update=False):
    """
    
    :params
    :request: request.data
    :field: key of file
    
    """
    request._mutable = True
    if update:
        if type(request[field]) == str:
            del request[field]
    else:
        request[field] = None if type(request[field]) == str else request[field]
    request._mutable = False
    return request
