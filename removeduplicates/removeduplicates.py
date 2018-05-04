#provided array with duplicates
names = ["Alex","John","Mary","Steve","John", "Steve"]
#empty array for sotring only unique entries
dupe_check = []

#populate empty array with unique entries only
for name in names:
    if name not in dupe_check:
        dupe_check.append(name)

#set names array equal to the unique only version
names = dupe_check

#print out the result
print(names)
