letras = [
    ["a","b","c","d","e"],
    ["f","g","h","i","j"],
    ["k","l","m","n","o"],
    ["p","q","r","s","t"],
    ["u","v","w","x","y"],
    ["z","","","","",]
]
  
for i in range(0,6):
    for j in range(0,5):
        if letras[i][j] !="":
            print(f"[{i}][{j}] = {letras[i][j]}")