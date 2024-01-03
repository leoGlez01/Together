from django.middleware.csrf import CsrfViewMiddleware

class WebSocketCSRFMiddleware(CsrfViewMiddleware):
    def _accept_websocket(self, request):
        return request.META.get('HTTP_SEC_WEBSOCKET_PROTOCOL', '').lower() == 'websocket'

    def _reject(self, request, reason):
        if not self._accept_websocket(request):
            super()._reject(request, reason)

    def _accept(self, request):
        if self._accept_websocket(request):
            return True
        return super()._accept(request)