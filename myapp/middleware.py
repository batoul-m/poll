class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
class MyAdvancedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Middleware before specific view")
        return None

    def process_exception(self, request, exception):
        print("Error happened:", exception)
        return None

    def process_template_response(self, request, response):
        response.context_data['middleware_note'] = "Processed by middleware"
        return response
