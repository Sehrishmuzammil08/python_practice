#saquare star pattern
 for i in range(4):
     for j in range(4):
         print("*", end=" ")
     print()



# #triangle pattern
 for i in range(1, 6):
     for j in range(i):
         print("*", end=" ")
     print()


#num in a gird format(rows 3 , coiumn 4)
num = 1
for i in range(3):
    for j in range(4):
        print(num, end="\t")
        num += 1
    print()
