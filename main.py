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
    m11 = []
    m12 = []
    m21 = []
    m22 = []
    for i in range(littleN):
        tempArr11 = []
        tempArr12 = []
        tempArr21 = []
        tempArr22 = []
        for j in range(littleN):
            tempArr11.append(m[i          ][j          ])
            tempArr12.append(m[i          ][j + littleN])
            tempArr21.append(m[i + littleN][j          ])
            tempArr22.append(m[i + littleN][j + littleN])
        m11.append(tempArr11)
        m12.append(tempArr12)
        m21.append(tempArr21)
        m22.append(tempArr22)

    return m11, m12, m21, m22

def addM(mA,mB):
    N = len(mA)

    mC = []

    for i in range(N):
        tempArr = []
        for j in range(N):
            tempArr.append(int(mA[i][j]) + int(mB[i][j]))
        mC.append(tempArr)
        
    return mC

def subM(mA,mB):
    N = len(mA)

    mC = []

    for i in range(N):
        tempArr = []
        for j in range(N):
            tempArr.append(int(mA[i][j]) - int(mB[i][j]))
        mC.append(tempArr)

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

    mC = [[0] * N] * N

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
    menuString += ' 5 - Executar calculo dos produtos 30 vezes' + '\n'
    menuString += ' 6 - Sair' + '\n'
    print(menuString)
    option = int(input(">> "))
    if option == 1:
        generateMatriz()
    elif option == 2:
        result = calculateProduct()
        tempo1 = result[1]
    elif option == 3:
        t3 = time.time()
        result = strassenMult(matrizA,matrizB)
        t4 = time.time()
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
        break
    elif option == 5:
        print('Executando teste para matrizes 128 x 128, 30 vezes')
        tempoAlg1 = []
        tempoAlg2 = []
        readFileMatrix()

        for i in range(30):
            print('Calculando o produto 1...')
            t01 = time.time()
            result = calculateProduct()
            t02 = time.time()
            tempoAlg1.append(t02-t01)
            print('Calculando o produto 2...')
            t03 = time.time()
            result = strassenMult(matrizA,matrizB)
            t04 = time.time()
            tempoAlg2.append(t04-t03)
            print(i)
        arquivoSaidaTempo = open('./Data/tempo.txt', 'w')
        stringTempo1 = ''
        stringTempo2 = ''
        concatStringTempo = ''
        for i in range(len(tempoAlg1)):
            stringTempo1 += str(tempoAlg1[i]) + '\n'
        for i in range(len(tempoAlg2)):
            stringTempo2 += str(tempoAlg2[i]) + '\n'
        concatStringTempo = stringTempo1 + '\n\n\n\n' + stringTempo2
        arquivoSaidaTempo.write(concatStringTempo)
        arquivoSaidaTempo.close()
    elif option == 6:
        print('Encerramento solicitado pelo usuario.')
        break
    else:
        print('Opcao invalida.')
