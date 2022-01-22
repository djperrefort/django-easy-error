"""Defines ``View`` objects for converting web requests into rendered responses."""

from django.shortcuts import render


def _handler_factory(template: str, error_code: int) -> callable:
    """Build a function based view for handling HTTP error pages"""

    def handler(request, *args, **kwargs):
        return render(request, template, status=error_code, context={'error_code': error_code})

    return handler


for _error_code in range(400, 600):
    globals()[f'handler{_error_code}'] = _handler_factory('error_pages/error_page.html', _error_code)
