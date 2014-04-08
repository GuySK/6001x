def howMany(aDict):
    total = 0
    for k in aDict.keys():
        total += len(aDict[k])
    return total
# end of code