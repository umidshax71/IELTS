from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import IELTS


# View metodida - 2xil usul bor


# 1) Agar html fayllar bittani ichida ishlailsa - index funksiya metodidan foydalaniladi

# 2) Agar html fayl ko'p bo'lsa - ListView klasslik metoddan foydalanamiz


# class PortfoliyomViews(ListView):
#     model = Portfolio
#     context_object_name = 'portfolio'
#     template_name = 'index.html'

def index(request):
    ielts = IELTS.objects.all()

    contex = {
        'Ielts': ielts,


    }
    return render(request, ['index.html'], contex)