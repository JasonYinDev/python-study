#add element

alphbeta=["a","b","c","d"]
alphbeta.append("e")

print(alphbeta)

alphbeta.extend(['f','g'])# alphbeta+=['f','g']
print(alphbeta)

alphbeta.insert(1,"X")
print(alphbeta)


#find element
  #in, not in, index,count
print("a" in alphbeta)
print("a" not in alphbeta)
print("y" not in alphbeta)

print(alphbeta.index("c"))

alphbeta.append("c")
print(alphbeta.count("c"))

#delet element
del alphbeta[0]#无返回值
print(alphbeta)

print(alphbeta.pop(0))#有返回值
print(alphbeta)

alphbeta.remove("c")
print(alphbeta)

alphbeta.reverse()
print(alphbeta)

