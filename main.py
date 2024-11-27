from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from datetime import datetime


def gasolina(a):
    a = a * 6.60
    return a


def gasolinaadv(a):
    a = a * 6.77
    return a


def oleo(a):
    a = a * 6.59
    return a


def negative(Num1, Num2):
    if Num1 < Num2:
        a = Num2 - Num1
    else:
        a = Num1 - Num2
    return a

print("---------------------------")
print("           CAIXA           ")
print("---------------------------")

data_atual = datetime.today().date()

print("")
#Bombas de Gasolina
print("Bico 1")
(Bomba_comum) = float(input("Numeração 1: "))
Bomba1_comum = float(input("Numeração 2: "))
result_bomba = negative(Bomba_comum, Bomba1_comum)
valor_em_reais = gasolina(result_bomba)
print(f"Litros: {result_bomba:.2f} Reias: {valor_em_reais:.2f}")
print("--------------------------")

print("Bico2")
Bomba_comum2 = float(input("Numeração 1: "))
Bomba_comum3 = float(input("Numeração 2: "))
result_bomba2 = negative(Bomba_comum2, Bomba_comum3)
valor_em_reais2 = gasolina(result_bomba2)
print(f"litros: {result_bomba2:.2f} Reias: {valor_em_reais2:.2f}")
print("--------------------------")

print("Bico 3")
Bomba_comum4 = float(input("Numeração 1: "))
Bomba_comum5 = float(input("Numeração 2: "))
result_bomba3 = negative(Bomba_comum4, Bomba_comum5)
valor_em_reais3 = gasolina(result_bomba3)
print(f"litros: {result_bomba3:.2f} Reais: {valor_em_reais3:.2f}")
print("--------------------------")

#Bomba Gasolina Aditivada
print("    Gasolina Aditivada    ")
print("Bico 4:")
Bomba_adv = float(input("Numeração 1: "))
Bomba_adv2 = float(input("Numeração 2: "))
result_bomba4 = negative(Bomba_adv, Bomba_adv2)
valor_em_reais4 = gasolinaadv(result_bomba4)
print(f"litros:{result_bomba4:.2f} Reais: {valor_em_reais4:.2f}")
print("--------------------------")

#Bomba oleo Comum e S10
print("     Oleo Comum & S10     ")
print("Bico 5:")
bomba_s10 = float(input("Numeração 1: "))
bomba_s102 = float(input("Numeração 2: "))
result_bomba5 = negative(bomba_s10, bomba_s102)
valor_em_reais5 = oleo(result_bomba5)
print(f"litros: {result_bomba5:.2f} reias: {valor_em_reais5:.2f}")
print("--------------------------")

print("Bico 6:")
bomba_s101 = float(input("Numeração 1: "))
bomba_s103 = float(input("Numeração 2: "))
result_bomba7 = negative(bomba_s101, bomba_s103)
valor_em_reais7 = oleo(result_bomba7)
print(f"litros: {result_bomba7:.2f} reias: {valor_em_reais7:.2f}")
print("--------------------------")

print("Bico 7:")
bomba_s500 = float(input("Numeração 1: "))
bomba_s5002 = float(input("Numeração 2: "))
result_bomba6 = negative(bomba_s500, bomba_s5002)
valor_em_reais6 = oleo(result_bomba6)
print(f"litros: {result_bomba6:.2f} reias: {valor_em_reais6:.2f}")

Total_litros = result_bomba + result_bomba2 + result_bomba3 + result_bomba4 + result_bomba5 + result_bomba6 + result_bomba7
Total_reias = valor_em_reais + valor_em_reais2 + valor_em_reais3 + valor_em_reais4 + valor_em_reais5 + valor_em_reais6 + valor_em_reais7

print("===========================")
print(F"   Total litros: {Total_litros:.2f}")
print(F"   Total Reais: {Total_reias:.2f}")
print("===========================")

print("Diversos:")
diversos = float(input("Quanto foi vendido: "))
Bomba_diversos_total = Total_reias + diversos

print(f"TOTAL BOMBA + DIVERSOS: {Bomba_diversos_total:.2f}")

print("---------------------------------")
print("RECEBIDO")

cofre = float(input("Cofre: "))
dinheiro = float(input("Dinheiro: "))
vale_diverso = float(input("Vale Diversos: "))
vale_pmm = float(input("Vale PMM: "))
vale_pmm_diesil = float(input("Vale PMM DS500: "))
vale_pmm_diesil500 = float(input("Vale PMM DS10: "))
cartao = float(input("Cartao: "))
moeda = float(input("Moeda: "))
shell_box = float(input("Shell Box: "))
desconto = float(input("Desconto: "))

resultado_recebido = (cofre + desconto + dinheiro + vale_diverso +
                      vale_pmm_diesil + vale_pmm + cartao + moeda + shell_box + desconto + vale_pmm_diesil500)

print("===========================")
print(f"Total Recebido: {resultado_recebido:.2f}")
print("===========================")

total = Total_reias - resultado_recebido

print(total)

if total < 0:
    print("CAIXA FALTANDO!!")
else:
    print("CAIXA BATIDO!")

print("===========================")

print(f"GA: {Bomba_adv} - {Bomba_adv2}")
print(f"GC: {Bomba_comum} - {Bomba1_comum}")
print(f"GC: {Bomba_comum2} - {Bomba_comum3}")
print(f"GC: {Bomba_comum4} - {Bomba_comum5}")
print(f"DS: {bomba_s10} - {bomba_s102}")
print(f"DS: {bomba_s101} - {bomba_s103}")
print(f"DC: {bomba_s500} - {bomba_s5002}")
print("------------------------------")
print(f"      Cofre: {cofre}         ")
print("------------------------------")
print(F"Din:      {dinheiro}")
print(F"Mo:       {moeda}")
print(f"VDS:      {vale_diverso}")
print(f"VPMM:     {vale_pmm}")
print(f"VPMMs10:  {vale_pmm_diesil}")
print(f"VPMMs500: {vale_pmm_diesil500}")
print(f"Cartao:   {cartao}")
print(f"ShellBox: {shell_box}")
print(f"Desconto: {desconto}")
print("------------------------------")
print(F"    Diversos: {diversos}     ")

while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Courier-Bold", 13)
    c.drawString(50, 765, f"       {data_atual}           ")
    c.drawString(50, 750, f"Ga:{Bomba_adv} - {Bomba_adv2}")
    c.drawString(50, 735, f"Gc:{Bomba_comum} - {Bomba1_comum}")
    c.drawString(50, 720, f"Gc:{Bomba_comum2} - {Bomba_comum3}")
    c.drawString(50, 705, f"Gc:{Bomba_comum4} - {Bomba_comum5}")
    c.drawString(50, 690, f"Ds:{bomba_s10} - {bomba_s102}  ")
    c.drawString(50, 675, f"Ds:{bomba_s101} - {bomba_s103}  ")
    c.drawString(50, 660, f"Dc:{bomba_s500} - {bomba_s5002} ")
    c.drawString(50, 645, "")
    c.drawString(50, 630, f"      Cofre: {cofre}                 ")
    c.drawString(50, 615, "")
    c.drawString(50, 600, f"Din:{dinheiro}          ")
    c.drawString(50, 585, F"Mo:{moeda}             ")
    c.drawString(50, 570, f"Vdi:{vale_diverso}      ")
    c.drawString(50, 555, f"Vpmm:{vale_pmm}          ")
    c.drawString(50, 540, f"VpmmS10:{vale_pmm_diesil}   ")
    c.drawString(50, 525, f"VpmmS500:{vale_pmm_diesil500}")
    c.drawString(50, 510, f"Cartao:{cartao}            ")
    c.drawString(50, 495, f"ShellBox:{shell_box}         ")
    c.drawString(50, 480, f"Desconto:{desconto}          ")
    c.drawString(50, 465, "")
    c.drawString(50, 45045324, f"    Diversos: {diversos}      ")

    c.save()

create_pdf("CAIXA.pdf")