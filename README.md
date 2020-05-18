# LiveNews
LiveNews - search and read news from all over the world.

# Extracted information

LiveNews extracts the following attributes from news articles. Also, have a look at an [Json format](https://newsapi.org/docs/endpoints/top-headlines) file fetched by LiveNews.

- headline
- lead paragraph
- main text
- main image
- name(s) of author(s)
- publication date
     


# Getting started
It's super easy, we promise!

## Frameworks and API
- [Django](https://www.djangoproject.com/start/) - python based framework to build web applications
- [Heroku](https://www.heroku.com/) - to deploy the application 
- [News API](https://newsapi.org) - News API is a simple HTTP REST API for searching and retrieving live articles from all over the web.

## Installation
LiveNews runs on Python 3.5+.

```
$ git clone https://github.com/vishnukumarra/LiveNews
```

## Acquiring Free API Key

Next step is getting a free API key at [News API](https://newsapi.org) which will help us make some call requests to the server and retrieve the news articles.

Once the api key is in your hands, go to ```/newsreader/views.py``` and paste it to where it said put “PUT_YOUR_API_KEY_HERE”.


## Features

- works out of the box: git clone and run in Django :-)
- easy to use
- short and crisp news format


# What's next?

Search for articles with any combination of the following criteria:

- Keyword or phrase. Eg: find all articles containing the word 'Microsoft'.
- Date published. Eg: find all articles published yesterday.
- Source name. Eg: find all articles by 'TechCrunch'.
- Source domain name. Eg: find all articles published on nytimes.com.
- Language. Eg: find all articles written in English.

Sort the results in the following orders:

- Date published
- Relevancy to search keyword
- Popularity of source
