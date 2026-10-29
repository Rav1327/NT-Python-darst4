def parol_yetarlimi(parol):
    if len(parol) >= 8:
        return True
    else:
        return False


natija = parol_yetarlimi("python123")
print(natija)
