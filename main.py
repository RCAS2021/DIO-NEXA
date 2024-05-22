# Dicionário associando características aos modelos Claude 3
caracteristicas_modelos = {
    "automatizar tarefas": "Claude 3 Opus",
    "pesquisa e desenvolvimento": "Claude 3 Opus",
    "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",
    "motores de chatbots de lojas": "Claude 3 Haiku",
    "moderação de conteúdo": "Claude 3 Haiku",
    "processamento de tarefas mais básicas": "Claude 3 Haiku",
    "raciocínio cuidadoso": "Claude 3 Sonnet",
    "processamento de dados": "Claude 3 Sonnet",
    "aplicações de vendas": "Claude 3 Sonnet",
    "extração de texto de imagens": "Claude 3 Sonnet",
    "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
   
}

# TODO: Crie uma função 'encontrar_modelo' para encontrar o modelo correspondente à característica fornecida: 
def encontrar_modelo(caracteristica_fornecida):
# TODO: Itere sobre cada chave e valor no dicionário caracteristicas_modelos:
  for k, v in caracteristicas_modelos.items():
    if k in caracteristica_fornecida.lower():
      return v
  return "Modelo não encontrado." 
# TODO: Verifique se a palavra-chave (característica) está contida na característica fornecida (ignorando maiúsculas/minúsculas):
        
# TODO: Se encontrada, retorne o modelo correspondente:
           
# TODO: Se não encontrada, retorne uma mensagem indicando que o modelo não foi encontrado
 

# Entrada do usuário
caracteristica_fornecida = input()

# Encontrar e imprimir o modelo correspondente
modelo_correspondente = encontrar_modelo(caracteristica_fornecida)
print(modelo_correspondente)