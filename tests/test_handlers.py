from importlib import reload
from unittest import TestCase

from django.test import override_settings

from django_simple_error import handlers


class HandlerDefinitions(TestCase):
    """Tests the dynamic definition of error code handlers"""

    def test_default_handlers_are_defined(self) -> None:
        """Test views are defined only for HTTP error codes from 400 through 599"""

        for i in range(0, 400):
            self.assertFalse(hasattr(handlers, f'handler{i}'))

        for i in range(400, 600):
            self.assertTrue(hasattr(handlers, f'handler{i}'))

    def test_overridden_settings(self) -> None:
        """Test views are created dynamically based on application settings"""

        with override_settings(SIMPLE_ERROR_CODES=[200, 201]):
            reload(handlers)

            self.assertFalse(hasattr(handlers, f'handler{199}'))
            self.assertTrue(hasattr(handlers, f'handler{200}'))
            self.assertTrue(hasattr(handlers, f'handler{201}'))
            self.assertFalse(hasattr(handlers, f'handler{203}'))

        reload(handlers)
