from django.contrib import admin
from .models import Categoria, Marca, Produto, Compra, ItensCompra

#admin.site.register(Categoria)
#admin.site.register(Marca)
#admin.site.register(Produto)

@admin.register(Categoria) # Decorador; registra no admin herdando da model Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',) # Lista os campos a serem aparecidos
    search_fields = ('descricao',) # Campos de busca por Categoria no admin
    list_filter = ('descricao',) # Permite filtrar categoria por nome
    ordering = ('descricao',) # Ordena por nome e email

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'categoria')
    search_fields = ('nome', 'marca__nome', 'categoria__descricao') # underlines são usados para acessar atributos de chave estrangeira
    list_filter = ('marca', 'categoria')
    ordering = ('nome', 'marca', 'categoria')
    list_per_page = 25
    
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status')
    ordering = ('-id',)
    list_per_page = 25
    inlines = [ItensCompraInline] # Assim, os itens de compra irão ser apresentados abaixo do formulário de edição
