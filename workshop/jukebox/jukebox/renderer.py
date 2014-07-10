from rest_framework.renderers import JSONRenderer

class PrettyJSONRenderer(JSONRenderer):
    """
    JSON renderer with pretty-print by default
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if (renderer_context 
            and 'indent' not in renderer_context):
            renderer_context = {'indent': 4}

        return super().render(data, 
                              accepted_media_type=accepted_media_type,
                              renderer_context=renderer_context) 
