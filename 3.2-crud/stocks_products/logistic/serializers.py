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
            StockProduct.objects.create(stock=stock, product=position.get('product'), price=position.get('price'),
                                        quantity=position.get('quantity'))
        return stock

    def update(self, instance, validated_data):
        # извлекаем связанные данные для других таблиц
        positions = validated_data.pop('positions', None)
        stock = super().update(instance, validated_data)


        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, product=position.get('product'),
                                                  defaults={'price': position.get('price'),
                                                            'quantity': position.get('quantity')})

        return stock
