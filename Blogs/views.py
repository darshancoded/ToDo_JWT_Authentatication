from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .permissions import IsOwner
from .models import Blog
User = get_user_model()
class Blogview(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serialiazer = BlogSerializer(data = request.data)
        if serialiazer.is_valid():
            post = serialiazer.save(author=request.user)
            return Response({"message":"Todo created successfully","title":post.title},status=status.HTTP_200_OK)
        return Response(serialiazer.errors,status=400)    
class AllView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,pk):
        if pk is not None:
            try:
                user = User.objects.get(pk=pk)
                serializer = BlogSerializer(user)
                return Response(serializer.data)
            except: User.DoesNotExist
            return Response({"error": "User not found"}, status=404)
        else:
            users = User.objects.all()
        serializer = BlogSerializer(users, many=True)
        return Response(serializer.data)

class BlogUpdateDelete(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def patch(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        self.check_object_permissions(request, blog)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            post = serializer.save()
            return Response({"message": "Blog updated successfully", "title": post.title}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        self.check_object_permissions(request, blog)
        blog.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)