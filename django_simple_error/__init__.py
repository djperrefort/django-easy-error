"""A django application for displaying custom error messages."""

from django.conf import settings

__version__ = '0.0.1'
__author__ = 'Daniel Perrefort'

# Allow reloading of the module without Django raising an error
# This is useful for running tests without a running django server
try:
    settings.configure()

except RuntimeError:
    pass

# Set default setting values
try:
    getattr(settings, 'ERROR_CODE_DESCRIPTIONS')

except AttributeError:
    setattr(settings, 'ERROR_CODE_DESCRIPTIONS', {
        400: 'Bad Request.',
        403: 'Forbidden.',
        404: 'Page not found.',
        500: 'Internal Server Error.'
    })

try:
    getattr(settings, 'ERROR_CODE_DESCRIPTIONS_LONG')

except AttributeError:
    setattr(settings, 'ERROR_CODE_DESCRIPTIONS_LONG', {
        400: 'The server could not process your request.',
        403: 'You are not authorized for access to the requested content.',
        404: 'The server can\'t find the resource you requested.',
        500: 'The server has encountered a situation it does not know how to handle.',
    })
