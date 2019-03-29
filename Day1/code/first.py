
# for x in range(1,10):
#     for y in range(1, x+1):
#         print("%s*%s=%s" % (x,y,x*y))

print("\n".join(" ".join(["%s*%s=%s" % (x, y, x*y) for x in range(1, y+1)]) for y in range(1, 10)))
print(list(" ".join(["%s*%s=%s" % (x, y, x*y) for x in range(1, y+1)]) for y in range(1, 10)))