

class BankFunctions:
    def __init__(self, contaPrincipal,  boletos, contasFavoritas):
        self.contaPrincipal = contaPrincipal
        self.boletos = boletos
        self.contasFavoritas = contasFavoritas

    def boletos_pendentes(self):
        return "Boleto Pendentes:\n" + "\n".join([f"Numero: {b.numero} - Valor: {b.valor}" for b in self.boletos if b.status == 'pendente'])
    
    def pagarBoleto(self, numero_boleto):
        boleto = None
        for b in self.boletos:
            if b.numero == numero_boleto:
                boleto = b
                break
        if boleto == None:
            return "Boleto não encontrado"
        boleto.pagar(self.contaPrincipal)
        return "Boleto pago com sucesso"
    
    def transferir(self, valor, numero_conta_destino):
        conta_destino = None
        for conta in self.contasFavoritas:
            if conta.numero == numero_conta_destino:
                conta_destino = conta
                break
        if conta_destino == None:
            return "Conta não encontrada"
        self.contaPrincipal.transferir(valor, conta_destino)
        return "Transferência realizada com sucesso"

    def saldo(self):
        return self.contaPrincipal.saldo
    
    def obter_numero_conta_por_apelido(self, apelido):
        for conta in self.contasFavoritas:
            if conta.apelido.lower() == apelido.lower():
                return conta.numero
        return "Conta não encontrada"
    
    def get_functions(self):
        return [  
            {
                "name": "pagarBoleto",
                "description": "Paga um boleto pelo seu número",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numero_boleto": {
                            "type": "string",
                            "description": "numero do boleto a pagar"
                        }
                    },
                    "required": ["numero_boleto"],
                }
            },
            {
                "name": "boletos_pendentes",
                "description": "Obtem a lista de boletos não pagos",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                    "required": [],
                }
            },
            {
                "name": "transferir",
                "description": "Paga um boleto pelo seu número",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "valor": {
                            "type": "integer",
                            "description": "valor a ser transferido"
                        },
                        "numero_conta_destino": {
                            "type": "string",
                            "description": "numero da conta destino"
                        },
                        
                    },
                    "required": ["valor", "numero_conta_destino"],
                }
            },
            {
                "name": "saldo",
                "description": "Obtem o saldo da conta principal",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                    "required": [],
                }
            },
            {
                "name": "obter_numero_conta_por_apelido",
                "description": "Obtem o saldo da conta principal",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "apelido": {
                            "type": "string",
                            "description": "apelido da conta"
                        }
                    },
                    "required": ["apelido"],
                }
            },
            
        ]  


class ContaCorrente:
    def __init__(self, numero, saldo, apelido=None):
        self.numero = numero
        self.saldo = saldo
        self.apelido = apelido

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def __str__(self):
        return f'Numero: {self.numero}\nSaldo: {self.saldo}'
    

class Boleto:
    def __init__(self, valor, numero, sacado, status='pendente'):
        self.valor = valor
        self.numero = numero
        self.sacado = sacado
        self.status = status

    def pagar(self, conta):
        conta.sacar(self.valor)
        self.status = 'pago'

    def __str__(self):
        return f'Valor: {self.valor}\nNumero: {self.numero}\nData de Vencimento: {self.data_vencimento}\nSacado: {self.sacado}\nStatus: {self.status}'