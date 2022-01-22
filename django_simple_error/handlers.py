from django.conf import settings

from django_simple_error.factory import view_factory as _view_factory

settings.configure()

__all__ = []
for error_code in getattr(settings, "SIMPLE_ERROR_CODES", range(400, 600)):
    handler = 'handler{}'.format(error_code)
    __all__.append(handler)
    globals()[handler] = _view_factory(error_code)

del handler
del error_code