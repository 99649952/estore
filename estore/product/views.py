from django.template.response import TemplateResponse


def home(request):
    context = {"name": "lxb"}
    return TemplateResponse(request, 'home.html', context)
