import random
import time

def generateMatriz():  # Funcao que faz a geracao de uma matriz com elementos aleatorios
    try:
        while (True):  # Enquanto entrada de dados nao for inteiro, nao prossegue a execucao
            qtdLinhas = str(input('Digite a quantidade de linhas da matriz: '))
            qtdColunas = str(input('Digite a quantidade de colunas da matriz: '))
            if (qtdLinhas.isnumeric() != True or qtdColunas.isnumeric() != True):
                print('Entrada de dados invalida! Tente novamente!\n')
            else:
                break
        qtdLinhas = int(qtdLinhas)
        qtdColunas = int(qtdColunas)
        print('Gerando matriz aleatoria {} x {}'.format(qtdLinhas, qtdColunas))
        matrizOutput = open(outputFileConfig, 'w')
        randomMatriz = []
        for i in range(qtdLinhas * qtdColunas * 2):
            randomNumber = random.randint(0, 500)
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
    # Fazendo a leitura da matriz advinda do arquivo de entrada
    print('Abrindo arquivo de entrada.')
    fileContent = []
    with open(inputFileConfig) as file:
        for qtdLines, rowContent in enumerate(file):
            rowContent = rowContent.replace('\n', '')
            fileContent.append(rowContent.split())
    limitFor = qtdLines + 1
    for i in range(int(limitFor / 2)):
        matrizA.append(fileContent[i])
    for i in range(int(limitFor / 2), limitFor):
        matrizB.append(fileContent[i])

    # Calculando o produto entre as matrizes 1 e 2


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
    elapsedTime = t1 - t0
    return matriz3, elapsedTime


############################################################################################################################################
def IsPowerOfTwo(x):
  return (x != 0) and ((x & (x - 1)) == 0)

def split(m):
  littleN = int(len(m)/2)
  m11 = [[0 for x in range(littleN)] for x in range(littleN)]
  m12 = [[0 for x in range(littleN)] for x in range(littleN)]
  m21 = [[0 for x in range(littleN)] for x in range(littleN)]
  m22 = [[0 for x in range(littleN)] for x in range(littleN)]
  for i in range(littleN):
    for j in range(littleN):
      m11[i][j] = m[i          ][j          ]
      m12[i][j] = m[i          ][j + littleN]
      m21[i][j] = m[i + littleN][j          ]
      m22[i][j] = m[i + littleN][j + littleN]

  return m11, m12, m21, m22

def addM(mA,mB):
  N = len(mA)

  mC = [[0 for x in range(N)] for x in range(N)]

  for i in range(N):
    for j in range(N):
      mC[i][j] = int(mA[i][j]) + int(mB[i][j])
      
  return mC

def subM(mA,mB):
  N = len(mA)

  mC = [[0 for i in range(N)] for i in range(N)]

  for i in range(N):
    for j in range(N):
      mC[i][j] = int(mA[i][j]) - int(mB[i][j])
      
  return mC

def strassenMult(mA,mB):
  N = len(mA)
  
  if N == 1:
    return [[int(mA[0][0]) * int(mB[0][0])]]
  
  padding = False
  oldN = N
  if IsPowerOfTwo(N) == False:
    padding = True

    nextN = 1
    while(nextN < N):
      nextN*=2;
  
    newMA = [[0 for i in range(nextN)] for i in range(nextN)]
    newMB = [[0 for i in range(nextN)] for i in range(nextN)]
    for i in range(N):
      for j in range(N):
        newMA[i][j] = mA[i][j]
        newMB[i][j] = mB[i][j]

    N = nextN
    mA = newMA
    mB = newMB

  mA11,mA12,mA21,mA22 = split(mA)
  mB11,mB12,mB21,mB22 = split(mB)


  p1 = strassenMult(mA11           , subM(mB12,mB22))
  p2 = strassenMult(addM(mA11,mA12), mB22           )
  p3 = strassenMult(addM(mA21,mA22), mB11           )
  p4 = strassenMult(mA22           , subM(mB21,mB11))
  p5 = strassenMult(addM(mA11,mA22), addM(mB11,mB22))
  p6 = strassenMult(subM(mA12,mA22), addM(mB21,mB22))
  p7 = strassenMult(subM(mA21,mA11), addM(mB11,mB12))

  mC11 = addM(subM(addM(p5,p4),p2),p6)
  mC12 = addM(p1,p2)
  mC21 = addM(p3,p4)
  mC22 = addM(subM(addM(p1,p5),p3),p7)

  mC = [[0 for i in range(N)] for i in range(N)]

  littleN = int(N/2)
  for i in range(littleN):
    for j in range(littleN):
      mC[i          ][j          ] = mC11[i][j]
      mC[i          ][j + littleN] = mC12[i][j]
      mC[i + littleN][j          ] = mC21[i][j]
      mC[i + littleN][j + littleN] = mC22[i][j]

  if padding:
    newC = [[0 for i in range(oldN)] for i in range(oldN)]
    for i in range(oldN):
      for j in range(oldN):
        newC[i][j] = mC[i][j]
    mC = newC
  t4 = time.time()
  elapsedTime2 = t4-t3
  return mC
################################################################################################################################################################
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

matrizA:int = []
matrizB:int = []
tempo1 = 0
tempo2 = 0
while True:
    menuString = 'Opcoes:' + '\n'
    menuString += ' 1 - Gerar matrizes aleatorias' + '\n'
    menuString += ' 2 - Calcular produto entre as matrizes' + '\n'
    menuString += ' 3 - Calcular produto Strassen' + '\n'
    menuString += ' 4 - Imprime tempos' + '\n'
    menuString += ' 5 - Sair' + '\n'
    print(menuString)
    option = int(input(">> "))
    if option == 1:
        generateMatriz()
    elif option == 2:
        result = calculateProduct()
        print(result[0])
        for i in range(15):
            print()
        tempo1 = result[1]
    elif option == 3:
        t3 = time.time()
        result = strassenMult(matrizA,matrizB)
        t4 = time.time()
        print(result)
        for i in range(15):
            print()
        tempo2 = t4-t3
    elif option == 4:
        print('Para matrizes de tamanho {} x {}, o tempo gasto foi de \n'.format(len(matrizA), len(matrizB)))
        print('Tempo 1: {}'.format(tempo1))
        print('Tempo 2: {}'.format(tempo2))
        if(tempo1 > tempo2):
            print('\nO algoritmo 2 foi mais rapido.')
        elif(tempo2 > tempo1):
            print('\nO algoritmo 1 foi mais rapido.')
        else:
            print('Os dois algoritmos tiveram o mesmo tempo.')
    elif option == 5:
        print('Encerramento solicitado pelo usuario.')
        break
    else:
        print('Opcao invalida.')
