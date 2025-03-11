import re
import matplotlib.pyplot as plt
from collections import Counter

# análise básica
def contar_caracteres(texto):
    # Contando caracteres incluindo espaços
    print(f'caracteres com espaço: {len(texto)}')
    
    # Contando caracteres sem espaços
    print(f'caracteres sem espaço: {len(texto.replace(" ", ""))}')
def contar_palavras(texto):
   # contando palavras
   print(f'quantidade de palavras no texto: {len(texto.split())}')
def contar_frases(texto):
    # identificando as frases
    frases = re.split(r'[.!?]', texto)

    # Removendo frases vazias (se o usuário usar mais de uma pontuação em uma frase)
    frases = [frase.strip() for frase in frases if frase.strip()]

    # resultado
    print(f'quantidade de frases: {len(frases)}')

# análise de palavras
def palavra_mais_frequente(texto):
    # divide o texto em palavras
    palavras = texto.split()

    # conta a frequência de cada palavra
    contador = Counter(palavras)
    palavra_mais_comum, frequencia = contador.most_common(1)[0]

    # resultado
    print(f'a palavra mais comum é: {palavra_mais_comum}, aparece {frequencia} vezes')
def palavras_unicas(texto):
    # divide o texto em palavras
    palavras = texto.split()

    # conta a frequência de cada palavra
    contador = Counter(palavras)

    # filtra palavras que só aparecem uma vez
    palavras_unicas = [palavra for palavra, frequencia in contador.items() if frequencia == 1]

    # resultado
    if palavras_unicas:
        print('palavras que aparecem uma unica vez: ')
        for palavra in palavras_unicas:
            print(f'    - {palavra}')
    else:
        pritn('todas as palavras aparecem mais de uma vez no texto.')
def palavras_por_frequencia(texto):
    # divide o texto em palavras
    palavras = texto.split()

    # conta a frequência de cada palavra
    contador = Counter(palavras)

    # ordena as palavras por frequência
    palavras_ordenadas = contador.most_common()

    # resultado
    print('palavras ordenadas por frequência:')
    for palavra, frequencia in palavras_ordenadas:
        print(f'    - {palavra}: {frequencia}')

# análise sentenças
def frase_mais_longa(texto):
    # identifica as frases
    frases = re.split(r'[.!?]', texto)

    # Removendo frases vazias (se o usuário usar mais de uma pontuação em uma frase)
    frases = [frase.strip() for frase in frases if frase.strip()]

    # encontra a frase mais longa
    frase_mais_longa =  max(frases, key=lambda frase: len(frase.split()))

    # resultado
    print(f'a frase mais longa é: {frase_mais_longa}')
def frase_mais_curta(texto):
    # identifica as frases
    frases = re.split(r'[.!?]', texto)

    # Removendo frases vazias (se o usuário usar mais de uma pontuação em uma frase)
    frases = [frase.strip() for frase in frases if frase.strip()]

    # encontra a frase mais curta
    frase_mais_curta =  min(frases, key=lambda frase: len(frase.split()))

    # resultado
    print(f'a frase mais curta é: {frase_mais_curta}')

# estatísticas avançadas
def media_palavras_por_frase(texto):
    # identifica as frases
    frases = re.split(r'[.!?]', texto)

    # Removendo frases vazias (se o usuário usar mais de uma pontuação em uma frase)
    frases = [frase.strip() for frase in frases if frase.strip()]

    # conta o numero de palavras em cada frase
    total_palavras = sum(len(frase.split()) for frase in frases)

    # calcula o total de frases
    total_frases = len(frases)

    # calcula a média de palavras por frase
    if total_frases > 0:
        media = total_palavras / total_frases
        print(f'média de palavras por frase: {media: .2f}')
    else:
        print('não há frases para calcular')
def tamanho_medio_palavras(texto):
    # divide o texto em palavras
    palavras = texto.split()

    # verifica se o texto não está em branco
    if not palavras:
        print('o texto está em branco. Não é possivel calcular uma média')
        return
    
    # calcula o total de caracteres nas palavras
    total_caracteres = sum(len(palavra) for palavra in palavras)

    # calcula o numero de palavras no texto
    total_palavras = len(palavras)

    # calcula a media dos caracteres/palavra
    tamanho_medio = total_caracteres / total_palavras

    # resultado
    print(f'Tamanho médio das palavras: {tamanho_medio: .2f} caracteres')
def palavras_grandes(texto):
    # divide o texto em palavras
    palavras = texto.split()

    # verifica se a palavra tem mais de 5 caracteres
    palavras_longas = [palavra for palavra in palavras if len(palavra) > 5]

    # resultado
    print(f'palavras com mais de 5 caracteres: {palavras_longas}')

# analise de caracteres especiais
def vogais_consoantes(texto):
     # Define as vogais (eu copiei as vogais da internet, acho que não tem problema :D)
    considerado_vogal = "aeiouáéíóúâêîôûàèìòùãõäëïöüAEIOUÁÉÍÓÚÂÊÎÔÛÀÈÌÒÙÃÕÄËÏÖÜ"

    # ativa os contadores
    vogais = 0
    consoantes = 0

    # conta as vogais e consoantes
    for caractere in texto:
        if caractere.isalpha():
            if caractere in considerado_vogal:
                vogais += 1
            else:
                consoantes += 1
    
    # resultado
    print(f'total de vogais: {vogais}')
    print(f'total de consoantes: {consoantes}')
def numeros_e_especiais(texto):
    # Define caracteres especiais (copiei também rs :D)
    caracteres_especiais = "!@#$%^&*()_+-=[]{};':\",./<>?\\|`~"

    # ativa os contadores
    numeros = 0
    especiais = 0

    # conta os numeros e caracteres especiais
    for caractere in texto:
        if caractere.isdigit(): # .isdigit verifica se é numero
            numeros += 1
        elif caractere in caracteres_especiais:
            especiais += 1
    
    # resultado
    print(f'Quantidade de numeros: {numeros}')
    print(f'Quantidade de caracteres especiais: {especiais}')

# geração de relatório visual
def histograma_frequencia_palavras(texto, top_n=10):
    # Remove pontuações e converte o texto para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    
    # Divide o texto em palavras
    palavras = texto.split()
    
    # Conta a frequência de cada palavra
    contagem_palavras = Counter(palavras)
    
    # Pega as 'top_n' palavras mais comuns
    palavras_comuns = contagem_palavras.most_common(top_n)
    
    # Separa as palavras e suas frequências
    palavras, frequencias = zip(*palavras_comuns)
    
    # Plota o histograma
    plt.figure(figsize=(10, 6))
    plt.bar(palavras, frequencias, color='blue')
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.title(f'Top {top_n} Palavras Mais Frequentes')
    plt.xticks(rotation=45)
    plt.show()
def grafico_frases_por_tamanho(texto):
    # identifica as frases
    frases = re.split(r'[.!?]', texto)
    
    # Inicializa contadores
    curtas = 0
    medias = 0
    longas = 0
    
    # Conta o tamanho de cada frase
    for frase in frases:
        palavras = frase.split()  # Divide a frase em palavras
        num_palavras = len(palavras)
        
        if num_palavras < 10:
            curtas += 1
        elif 10 <= num_palavras <= 20:
            medias += 1
        else:
            longas += 1
    
    # Categorias e valores para o gráfico
    categorias = ['Curtas (<10)', 'Médias (10-20)', 'Longas (>20)']
    valores = [curtas, medias, longas]
    
    # Configura o gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(categorias, valores, color=['blue', 'green', 'red'])
    plt.xlabel('Tipo de Frase')
    plt.ylabel('Quantidade de Frases')
    plt.title('Quantidade de Frases Curtas, Médias e Longas')
    plt.show()

# recebendo o texto do usuário para o programa
print("---=== Analisador de texto inteligente ===---")
texto = input("digte o texto: ").strip()
print('\n')

# usuario escolhe a função que irá utilizar
print('---=== Funções ===---')
funcao = input((f'para cada função digite o numero correspondente:\n'
      'análise basica [1]\n'
      'análise de palavras [2]\n'
      'análise de sentenças [3]\n'
      'estatísticas avançadas [4]\n'
      'analise de caracteres especiais [5]\n'
      'geração de relatório visual [6]\n'
      'todas as funções [7]\n'))
print('\n')

# resultado da função escolhida pelo usuário
print('---=== Resultado ===---')
if funcao == '1':
    contar_caracteres(texto)
    contar_palavras(texto)
    contar_frases(texto)
elif funcao == '2':
    palavra_mais_frequente(texto)
    palavras_unicas(texto)
    palavras_por_frequencia(texto)
elif funcao == '3':
    frase_mais_longa(texto)
    frase_mais_curta(texto)
elif funcao == '4':
    media_palavras_por_frase(texto)
    tamanho_medio_palavras(texto)
    palavras_grandes(texto)
elif funcao == '5':
    vogais_consoantes(texto)
    numeros_e_especiais(texto)
elif funcao == '6':
    histograma_frequencia_palavras(texto)
    grafico_frases_por_tamanho(texto)
elif funcao == '7':
    contar_caracteres(texto)
    contar_palavras(texto)
    contar_frases(texto)
    print('---------------------------')
    palavra_mais_frequente(texto)
    palavras_unicas(texto)
    palavras_por_frequencia(texto)
    print('---------------------------')
    frase_mais_longa(texto)
    frase_mais_curta(texto)
    print('---------------------------')
    media_palavras_por_frase(texto)
    tamanho_medio_palavras(texto)
    palavras_grandes(texto)
    print('---------------------------')
    vogais_consoantes(texto)
    numeros_e_especiais(texto)
    print('---------------------------')
    histograma_frequencia_palavras(texto)
    grafico_frases_por_tamanho(texto)
