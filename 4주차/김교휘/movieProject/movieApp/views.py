from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movieApp.models import Movie, Review
from movieApp.serializers import MovieSerializer,MovieReviewSerializer

class MovieListView(APIView):
    def get(self, request):
      movies = Movie.objects.all()
      serializer = MovieSerializer(movies, many=True)
      return Response(serializer.data)
    
    def post(self, request):
      serializer = MovieSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailView(APIView):
  def get(self, request, id):
      try:
        movie = Movie.objects.get(id=id)
      except Movie.DoesNotExist:
        return Response({'Error': '없는 영화입니다.'}, status=status.HTTP_400_BAD_REQUEST)
      serializer = MovieSerializer(movie)
      return Response(serializer.data)
  
  def put(self, request, id):
      try:
        movie = Movie.objects.get(id=id)
      except Movie.DoesNotExist:
        return Response({'Error': '없는 영화입니다.'}, status=status.HTTP_400_BAD_REQUEST)
      serializer = MovieSerializer(movie, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else:
        return Response(serializer.errors)
      
  def delete(self, request, id):
      try:
        movie = Movie.objects.get(id=id)
      except Movie.DoesNotExist:
        return Response({'Error': '없는 영화입니다.'}, status=status.HTTP_400_BAD_REQUEST)
      movie.delete()
      return Response(status=status.HTTP_200_OK)
  
class MovieReviewListView(APIView):
  def get(self, request, id):
    try:
      movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
      return Response({'Error': '없는 영화입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    reviews = movie.reviews.all()
    serializer = MovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)
  
  def post(self, request, id):
    pass

class MovieReviewDetailView(APIView):
  def get(self, request, id, review_id):
    try:
      review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
      return Response({'Error': '없는 리뷰입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = MovieReviewSerializer(review)
    return Response(serializer.data)

  def put(self, request, id, review_id):
    pass

  def delete(self, request, id, review_id):
    try:
      review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
      return Response({'Error': '없는 리뷰입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    review.delete()
    return Response(status=status.HTTP_200_OK)