from rest_framework import serializers
from .models import CategoryProduct # 1


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    category = serializers.ChoiceField( # 2
        choices=CategoryProduct.choices, # 3
        default=CategoryProduct.OTHER # 4
    )
    price = serializers.DecimalField(decimal_places=2, max_digits=5)

    '''
Pontos de atenção:

1. Estamos importando nossa classe de escolhas criada em products/models.py. Assim conseguimos reutilizá-la para nosso serializador.
2. Atributo category: Utilizamos o tipo ChoiceField acessado a partir de serializers para configurar nosso category.
3. Parâmetro choices: passamos o argumento nomeado choices para definirmos as opções de escolha para aquele campo. Neste caso, estamos passando todas as choices de CategoryProduct.
4. Parâmetro default: Definimos o parâmetro default com um valor padrão, chamando a classe e seu atributo padrão (CategoryProduct.OTHER);      
    
    '''