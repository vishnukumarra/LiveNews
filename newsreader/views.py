from django.shortcuts import render
from newsapi import NewsApiClient
import django_filters.rest_framework




def Index(request):
    newsapi = NewsApiClient(api_key="3261097a702947809aad72c0ab3c2291")
    topheadlines = newsapi.get_top_headlines(country="in")
    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


         

    mylist = zip(news, desc, img)


    return render(request, 'mainpage.html', context={"mylist":mylist,})



def bbc(request):
    newsapi = NewsApiClient(api_key="3261097a702947809aad72c0ab3c2291")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'newspage.html', context={"mylist":mylist})
