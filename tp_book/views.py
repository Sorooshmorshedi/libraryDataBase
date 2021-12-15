#######IMPORTS########
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookModelSerializer, BookSerializer
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

#This is first page's view
def index(request):
	avalible = Book.objects.count()
	template = loader.get_template('tp_book/index.html')
	args = {'cnt': avalible}
	return HttpResponse(template.render(args, request))

#This is library page's view	
def book_lib(request):
	books = Book.objects.all()
	cnt = Book.objects.count()
	template = loader.get_template('tp_book/books.html')
	args = {'books': books, 'cnt': cnt}
	return HttpResponse(template.render(args, request))
	
#This is detail page's view for any book of library
def detail(request, slug):
	book = Book.objects.get(slug = slug)
	template = loader.get_template('tp_book/detail.html')
	args = {'book': book}
	return HttpResponse(template.render(args, request))

#This view is for list of books page whit print styles
def books_list(request):
	books = Book.objects.all()
	avalible = Book.objects.count()
	template = loader.get_template('tp_book/book-list.html')
	args = {'books': books, 'cnt': avalible}
	return HttpResponse(template.render(args, request))
	
#This is APIs page's view	
def apis(request):
	template = loader.get_template('tp_book/apis.html')
	args = {'a': 1}
	return HttpResponse(template.render(args, request))			

#___________________API____________________

class GetAllData(APIView):
	'''do get request and this is return all book in library'''
	def get(self, request):
		query = Book.objects.all()
		serializers = BookModelSerializer(query, many=True, context = {'request': request})
		return Response(serializers.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
	'''do get request and this is return all fav book in library'''
	def get(self, request) :
		query =Book.objects.filter(fav=True)
		serializers = BookModelSerializer(query, many=True)
		return Response(serializers.data, status=status.HTTP_200_OK)

		
class UpdateFavData(APIView):
	'''this is for Update books
	do get request and this is return all book in library
	do PUT request and this is Update a book in library
	'''
	def get(self, request, pk):
		query = Book.objects.get(pk = pk)
		serializers = BookModelSerializer(query)
		return Response(serializers.data, status=status.HTTP_200_OK)
	def put(self, request, pk):
		query = Book.objects.get(pk=pk)
		serializers = BookModelSerializer(query, data=request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
	
	
class PostModelData(APIView):
	'''do POST request and this is Create a book in library'''
	def post(self, request):
		serializer = BookModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		
class PostData(APIView):
	'''do POST request with all fiels and this is Create a book in library'''
	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			store_name = serializer.data.get('store_name')
			description = serializer.data.get('description')
			image = request.FILES['image']
			fav = serializer.data.get('fav')
		else :
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		book = Book()
		book.name = name
		book.store_name = store_name
		book.description = description
		book.image = image
		book.fav = fav
		book.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
				
class search(APIView):
	'''give ID and do get request and this is search in library and return Book'''
	def get(self, request):
		search = request.GET['id']
		query = Book.objects.filter(id=search)
		serializer = BookModelSerializer(query, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)   
		

			

