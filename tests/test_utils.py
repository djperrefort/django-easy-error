from django.conf import settings
from django.test import RequestFactory, TestCase

from django_simple_error.utils import error_render


class TestRenderedResponse(TestCase):
    """Tests for responses rendered by the ``error_render`` function"""

    def test_correct_status_code(self) -> None:
        """Test returned views render the correct error code"""

        request = RequestFactory().request()
        for http_code in (404, 403, 404, 500):
            response = error_render(http_code, request)
            self.assertEqual(http_code, response.status_code)

    def test_rendered_context(self) -> None:
        """Test responses include the error code end descriptions in the context"""

        request = RequestFactory().request()
        for http_code in (404, 403, 404, 500):
            response = error_render(http_code, request)
            expected_desc = settings.ERROR_CODE_DESCRIPTIONS[http_code]
            expected_long_desc = settings.ERROR_CODE_DESCRIPTIONS_LONG[http_code]

            self.assertEqual(http_code, response.content.context['error_code'])
            self.assertEqual(expected_desc, response.content.context['description'])
            self.assertEqual(expected_long_desc, response.content.context['description_long'])
