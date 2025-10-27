class NodeArvore:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.sim = None
        self.nao = None

class Node:
    def __init__(self, dados):
        self.dados = dados
        self.next = None

class Protocolo:
    def __init__(self):
        self.root_node = None    
        self.montar_arvore()     

    def montar_arvore(self):
        primeiro = NodeArvore('O paciente está inconsciente ou não responde a estímulos? (s/n)')
        segundo = NodeArvore('Está com falta de ar moderada a grave (s/n)?')
        terceiro = NodeArvore('Está com tontura ou fraqueza acentuada (s/n)?')
        quarto = NodeArvore('Está com febre leve ou mal-estar geral (s/n)?')
        
        self.root_node = primeiro
        # Prioridade 1 = Vermelho
        primeiro.sim = 1
        primeiro.nao = segundo
        # Prioridade 2 = Laranja
        segundo.sim = 2
        segundo.nao = terceiro
        # Prioridade 3 = Amarelo
        terceiro.sim = 3
        terceiro.nao = quarto
        # Prioridade 4 = Verde
        quarto.sim = 4
        # Prioridade 5 = Verde
        quarto.nao = 5

    def triagem(self):
        current = self.root_node
        while current and not isinstance(current, (int, float)):
            validador = input(current.pergunta)
            if validador == 's':
                current = current.sim
            elif validador == 'n':
                current = current.nao
            else:
                print('Entrada inválida. Tente novamente.')
                pass
        return current
    
class Fila:
    def __init__(self,nome):
        self.nome = nome
        self.head = None
        self.tail = None

    def enqueue(self, dados):
        paciente = Node(dados)
        if self.head == None:
            self.head = paciente
            self.tail = self.head
        else:
            self.tail.next = paciente
            self.tail = paciente
        print(f'Paciente {paciente.dados} foi adicionado à fila {self.nome} na posição')

    def dequeue(self):
        if self.head == None:
            return print('Não há pacientes nessa fila')
        print(f'Chamando paciente da fila {self.nome}: {self.head.dados}')
        self.head = self.head.next

    def listar(self):
        pos = 1
        current = self.head
        print(f'FILA: {self.nome}')
        if current:
            while current:
                print(f'Posição {pos}: {current.dados}')
                current = current.next
                pos += 1
        else:
            print('Não há ninguém esperando!')
        print('='*10)

class GerenciadorFila:
    def __init__(self):
        self.vermelha = Fila('Vermelha - Emergência')
        self.laranja = Fila('Laranja - Muito Urgente')
        self.amarelo = Fila('Amarelo - Urgente')
        self.verde = Fila('Verde - Pouco Urgente')
        self.azul = Fila('Azul - Não Urgente')

    def inserir(self, nome, categoria):
        categoria = str(categoria)
        if categoria == '1':
            self.vermelha.enqueue(nome)
        elif categoria == '2':
            self.laranja.enqueue(nome)
        elif categoria == '3':
            self.amarelo.enqueue(nome)
        elif categoria == '4':
            self.verde.enqueue(nome)
        elif categoria == '5':
            self.azul.enqueue(nome)

    def chamar(self):
        if not self.vermelha.head == None:
            self.vermelha.dequeue()
        elif not self.laranja.head == None:
            self.laranja.dequeue()
        elif not self.amarelo.head == None:
            self.amarelo.dequeue()
        elif not self.verde.head == None:
            self.verde.dequeue()
        elif not self.azul.head == None:
            self.azul.dequeue()
        else:
            print('Não há pacientes na fila.')

    def listar_todos(self):
        self.vermelha.listar()
        self.laranja.listar()
        self.amarelo.listar()
        self.verde.listar()
        self.azul.listar()

def menu():
    print('=== SISTEMA DE TRIAGEM MANCHESTER ===')
    print('1 - Cadastrar paciente')
    print('2 - Chamar paciente')
    print('3 - Mostrar status das filas')
    print('0 - Sair')

def main():
    protocolo = Protocolo()
    fila = GerenciadorFila()

    while True:
        menu()
        escolha = str(input('Digite o número: '))

        if escolha == '1':
            nome = input('Qual o nome do paciente? ')
            categoria = str(protocolo.triagem())
            fila.inserir(nome,categoria)
        elif escolha == '2':
            fila.chamar()
        elif escolha == '3':
            fila.listar_todos()
        elif escolha == '0':
            break
            
main()