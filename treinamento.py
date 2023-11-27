from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "conversas\saudacoes.json",
    "conversas\servicos.json",
    "conversas\suporte.json"
]

def iniciar():
    robo = ChatBot("Maria, Robô de atendimento da TratorCenter")
    treinador = ListTrainer(robo)
    
    return treinador

def carregar_conversas():
    carregado, conversas = False, []
    
    for arquivo_conversas in CONVERSAS:
        with open(arquivo_conversas, "r", encoding="utf-8") as arquivo:
            conversas_para_treinamento = json.load(arquivo)
            conversas.append(conversas_para_treinamento["conversas"])
        carregado = True
            
    return carregado, conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]
            
            print(f"Treinando Robô Maria. Mensagens: {mensagens}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])
                
if __name__=="__main__":
    treinador = iniciar()
    
    
    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)