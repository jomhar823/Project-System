from functools import wraps
from django.http import HttpResponseForbidden

def mdrrmc_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.user_type == 'mdrrmc':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access Denied")
    return _wrapped_view
