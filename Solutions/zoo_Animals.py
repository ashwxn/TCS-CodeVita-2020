costHerb,costCarn,costAqua = list(map(int,input().strip().split()))
maxHerb,maxCarn,maxAqua = list(map(int,input().strip().split()))
minHerb,minHerbArea = list(map(int,input().strip().split()))
minCarn,minCarnArea = list(map(int,input().strip().split()))
minAqua,minAquaArea =list(map(int,input().strip().split()))
totArea = int(input().strip())
win = [] 
ash = ["Herb","Carn","Aqua"]
cost_list = {costHerb:"Herb",costCarn:"Carn",costAqua:"Aqua"}
max_area = {"Herb":maxHerb,"Carn":maxCarn,"Aqua":maxAqua}
min_Ani = {"Herb":minHerb,"Carn":minCarn,"Aqua":minAqua}
ani_Area = {"Herb":minHerbArea,"Carn":minCarnArea,"Aqua":minAquaArea}

minCostType = min(costAqua,costHerb,costCarn)
win.append(cost_list.get(min(costAqua,costHerb,costCarn)))
zooCost = max_area.get(cost_list.get(minCostType))*minCostType

totArea = totArea - max_area.get(cost_list.get(minCostType))

maxCostType = max(costHerb,costAqua,costCarn)
zooCost = zooCost + ani_Area.get(cost_list.get(maxCostType))*min_Ani.get(cost_list.get(maxCostType))*maxCostType
win.append(cost_list.get(max(costAqua,costHerb,costCarn)))
totArea = totArea - ani_Area.get(cost_list.get(maxCostType))*min_Ani.get(cost_list.get(maxCostType))
ashwin = list(set(ash) - set(win))
ashwin = "".join(ashwin)
for key,value in cost_list.items():
    if value==ashwin:
        rem = key 
zooCost = zooCost +  totArea * rem
print(zooCost,end="")