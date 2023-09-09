n = int(input())
h = n//60//60
m = (h*60)- (n//60)
minutes = abs(m)
print(h, "час(а/ов)", "и", minutes, "минут(а/ы)")