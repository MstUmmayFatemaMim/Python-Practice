                    ######### DEEP Copy --> Value and Location always changed
import copy
Dcopy=[4,5,6,8]
Dcopy1=copy.deepcopy(Dcopy)
print("Deep Copy : ")
Dcopy1[1]=5000
print(f"Dcopy: {Dcopy}",f"Dcopy1: {Dcopy1}")
print(f"Dcopy: {id(Dcopy)}",f"Dcopy1: {id(Dcopy1)}")

        ###### 'In a normal list shallow===Deep Copy  creating fully independent objects.

DPcopy=[[4, 5, 6, 8], [7, 3, 2, 9], [34, 55, 63, 88]]
DPcopy1=copy.deepcopy(DPcopy)
print(f"DPcopy: {DPcopy}",f"Deep Copy : {DPcopy1}")
DPcopy[1][0]=333
print("Deep Copy Nested : ")
print(f"DPcopy: {DPcopy}",f"DPcopy1: {DPcopy1}")
print(f"DPcopy: {id(DPcopy)}",f"DPcopy1: {id(DPcopy1)}")
