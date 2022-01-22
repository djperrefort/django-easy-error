from django.conf import settings

from django_simple_error.factory import view_factory as _view_factory

for _error_code in getattr(settings, "SIMPLE_ERROR_CODES", range(400, 600)):
    globals()[f'handler{_error_code}'] = _view_factory(_error_code)
