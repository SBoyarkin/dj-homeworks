from pprint import pprint

from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
    # настройте сериализатор для позиции продукта на складе



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['address', 'positions']
    # настройте сериализатор для склада

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            obj = StockProduct()
            obj.stock = stock
            obj.product = position.get('product')
            obj.price = position.get('price')
            obj.quantity = position.get('quantity')
            obj.save()
        return stock

    def update(self, instance, validated_data):
        # извлекаем связанные данные для других таблиц
        positions = validated_data.pop('positions', None)
        stock = super().update(instance, validated_data)

        if positions is not None:
            existing_products = {prod.product.id: prod for prod in StockProduct.objects.filter(stock=instance)}
            print(existing_products)
            for position in positions:
                product_id = position.get('product').id
                print(product_id)
                if product_id in existing_products:
                    stock_product = existing_products[product_id]
                    print(stock_product)
                    stock_product.price = position.get('price', stock_product.price)
                    stock_product.quantity = position.get('quantity', stock_product.quantity)
                    stock_product.save()

        return stock
