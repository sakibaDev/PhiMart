from rest_framework import status
from rest_framework.response import Response
from product.models import Product,Category
from product.serializers import ProductSerializers,CategorySerializers
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
 


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializers


    def delete(self,request,id):

        product =Product.objects.all()
        product.delete()

        if product.stock >10:
            return Response({'message':'Product with stock more than 10 cannot be deleted.'})
        
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoryViewSet(ModelViewSet):

    queryset =Category.objects.annotate(product_count = Count('products')).all()
    serializer_class = CategorySerializers

# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
        
# class ProductDetails(RetrieveUpdateDestroyAPIView):

#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializers


# class CategoryList(ListCreateAPIView):

#     queryset =Category.objects.annotate(product_count = Count('products')).all()
#     serializer_class = CategorySerializers

# class CategoryDetails(RetrieveUpdateDestroyAPIView):

#     queryset =Category.objects.annotate(product_count = Count('products')).all()
#     serializer_class = CategorySerializers


# 



# class ViewSpecificProduct(APIView):

#     def get(self,request,id):

#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializers(product,context={'request': request})
#         return Response(serializer.data) 
    
#     def put(self,request,id):

#         product =get_object_or_404(Product,pk=id)
#         serializer = ProductSerializers(product,data= request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)
    
#     def delete(self,request,id):

#         product =get_object_or_404(Product,pk=id)
#         copy_of_product = product
#         product.delete()

#         serializer = CategorySerializers(copy_of_product)
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

# class ViewCategory(APIView):

#     def get(self, request):
#         categories = Category.objects.annotate(product_count=Count('products')).all()
#         serializer = CategorySerializers(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):

#         serializer = CategorySerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ViewSpecificCategory(APIView):

#     def get(self,request,pk):

#         category = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializers(category)
#         return Response(serializer.data)
    
#     def put(self,request,pk):

#         category = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializers(category,data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,requet,pk):

#         category = get_object_or_404(Categorypk=pk)
#         copy_of_category = category

#         category.delete()
#         serializer = CategorySerializers(copy_of_category)
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

# Create your views here.

# @api_view(['GET','POST'])
# def view_products(request):

#     if request.method == 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializers(products,many=True,context={'request': request})
#         return Response(serializer.data) 
    
#     if request.method == 'POST':

#         serializer = ProductSerializers(data = request.data)
        
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)



# @api_view(['GET', 'PUT', 'DELETE'])
# def view_specific_products(request,pk):
    
#     if request.method == 'GET':
#         product = get_object_or_404(Product,pk=pk)
#         serializer = ProductSerializers(product,context={'request': request})
#         return Response(serializer.data) 
    
#     if request.method =='PUT':

#         product =get_object_or_404(Product,pk=id)
#         serializer = ProductSerializers(product,date= request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)
    
#     if request.method =='DELETE':

#         product =get_object_or_404(Product,pk=id)
#         product.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
