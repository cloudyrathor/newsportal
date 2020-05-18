from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def movie_news_view(request):
    news1 = 'News one is good'
    news2 = 'News two is good'
    news3 = 'News three is good'
    news4 = 'News four is good'
    news5 = 'News five is good'
    my_dict = {'news1':news1,
               'news2':news2,
               'news3':news3,
               'news4':news4,
               'news5':news5,}
    return render(request,'testapp/movie_news.html',my_dict)