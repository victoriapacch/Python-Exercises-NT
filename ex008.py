medida = float(input("Digite um valor em metros: "))
print("Medida em metros:", medida)
cm = medida * 100
print("Convertido para centímetros:", cm)
mm = medida * 1000
print("Convertido para milímetros:", mm)
km = medida / 1000
print("Convertido para quilômetros:", km)
print("O valor especificado equivale a {}cm, {}mm e {}km".format(cm, mm, km))