import random
import time

def generateMatriz():  #Funcao que faz a geracao de uma matriz com elementos aleatorios
    try:
        while(True):     #Enquanto entrada de dados nao for inteiro, nao prossegue a execucao
            qtdLinhas = str(input('Digite a quantidade de linhas da matriz: '))
            qtdColunas = str(input('Digite a quantidade de colunas da matriz: '))
            if(qtdLinhas.isnumeric() != True or qtdColunas.isnumeric() != True):
                print('Entrada de dados invalida! Tente novamente!\n')
            else:
                break
        qtdLinhas = int(qtdLinhas)
        qtdColunas = int(qtdColunas)
        print('Gerando matriz aleatoria {} x {}'.format(qtdLinhas, qtdColunas))
        matrizOutput = open(outputFileConfig, 'w')
        randomMatriz = []
        for i in range(qtdLinhas*qtdColunas*2):
            randomNumber = random.randint(-1000, 1000)
            randomMatriz.append(randomNumber)
        stringMatriz = str()
        qtdElem = qtdLinhas + qtdColunas
        qtd = 0
        for i in range(2):
            for i in range(qtdLinhas):
                for j in range(qtdColunas):
                    stringMatriz += str(randomMatriz[qtd]) + ' '
                    qtd += 1
                stringMatriz += '\n'
        matrizOutput.write(stringMatriz)
        matrizOutput.close()
        print('Matriz gerada com sucesso!')
    except Exception as e:
        print(e)
        print('Erro na criacao da matriz!')

def readFileMatrix():
    #Fazendo a leitura da matriz advinda do arquivo de entrada
    print('Abrindo arquivo de entrada.')
    fileContent = []
    with open(inputFileConfig) as file:
        for qtdLines, rowContent in enumerate(file):
            rowContent = rowContent.replace('\n', '')
            fileContent.append(rowContent.split())
    limitFor = qtdLines+1
    for i in range(int(limitFor/2)):
        matrizA.append(fileContent[i])
    for i in range(int(limitFor/2), limitFor):
        matrizB.append(fileContent[i])

    #Calculando o produto entre as matrizes 1 e 2

def calculateProduct():
    readFileMatrix()
    index = 0
    linhasA, colunasA = len(matrizA), len(matrizA[0])
    linhasB, colunasB = len(matrizB), len(matrizB[0])

    matriz3 = []
    print('Calculando o produto...')
    t0 = time.time()
    for i in range(linhasA):
        matriz3.append([])
        for j in range(colunasB):
            matriz3[i].append(0)
            for k in range(colunasA):
                matriz3[i][j] += int(matrizA[i][k]) * int(matrizB[k][j])
    t1 = time.time()
    elapsedTime = t1-t0
    return matriz3, elapsedTime

# def calculateProductStrassen():
#     tamanhoMatrizA = len(matrizA)
#     matrizAux = []
#     if tamanhoMatrizA == 1:
#         matrizAux.append(matrizA[tamanhoMatrizA][tamanhoMatrizA] * matrizB[tamanhoMatrizA][tamanhoMatrizA])
#     else:
#         listaSoma = []
#         for i in range(n):
#             listaSoma.append([])
#             for j in range(n):
#                 listaSoma[i].append(0)
#                 temp0 = 0
#                 temp1 = 0
#                 temp2 = 0
#                 temp3 = 0

#                 for x in range(n/2):
#                     temp0 = x
#                 for x in range((n/2)+1), n):
#                     temp1 = x
#         listaSoma.append((matrizB[x for x in range(n/2)][x for x in range((n/2)+1, n)]) - matrizB[x for x in range((n/2)+1, n)][x for x in range((n/2)+1, n)])
#         print(listaSoma)
#         return


try:
    configFile = open('./Config/config.txt', 'r')
    outputFileConfig = configFile.readline()
    inputFileConfig = configFile.readline()
    if (outputFileConfig.find("outputFile:") == -1):
        print('Nao eh possivel fazer a leitura do arquivo de saida.')
    if (inputFileConfig.find("inputFile:") == -1):
        print('Nao eh possivel fazer a leitura do arquivo de entrada.')
    outputFileConfig = outputFileConfig.replace("outputFile:", '')
    inputFileConfig = inputFileConfig.replace("inputFile:", '')
except Exception as e:
    print(e)
    print('Erro na leitura do arquivo de configuracao.')

matrizA = []
matrizB = []

while True:
    menuString = 'Opcoes:' + '\n'
    menuString += ' 1 - Gerar matrizes aleatorias' + '\n'
    menuString += ' 2 - Calcular produto entre as matrizes' + '\n'
    menuString += ' 3 - Calcular produto Strassen' + '\n'
    menuString += ' 4 - Sair' + '\n'
    print(menuString)
    option = int(input(">> "))
    if option == 1:
        generateMatriz()
    elif option == 2:
        result = calculateProduct()
        print(result[0])
        for i in range(15):
            print()
        print(result[1])
    # elif option == 3:
    #     calculateProductStrassen()
    #     break
    elif option == 4:
        print('Encerramento solicitado pelo usuario.')
        break
    else:
        print('Opcao invalida.')
