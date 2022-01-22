"""A django application for displaying custom error messages."""

from django.conf import settings

__version__ = '0.0.1'
__author__ = 'Daniel Perrefort'

# Allow reloading of the module without Django raising an error
# This is useful for running tests against different app settings
# and is required for compatibility as a pluggable application
try:
    settings.configure()

except RuntimeError:
    pass
