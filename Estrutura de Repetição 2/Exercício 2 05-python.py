paisA = 90000000
paisB = 140000000
ano = 0

while paisA < paisB:
    paisA += (paisA*0.035)
    paisB += (paisB*0.01)
    ano += 1
print(ano,"Anos")