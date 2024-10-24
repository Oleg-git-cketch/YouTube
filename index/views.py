from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import User, Video


# Create your views here.
def home_page(request):
    # Достаем данные из БД
    videos = Video.objects.all()
    # Отправляем данные на фронт
    context = {'videos': videos}

    return render(request, 'home.html', context)


def video_page(request, pk):
    # Достаем данные из БД
    video = Video.objects.get(id=pk)
    # Отправляем данные на фронт
    context = {'video': video}
    return render(request, 'video.html', context)

def user_page(request):
    user = User.objects.all()
    context = {'user': user}

    return render(request, 'user.html', context)

def comment_page(request):
    comment = Comment.objects.all()
    context = {'comment': comment}

    return render(request, 'comment.html', context)
