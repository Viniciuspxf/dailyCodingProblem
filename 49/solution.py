from numpy import minimum


def solution(array:list)->int:
  auxiliarList = [0]
  maxIndex = 0
  minimumIndex = 0

  for integer in array:
    auxiliarList.append(auxiliarList[-1] + integer)

  for i in range(len(auxiliarList)):
    if auxiliarList[i] >= auxiliarList[maxIndex]:
      maxIndex = i

  for j in range(maxIndex + 1):
    if auxiliarList[j] <= auxiliarList[minimumIndex]:
      minimumIndex = j

  return auxiliarList[maxIndex] - auxiliarList[minimumIndex]

def erickSolution(array:list)->int:
  currentSum = 0
  maxSum = 0

  for integer in array:
    currentSum = max(currentSum + integer, integer)
    maxSum = max(currentSum, maxSum)
  
  return maxSum

assert solution([34, -50, 42, 14, -5, 86]) == 137

assert solution([-5, -1, -8, -9]) == 0

assert erickSolution([34, -50, 42, 14, -5, 86]) == 137

assert erickSolution([-5, -1, -8, -9]) == 0

# erick solution is better (use less space)