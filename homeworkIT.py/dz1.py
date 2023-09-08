def el(n):
    inelll: list = []
    
    for i in range (1, len(n)):
        if n[i] != n[i-1]+1:
            inelll.append(i)
            
    if inelll:
        return inelll
    else:
        return "не найдено"
            
