from django.views import debug


def _patch_django_debug_view():

    new_data = """
        <h3 style="margin-bottom:10px;">
            <a href="https://www.google.com.tr/#q=site:stackoverflow.com+django+{{ exception_value|force_escape }}"
             target="_blank">View in Stackoverflow</a>
        </h3>
    """

    replace_point = '<table class="meta">'
    replacement = new_data + replace_point

    # monkey path the built-in template.
    debug.TECHNICAL_500_TEMPLATE = debug.TECHNICAL_500_TEMPLATE.replace(
        replace_point,
        replacement,
        1  # replace the first occurence
    )


class DjangoStackoverTraceMiddleware(object):

    def __init__(self):
        _patch_django_debug_view()

    def process_response(self, request, response):
        return response
