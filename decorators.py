from functools import wraps


def Secured(param: str):
    # @wraps
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            print("start for " + param)
            if kwargs["role"] == param:
                r = await func(*args, **kwargs)
            else:
                r = {"error_message": "Unauthorized " + kwargs["role"] + ", " + param + " is needed"}
            print("end for " + param)
            return r
        return wrapper

    return decorator