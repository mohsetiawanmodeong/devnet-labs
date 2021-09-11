# devices=["R1","R2","R3","S1","S2"]
# for item in devices:
#     print(item)

# devices=["R1","R2","R3","S1","S2"]
# for item in devices:
#     if "R" in item:
#         print(item)

devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
switches