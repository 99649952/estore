from django.template.response import TemplateResponse


def home(request):
    context = {"name": "lxb"}
    return TemplateResponse(request, 'home.html', context)


def handle_404(request):
    return TemplateResponse(request, '404.html', status=404)
