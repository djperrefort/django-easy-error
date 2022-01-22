from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views import View


def view_factory(error_code: int) -> callable:
    """Factory function for creating class based django views that render custom error templates

    Args:
        error_code: The error code handled by the view
    """

    try:
        template = f'django_simple_error/http_{error_code}.html'
        get_template(template)

    except TemplateDoesNotExist:
        template = 'django_simple_error/default.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Respond to an incoming HTTP request

        Args:
            request: The response to respond to

        Returns:
            A rendered HML response
        """

        return render(request, template, status=error_code, context={'error_code': error_code})

    return type(f'HttpErrorView{error_code}', (View,), {'get': get})
