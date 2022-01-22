import inspect
from unittest import TestCase

from django_simple_error import handlers


class HandlerSignatures(TestCase):
    """Test handlers have compatible signatures with django"""

    @staticmethod
    def get_argument_names(func: callable) -> tuple:
        """Return a tuple of argument names taken by the given callable"""

        signature = inspect.signature(func)
        arg_names = tuple(signature.parameters.keys())
        return arg_names

    def test_4xx_errors(self) -> None:
        """Test errors 400, 403, and 404"""

        for error_code in (400, 403, 404):
            handler = getattr(handlers, f'handler{error_code}')
            arg_names = self.get_argument_names(handler)
            self.assertEqual(('request', 'exception'), arg_names)

    def test_500_error(self) -> None:
        """Test error 500"""

        handler = getattr(handlers, 'handler500')
        arg_names = self.get_argument_names(handler)
        self.assertEqual(('request',), arg_names)
