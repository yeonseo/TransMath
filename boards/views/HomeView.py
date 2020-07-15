from . import *

class HomeView(ListView):
    name = "home"

    model = Board
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "boards"

class HomeDetail(DetailView):

    """ Detail Definition """
    name = "detail"

    model = Board

# class HomeView(APIView):
# #     name = "home"
# #
# #     permission_classes = [AllowAny]
# #
# #     @staticmethod
# #     def get(request):
# #         return Response(data={'Main': 1}, status=status.HTTP_200_OK)