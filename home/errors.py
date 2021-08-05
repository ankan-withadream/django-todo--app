from django.shortcuts import redirect
from django.contrib import messages


def error_404(request, exception):
    messages.error(request, "Error 404: Not found :(")
    return redirect("/todos")


def error_500(request):
    messages.error(request, "Error 500: Server failed to process your request :(")
    return redirect("/todos")

        
def error_403(request, exception):
    messages.error(request, "Error 403: Authorization error :(")
    return redirect("/todos")


def error_400(request,  exception):
    messages.error(request, "Error 400: Request must be incorrect of corrupt :(")
    return redirect("/todos")