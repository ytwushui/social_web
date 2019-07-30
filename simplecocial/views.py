# view for the home page and link it to urls for the intile page
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"
    # the way to use views to create link to html then add the url to urls
    # for the entile page
    def get(self, request, *args, **kwargs):
        #if request.user.is_authenticated():
            #return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
