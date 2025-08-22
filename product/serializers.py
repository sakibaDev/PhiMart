from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product

# class CategorySerializers(serializers.Serializer):

#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

# class ProductSerializers(serializers.Serializer):

#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10,decimal_places=2,source ='price')

#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")


#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'specific-category'
#     )
#     # category = CategorySerializers()
#     # category = serializers.StringRelatedField()
#     # category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())

#     def calculate_tax(self,product):
#         return round(product.price * Decimal(1.1),2)
    
class CategorySerializers(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ['id','name','description','product_count']

    product_count = serializers.IntegerField()

class ProductSerializers(serializers.ModelSerializer):

    calculate_tax = serializers.SerializerMethodField()
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='specific-category'
    )

    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','image','category','calculate_tax']

    def get_calculate_tax(self, product):   # ✅ Correct method name
        return round(product.price * Decimal(1.1), 2)



    

    
    
