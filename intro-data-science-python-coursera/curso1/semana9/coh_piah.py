import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
  i = 1
  textos = []
  texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  while texto:
      textos.append(texto)
      i += 1
      texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

  return textos

def separa_sentencas(texto):
  '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
  sentencas = re.split(r'[.!?]+', str(texto))
  if sentencas[-1] == '':
    del sentencas[-1]
  return sentencas

def separa_frases(sentenca):
  '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
  return re.split(" ", frase)

def n_palavras_unicas(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
      p = palavra.lower()
      if p in freq:
          if freq[p] == 1:
              unicas -= 1
          freq[p] += 1
      else:
          freq[p] = 1
          unicas += 1

  return unicas

def n_palavras_diferentes(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
  freq = dict()
  for palavra in lista_palavras:
      p = palavra.lower()
      if p in freq:
          freq[p] += 1
      else:
          freq[p] = 1

  return len(freq)

def compara_assinatura(as_a, as_b):
  '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
  somatorio_dif_ass = 0
  i = 0
  while i < len(as_a):
      somatorio_dif_ass += abs(as_a[i] - as_b[i])
      print("SOMATORIO : ", somatorio_dif_ass)
      i += 1
  return somatorio_dif_ass / 6

def calcula_assinatura(texto):
  '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
  sentencas = separa_sentencas(texto)
  frases = []
  palavras = []
  caracteres_sentenca = 0
  i = j = 0
  tamanho_palavras = []
  n_caracteres_frases = n_caracteres_sentencas = 0
  for sentenca in sentencas:
      frases += separa_frases(sentenca)
      for ch in sentenca:
              n_caracteres_sentencas += 1
      j += 1
  for frase in frases:
      palavras += separa_palavras(frase)
      for ch in frase:
              n_caracteres_frases += 1
      i += 1
  for palavra in palavras:
      if palavra == '':
          palavras.remove(palavra)

  soma_tamanho_palavras = 0
  for palavra in palavras:
      tamanho_palavras.append(len(palavra))
      soma_tamanho_palavras += len(palavra)

  palavras_unicas = n_palavras_unicas(palavras)
  palavras_diferentes = n_palavras_diferentes(palavras)
  total_palavras = len(palavras)

  wal = soma_tamanho_palavras / (total_palavras)
  ttr = palavras_diferentes / total_palavras
  hlr = palavras_unicas / total_palavras
  sal = n_caracteres_sentencas / len(sentencas)
  sac = len(frases) / len(sentencas)
  pal = n_caracteres_frases / len(frases)

  return [wal, ttr, hlr, sal, sac, pal]

def soma(texto1, texto2):
    texto_novo = [texto1, texto2]
    return texto_novo

def avalia_textos(textos, ass_cp):
  '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
  i = 0
  novo_texto = []
  while i < len(textos):
      novo_texto.append(textos[i])
      i += 1
  ass_aluno = calcula_assinatura(novo_texto)
  comparacao = compara_assinatura(ass_aluno, ass_cp)
  print(comparacao)
  return comparacao


assinatura = le_assinatura()
texto = le_textos()
avalia_textos(texto, assinatura)


# Tamanho médio de palavra: Média simples do número de caracteres por palavra.
# Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
# Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
# Tamanho médio de sentença: Média simples do número de caracteres por sentença.
# Complexidade de sentença: Média simples do número de frases por sentença.
# Tamanho médio de frase: Média simples do número de caracteres por frase.
