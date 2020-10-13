from django.http import JsonResponse
from django.shortcuts import render

from .forms import CalcForm


def index(request):
    return render(request, "core/index.html")


def calc_form(request):
    """Stupid basic form example"""
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            num_left = form.cleaned_data["num_one"]
            num_right = form.cleaned_data["num_two"]
            answer = num_left + num_right
            return JsonResponse({"answer": answer})
    form = CalcForm()
    context = {"form": form}

    return render(request, "core/form_calc.html", context)


def health(request):
    """Health monitoring url"""
    return JsonResponse({"status": "OK", "status_code": 200})


def help(request):
    return render(request, "core/help.html")
