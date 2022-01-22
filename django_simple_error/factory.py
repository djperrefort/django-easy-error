from django.http import HttpRequest
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views import View


def view_factory(error_code: int) -> callable:
    """Factory function for creating class based django views that render custom error tempaltes

    Args:
        error_code: The error code handled by the view
    """

    def get(self, request: HttpRequest, *args, **kwargs) -> None:

        try:
            template = 'django_simple_error/http_{}.html'.format(error_code)
            get_template(self.template_name)

        except TemplateDoesNotExist:
            template = 'django_simple_error/default.html'

        return render(request, template, status=error_code, context={'error_code': error_code})

    return type('HttpError{}View', (object, View), {'get': get})
