from django.core.cache import cache
from django.http import HTTPResponse



def global_cache_page(cache_timeout: int):
    def decorator_function(view_function):
        def wrapper_function(*args, **kwargs):
            request = args[0]
            if cache.get(request.get_full_path()) is None:
                result = view_function(*args, **kwargs)
                cache.set(request.get_full_path(), result.content, cache_timeout)
                return result
            return HTTPResponse(result.content)
        return wrapper_function
    return decorator_function


