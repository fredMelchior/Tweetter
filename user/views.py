from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template import loader


from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    lookup_field = "id"
    serializer_class = ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "profile.html"

    def get(self, request, id):
        queryset = Profile.objects.get(id=id)
        return Response({"profile": queryset})

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    # def user_profile(request, id):
    #     profile = Profile.objects.get(id=id)
    #     template = loader.get_template("profile.html")
    #     context = {
    #         "profile": profile,
    #     }
    #     return HttpResponse(template.render(context, request))


def all_users(request):
    users = get_user_model().objects.all().values()
    template = loader.get_template("all_users.html")
    context = {
        "users": users,
    }
    return HttpResponse(template.render(context, request))
