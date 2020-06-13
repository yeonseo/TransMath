from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Board
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "boards"


class BoardDetail(DetailView):

    """ BoardDetail Definition """

    model = models.Board


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                board_type = form.cleaned_data.get("board_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if board_type is not None:
                    filter_args["board_type"] = board_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Board.objects.filter(
                    **filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                boards = paginator.get_page(page)

                return render(
                    request, "boards/search.html", {
                        "form": form, "boards": boards}
                )

        else:
            form = forms.SearchForm()

        return render(request, "boards/search.html", {"form": form})


class EditBoardView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Board
    template_name = "boards/board_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "board_type",
        "amenities",
        "facilities",
        "house_rules",
    )

    def get_object(self, queryset=None):
        board = super().get_object(queryset=queryset)
        if board.host.pk != self.request.user.pk:
            raise Http404()
        return board


class BoardPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Board
    template_name = "boards/board_photos.html"

    def get_object(self, queryset=None):
        board = super().get_object(queryset=queryset)
        if board.host.pk != self.request.user.pk:
            raise Http404()
        return board


@login_required
def delete_photo(request, board_pk, photo_pk):
    user = request.user
    try:
        board = models.Board.objects.get(pk=board_pk)
        if board.host.pk != user.pk:
            messages.error(request, "Cant delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("boards:photos", kwargs={"pk": board_pk}))
    except models.Board.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "boards/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        board_pk = self.kwargs.get("board_pk")
        return reverse("boards:photos", kwargs={"pk": board_pk})


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    template_name = "boards/photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("boards:photos", kwargs={"pk": pk}))


class CreateBoardView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateBoardForm
    template_name = "boards/board_create.html"

    def form_valid(self, form):
        board = form.save()
        board.host = self.request.user
        board.save()
        form.save_m2m()
        messages.success(self.request, "Board Uploaded")
        return redirect(reverse("boards:detail", kwargs={"pk": board.pk}))
