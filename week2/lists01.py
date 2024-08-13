dailyWaterList = [500, 300, 700, 600]
totalWater = 0
for i in dailyWaterList:
    totalWater += i
totalWL = totalWater/1000
if totalWL >= 2:
    target = "Günlük hedefine ulaştın."
else:
    target = "Günlük hedefinin gerisinde kaldın."
print(f"Bu gün {totalWL} litre su içtin.\n{target}")
