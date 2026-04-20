import random

def royxatni_shuffle(qaysi_royxat):
    random.shuffle(qaysi_royxat)
    return qaysi_royxat

# Misol uchun royxat
royxat = [1, 2, 3, 4, 5]

print("Asl royxat:", royxat)
print("Shuffle qilingan royxat:", royxatni_shuffle(royxat))
