from django.views import debug
from django.conf import settings


def get_search_link():
    default_choice = "stackoverflow"

    search_urls = {
        "stackoverflow": "http://stackoverflow.com/search?q=[python] or "
                         "[django]+{{ exception_value|force_escape }}",
        "googlesearch": "https://www.google.com.tr/#q="
                        "+django+{{ exception_value|force_escape }}"
    }

    search_url = getattr(
        settings,
        'DJANGO_STACKOVERFLOW_TRACE_SEARCH_SITE',
        default_choice
    )

    return search_urls.get(search_url, search_urls[default_choice])


def _patch_django_debug_view():

    new_data = """
        <h3 style="margin-bottom:10px;">
            <a href="%s"
             target="_blank">View in Stackoverflow</a>
        </h3>
    """ % get_search_link()

    replace_point = '<table class="meta">'
    replacement = new_data + replace_point

    # monkey patch the built-in template.
    debug.TECHNICAL_500_TEMPLATE = debug.TECHNICAL_500_TEMPLATE.replace(
        replace_point,
        replacement,
        1  # replace the first occurence
    )


class DjangoStackoverTraceMiddleware(object):

    def __init__(self):
        if settings.DEBUG:
            _patch_django_debug_view()

    def process_response(self, request, response):
        return response
