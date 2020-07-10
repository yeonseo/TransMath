from . import *

class Consulting(ListView):
    """ MainView Definition """

    name = "consulting"

    model = Board
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "boards"
