import hashlib

# Classe Produto
class Produto:
    def __init__(self, id, nome, categoria, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, categoria={self.categoria}, preco={self.preco})"
class Nodo:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def _inserir(self, nodo, produto):
        if nodo is None:
            return Nodo(produto)
        if produto.nome < nodo.produto.nome:
            nodo.esquerda = self._inserir(nodo.esquerda, produto)
        else:
            nodo.direita = self._inserir(nodo.direita, produto)
        return nodo

    def inserir(self, produto):
        self.raiz = self._inserir(self.raiz, produto)

    def _buscar(self, nodo, nome):
        if nodo is None:
            return None
        if nome == nodo.produto.nome:
            return nodo.produto
        elif nome < nodo.produto.nome:
            return self._buscar(nodo.esquerda, nome)
        else:
            return self._buscar(nodo.direita, nome)

    def buscar(self, nome):
        return self._buscar(self.raiz, nome)
class TabelaHash:
    def __init__(self):
        self.tabela = {}

    def inserir(self, produto):
        self.tabela[produto.id] = produto

    def buscar(self, id_produto):
        return self.tabela.get(id_produto, None)
class Usuario:
    def __init__(self, username, senha):
        self.username = username
        self.senha = self.criptografar_senha(senha)

    def criptografar_senha(self, senha):
        # Criptografia da senha usando SHA-256
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_senha(self, senha):
        # Verificar se a senha informada corresponde ao hash armazenado
        return self.senha == hashlib.sha256(senha.encode()).hexdigest()
        
# Criação de Produtos
produto1 = Produto(1, "Camiseta", "Vestuário", 29.90)
produto2 = Produto(2, "Calça Jeans", "Vestuário", 99.90)
produto3 = Produto(3, "Tênis", "Calçados", 199.90)

# Sistema de Busca com Arvore Binária
arvore = ArvoreBinariaBusca()
arvore.inserir(produto1)
arvore.inserir(produto2)
arvore.inserir(produto3)

# Sistema de Busca com Tabela de Hash
tabela_hash = TabelaHash()
tabela_hash.inserir(produto1)
tabela_hash.inserir(produto2)
tabela_hash.inserir(produto3)

# Testando Busca por Nome (Árvore Binária)
produto_encontrado = arvore.buscar("Camiseta")
print(f"Produto encontrado na árvore: {produto_encontrado}")
