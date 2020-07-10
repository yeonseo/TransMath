from . import *

class Main(APIView):
    name = "main"

    permission_classes = [AllowAny]
    @staticmethod
    def get(request):
        return Response(data={'Main': 1}, status=status.HTTP_200_OK)
