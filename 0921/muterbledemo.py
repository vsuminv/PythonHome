import copy 

original = [1,2,3]
target = original
target = copy.deepcopy(original) #multable을 emutable로 바꿔줌
print(original,target)
original[0] = 10000
print(original,target) #두 다 바뀜