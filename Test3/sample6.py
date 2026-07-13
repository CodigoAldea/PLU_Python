salery_reporta = [40000, 12000, 67000, 19000, 19000]
salery_reportb = [30000, 45000, 60000]
i = j = 0
merged = []
while i < len(salery_reporta) and j < len(salery_reportb):
    if salery_reporta[i] <= salery_reportb[j]:
        merged.append(salery_reporta[i])
        i += 1
    else:
        merged.append(salery_reportb[j])
        j += 1
while i < len(salery_reportb):
    merged.append(salery_reporta[i])
    i += 1
while j < len(salery_reportb):
    merged.append(salery_reportb[j])
    j += 1
print("Combined Salary Report (Ascending):")
for s in merged:
    print(s)
        