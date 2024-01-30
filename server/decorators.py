from flask import request, abort


# decorator functions
def require_librarian(func):
    def wrapper(*args, **kwargs):
        # no formal authentication, check postman headers
        if request.headers.get("librarian") != "true":
            abort(403, "Permission denied. Only librarians can perform this action.")
        return func(*args, **kwargs)

    return wrapper
