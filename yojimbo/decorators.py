import requests
from functools import wraps

new_endpoint = "http://localhost:8712"

def intercept(func):
    """
    Decorator function that intercepts and modifies API calls
    """
    # @wraps(func)
    def wrapper(*args, **kwargs):
        modified_kwargs = dict(kwargs)
        
        modified_kwargs['url'] = new_endpoint
        
        result = func(*args, **modified_kwargs)
        return result
    
    return wrapper

