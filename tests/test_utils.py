from unittest import TestCase

from django.test import RequestFactory

from django_easy_error.utils import error_render


class TestRenderedResponse(TestCase):
    """Tests for responses rendered by the ``error_render`` function"""

    def test_correct_status_code(self) -> None:
        """Test returned views render the correct error code"""

        request = RequestFactory().request()
        for http_code in (404, 403, 404, 500):
            response = error_render(http_code, request)
            self.assertEqual(http_code, response.status_code)
