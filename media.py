b1 = float(input ("Digite a primeira nota: "))
b2 = float(input ("Digite a segunda nota: "))
b3 = float(input ("Digite a terceira nota nota: "))
b4 = float(input ("Digite a quarta nota: "))
media = (b1+b2+b3+b4) / 4


if media >= 7.0: 
     print(f"media: {media:.2f}""-situaçao: aprovado")    
elif media >= 5.0 and 7.0:
    print(f"media: {media:.2f}""recuperaçao")
else:
    print(f"media: {media:.2f}""reprovado") 