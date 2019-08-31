stairSize = int(input("\nКоличество ступеней лестницы: "))
jumps = list(map(int, input("Возможные шаги в порядке возрастания: ").split()))
ans = [] 
sizeJ = len(jumps)
#########################################################################################################   
for i in range(0, stairSize):
    curr = 0                        # current calculated element
    lim = min(i, sizeJ-1)
    for j in range(lim+1):
        cstep = jumps[j]            # current step from jumps array
        if (i+1 < cstep):
            break
        curr += 1 if cstep == i+1 else ans[-cstep]
    
    ans.append(curr)
    if (i >= jumps[-1]):
        ans.pop(0)
#########################################################################################################        
print("\nЧисло способов: ", ans[-1])




























   