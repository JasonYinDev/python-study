names=[1,2,3]
ages=[2,3,4]

xNames=set(names) #{1,2,3}  set format
xAge=set(ages)

xResult=xNames & xAge
print(f"交集为{xResult}")

yResult=xNames | xAge
print(f"并集为{yResult}")

zResult=xNames-xAge
print(f"差集为{zResult}")

print(f"to list {list(zResult)}")