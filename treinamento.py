from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "/Users\moura\OneDrive\Documentos\GitHub\ChatterBot_Maria\conversas\saudacoes.json",
    "C:\Users\moura\OneDrive\Documentos\GitHub\ChatterBot_Maria\conversas\servicos.json",
    "C:\Users\moura\OneDrive\Documentos\GitHub\ChatterBot_Maria\conversas\suporte.json"
]

def iniciar():
    robo = ChatBot("Maria, Robô de atendimento da TratorCenter")
    treinador = ListTrainer(robo)
    
    return treinador

def carregar_conversas():
    conversas = []
    
    for arquivo_conversas in CONVERSAS:
        with open(arquivo_conversas, "r") as arquivo:
            conversas_para_treinamento = json.load(arquivo)
            conversas.append(conversas_para_treinamento["conversas"])
            
            arquivo.close()
            
    return conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagem_resposta in conversa:
            mensagem = mensagem_resposta["mensagem"]
            resposta = mensagem_resposta["resposta"]
            
            print(f"Treinando Robô Maria. Mensagens: {mensagem}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])
                
if __name__=="__main__":
    treinador = iniciar()
    
    
    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)