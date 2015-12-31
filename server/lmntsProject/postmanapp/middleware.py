class CorsMiddleware(object):

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
        response['Content-Type'] = 'application/json'
        response['Accept'] = 'application/json'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
        return response