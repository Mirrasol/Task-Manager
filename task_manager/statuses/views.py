from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
