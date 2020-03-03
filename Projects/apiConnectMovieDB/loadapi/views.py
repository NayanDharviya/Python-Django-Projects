from django.shortcuts import render
import requests
import datetime

# Create your views here
def popular_movies(request):
    url = "curl --request POST --header 'PRIVATE-TOKEN: dmc_XxbD6T_MWs8qqS6x' https://gitlab.example.com/api/v4/projects/1/issues"
    movieList = load_home_page(request, url)
    return render(request, "home.html", {'object_list': movieList})

def toprated_movies(request):
    url = "https://api.themoviedb.org/3/movie/top_rated?api_key=20d9d143411982b2f70ebb9f8ee6d3cb"
    movieList = load_home_page(request, url)
    return render(request, "home.html", {'object_list': movieList})

def upcoming_movies(request):
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=20d9d143411982b2f70ebb9f8ee6d3cb"
    movieList = load_home_page(request, url)
    return render(request, "home.html", {'object_list': movieList})

def nowplaying_movies(request):
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=20d9d143411982b2f70ebb9f8ee6d3cb"
    movieList = load_home_page(request, url)
    return render(request, "home.html", {'object_list': movieList})

def load_home_page(request, url):
    r = requests.get(url)
    data = r.json()
    movieList = []
    for movies in data["results"]:
        movieList.append({
            'id':movies['id'], 
            'name':movies['title'],
            'date': datetime.datetime.strptime(movies['release_date'], "%Y-%m-%d").strftime("%d %b, %Y"),
            'description':movies['overview'],
            'imgurl':"https://image.tmdb.org/t/p/w185_and_h278_bestv2" + (movies['poster_path'] or movies['backdrop_path'])
            })
    return movieList
    