from rest_framework import parsers, renderers, permissions, views, authentication, status
from rest_framework.response import Response
from utils.logging import get_exception_logger
from rest_framework.authtoken.models import Token

exception_logger = get_exception_logger()


class JSONApi(views.APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)

    # a wrapper function to handle exceptions and log them
    @staticmethod
    def api(func):
        def wrapper(self, request, *callback_args, **callback_kwargs):
            try:
                return func(self, request, *callback_args, **callback_kwargs)
            except Exception as e:
                exception_logger.exception("Exception: ".format(str(e)))
                return Response(data={"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return wrapper


class DeleteToken(JSONApi):
    @JSONApi.api
    def get(self, request):
        token = Token.objects.get(user_id=request.user.id)
        token.delete()
        return Response(data={"message": "Token deleted!"})

