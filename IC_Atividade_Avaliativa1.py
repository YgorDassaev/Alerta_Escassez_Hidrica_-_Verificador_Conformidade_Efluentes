#-------------------------------------------------------
#Introdução à Computação
#-------------------------------------------------------
#Atividade Avaliativa 1
#Aluno: Ygor Dassaev Lins Soares Barbosa
#-------------------------------------------------------
#Problemática A: Automação de Alerta de Escassez Hídrica
#Problemática B: Verificador de Conformidade de Efluentes

#Tabela de cores do texto:
texto_cor_vermelha = '\033[31m'
texto_cor_verde = '\033[32m'
texto_cor_amarela = '\033[33m'
reseta_texto_para_cor_padrao = '\033[97m'

#valores de segurança hídrica do reservatório
vazao_limite_critico = 1          
nivel_limite_critico = 1        

#valores legais de descarte de resíduos industriais estabelecidos pela CONAMA
temperatura_faixa_legal = 40 
ph_minimo = 5 
ph_maximo = 9

#Parâmetros do reservatório a ser analisado
vazao_atual_reservatorio = 0
nivel_atual_reservatorio = 0

#Parâmetros dos descartes industriais a ser analisado
ph_descarte_industrial = 0
temperatura_descarte_industrial = 0

#Armazena o tipo de análise digitada pelo usuário, mudando o fluxo do código
tipo_de_analise_selecionada = -1

print("+-------------------------------------------------------------------------------------------------------------------------+")

print("|", texto_cor_verde + "Programa de Automação de Alerta de Escassez Hídrica e Verificador de Conformidade de Efluentes" + reseta_texto_para_cor_padrao)

print("+-------------------------------------------------------------------------------------------------------------------------+")

print("|",texto_cor_amarela + "[1] - Análise de parâmetros do reservatório" + reseta_texto_para_cor_padrao)
print("|",texto_cor_amarela + "[2] - Análise de parâmetros dos descartes industriais" + reseta_texto_para_cor_padrao)

print("+-------------------------------------------------------------------------------------------------------------------------+")

tipo_de_analise_selecionada = int(input("| Digite o número referente ao tipo de análise desejada: "))

if tipo_de_analise_selecionada == 1:

  print("+-------------------------------------------------------------------------------------------------------------------------+")
  print("|", texto_cor_verde , "Análise selecionada: Análise de parâmetros do reservatório", reseta_texto_para_cor_padrao)
  print("+-------------------------------------------------------------------------------------------------------------------------+")

  vazao_atual_reservatorio = float(input("| Digite a vazão do reservatório: "))
  print("+-------------------------------------------------------------------------------------------------------------------------+")
  nivel_atual_reservatorio = float(input("| Digite o nível do reservatório: "))
  print("+-------------------------------------------------------------------------------------------------------------------------+")

  if(vazao_atual_reservatorio < vazao_limite_critico or nivel_atual_reservatorio < nivel_limite_critico):

    print("|", texto_cor_vermelha + "[ERRO]: Baixos níveis de água, fechar saída do reservatório até níveis entrarem na faixa segura." + reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")

  else:
    
    print("|", texto_cor_verde + "[OK]: Níveis do reservatório estáveis.." + reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")

if tipo_de_analise_selecionada == 2:

  verifica_parametos = 0 

  print("+-------------------------------------------------------------------------------------------------------------------------+")
  print("|", texto_cor_verde , "Análise selecionada: Análise de parâmetros dos descartes industriais", reseta_texto_para_cor_padrao)
  print("+-------------------------------------------------------------------------------------------------------------------------+")

  ph_descarte_industrial  = float(input("| Digite o pH do descarte industrial: "))
  print("+-------------------------------------------------------------------------------------------------------------------------+")
  temperatura_descarte_industrial = float(input("| Digite a temperatura do descarte industrial: "))
  print("+-------------------------------------------------------------------------------------------------------------------------+")

  if(ph_descarte_industrial >= ph_minimo and ph_descarte_industrial <= ph_maximo):
    verifica_parametos = verifica_parametos + 1 

    print("|", texto_cor_verde , "pH dos resíduos estão de acordo com a CONAMA", reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")
  else:

    print("|", texto_cor_vermelha + "pH fora da faixa permitida" + reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")

  if temperatura_descarte_industrial < temperatura_faixa_legal:
    verifica_parametos = verifica_parametos + 1 
    print("|", texto_cor_verde , "Temperatura dos resíduos estão de acordo com a CONAMA", reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")

  else:
    print("|", texto_cor_vermelha + "Temperatura fora da faixa permitida" + reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")

  if verifica_parametos == 2:
    print("|", texto_cor_verde , "Resíduos podem ser descartado", reseta_texto_para_cor_padrao)
    print("+-------------------------------------------------------------------------------------------------------------------------+")
  
  else:
      print("|", texto_cor_vermelha + "Resíduos não podem ser descartado" + reseta_texto_para_cor_padrao)
      print("+-------------------------------------------------------------------------------------------------------------------------+")    

    