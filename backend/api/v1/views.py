from rest_framework import viewsets


class BaseApiView(viewsets.ViewSet):

    #authentication_classes = [TokenAuthentication]

    def health(self, request, *args, **kwargs):
        """ Healthcheck """

        return Response({
            "status": "healthy",
        })
