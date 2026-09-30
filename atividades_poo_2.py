class Veiculo:

  def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.manutencoes = []

  def exibir_informacoes(self):
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Valor da diaria: R$ {self.valor_diaria:.2f}")

  def calcular_valor_locacao(self, dias):
            return self.valor_diaria * dias

  def adicionar_manutencao(self, manutencao):
      self.manutencoes.append(manutencao)

class Carro(Veiculo):

  def __init__(self, placa, modelo, ano, valor_diaria, quantidade_portas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.quantidade_portas = quantidade_portas

  def abrir_porta(self):
       print("A porta do carro foi aberta .")
 
  def exibir_tipo(self):
       print("Tipo de veiculo: Carro")

class Moto(Veiculo):

  def __init__(self, placa, modelo, ano, valor_diaria, cilindradas):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas

  def ligar(self):
      print("A moto foi ligada.")

  def exibir_tipo(self):
      print("Tipo de veiculo: Moto")

class Caminhao(Veiculo):

  def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

  def carregar(self):
      print("O caminhao está sendo carregado.")

  def exibir_tipo(self):
      print("Tipo de veiculo: Caminhao")

class Cliente:

  def __init__(self, nome, documento, telefone):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone

  def exibir_dados(self):
      print(f"Nome: {self.nome}")
      print(f"Documento: {self.documento}")
      print(f"Telefone: {self.telefone}")

  def atualizar_telefone(self, novo_telefone):
      self.telefone = novo_telefone

class ContratoLocacao:

  def __init__(self, data_inicio, data_fim_prevista, valor_total, status, cliente, veiculo, nome_condutor, cnh, telefone_condutor):
        self.data_inicio = data_inicio
        self.data_fim_prevista = data_fim_prevista
        self.valor_total = valor_total
        self.status = status
        self.cliente = cliente
        self.veiculo = veiculo

        self.condutor = Condutor(nome_condutor, cnh, telefone_condutor)

  def finalizar(self):
      self.status = "finalizado"
      print("Contrato finalizado.")

  def cancelar(self):
      self.status = "cancelado"
      print("Contrato cancelado.")

class Condutor:

  def __init__(self, nome, cnh, telefone):
        self.nome = nome
        self.cnh = cnh
        self.telefone = telefone

  def exibir_dados(self):
      print(f"Nome: {self.nome}")
      print(f"CNH: {self.cnh}")
      print(f"Telefone: {self.telefone}")

  def atualizar_cnh(self, nova_cnh):
      self.cnh = nova_cnh

class Manutencao:

  def __init__(self, data, tipo, custo):
        self.data = data
        self.tipo = tipo
        self.custo = custo

  def exibir_dados(self):
      print(f"Data: {self.data}")
      print(f"Tipo: {self.tipo}")
      print(f"Custo: R$ {self.custo:.2f}")

  def atualizar_custo(self, novo_custo):
      self.custo = novo_custo

veiculo1 = Veiculo(
      "ABC-1234",
      "Toyota corolla",
      2023,
      150.00
)

manutencao1 = Manutencao(
      "20/09/2026",
      "Troca de óleo",
      250.00
)

veiculo1.adicionar_manutencao(manutencao1)

print("Manutenção do veículo:")
veiculo1.manutencoes[0].exibir_dados()

cliente1 = Cliente(
    "João Silva",
    "123.456.789-00",
    "(86) 99999-9999"
)

contrato1 = ContratoLocacao(
    "25/09/2026",
    "30/09/2026",
    750.00,
    "ativo",
    cliente1,
    veiculo1,
    "Carlos Souza",
    "123456789",
    "(86) 98888-8888"
)

print("\nDados do condutor:")
contrato1.condutor.exibir_dados()