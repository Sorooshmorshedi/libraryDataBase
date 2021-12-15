from django.urls import path
from .views import book_lib, apis, books_list, detail, GetAllData, GetFavData, UpdateFavData, PostModelData, PostData, search 

app_name = 'mylib'
urlpatterns = [
	path('books/', book_lib, name = 'books'),
	path('book-list/', books_list ),
	path('api/', apis ),
	path('get-all-data/', GetAllData.as_view()),
	path('get-fav-data/', GetFavData.as_view()),
	path('update-fav-data/<int:pk>/', UpdateFavData.as_view()),
	path('post-model/', PostModelData.as_view()),
	path('post-data/', PostData.as_view()),
	path('search/', search.as_view()),	
	path('<slug>/', detail, name ='det'),
]
	

