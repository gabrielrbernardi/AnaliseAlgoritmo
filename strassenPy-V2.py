def normalMult(mA,mB):
  N = len(mA)

  mC = [[0 for x in range(N)] for x in range(N)]

  for i in range(N):
    for j in range(N):
      c = 0
      for k in range (N):
        c += mA[i][k] * mB[k][j]
      mC[i][j] = c
      
  return mC

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
      mC[i][j] = mA[i][j] + mB[i][j]
      
  return mC

def subM(mA,mB):
  N = len(mA)

  mC = [[0 for i in range(N)] for i in range(N)]

  for i in range(N):
    for j in range(N):
      mC[i][j] = mA[i][j] - mB[i][j]
      
  return mC

def strassenMult(mA,mB):
  N = len(mA)
  
  if N == 1:
    return [[mA[0][0] * mB[0][0]]]
  
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

  return mC

MA = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
MB = [[3,3,3,3],[3,3,3,3],[3,3,3,3],[3,3,3,3]]

print("Normal Mult:\n",normalMult(MA,MB))
print("")
print("Strassen Mult:\n",strassenMult(MA,MB))