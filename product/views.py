from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView
from .serializers import ProductSerializers
from .models import Product
class ProductCreate(CreateAPIView):
    queryset =Product.objects.all()
    serializer_class =ProductSerializers
    def get_object(self):
        product_id=self.request.data.get("product_id")
        return Product.objects.get(id=product_id)

class ProductUdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_object(self):
        product_id = self.request.data.get("product_id")
        return Product.objects.get(id=product_id)
class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    def get_object(self):
        product_id = self.request.data.get("product_id")
        return Product.objects.get(id=product_id).delete()






