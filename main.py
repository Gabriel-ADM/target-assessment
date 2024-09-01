import json


def qst1():
    indice, soma, k = 13, 0, 0
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma


def qst2(n):
    inicial0, inicial1 = 0, 1

    if n == 0 or n == 1:
        return True

    while inicial1 < n:
        inicial0, inicial1 = inicial1, inicial0 + inicial1

    return inicial1 == n


def qst3(data):
    fats = [item["faturamento"] for item in data if item["faturamento"] > 0]

    menor_fat = min(fats)
    maior_fat = max(fats)
    media = sum(fats) / len(fats)

    dias_acima_da_media = len([f for f in fats if f > media])

    return menor_fat, maior_fat, dias_acima_da_media


with open("faturamento_qst3.json", "r") as file:
    dados_faturamento = json.load(file)

menor, maior, dias_acima_media = qst3(dados_faturamento)


def qst4():
    # Valores de faturamento mensal por estado
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53,
    }

    # Calculando o valor total de faturamento
    faturamento_total = sum(faturamento_estados.values())

    # Calculando e exibindo o percentual de cada estado
    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"\t{estado} representa {percentual:.2f}% do faturamento mensal.")


def qst5(string_base):
    string_invertida = ""

    for i in range(len(string_base) - 1, -1, -1):
        string_invertida += string_base[i]

    return string_invertida


print(f"Questão 1:\n \t{qst1()}")

print(
    f"Questão 2:\n \tO número 4 está na sequência de Fibonacci: {qst2(4)}\n\tO número 13 está na sequência de Fibonacci: {qst2(13)}"
)

print(
    f"""Questão 3:
        Menor valor de faturamento ocorrido em um dia do mês: {menor}
        Maior valor de faturamento ocorrido em um dia do mês: {maior}
        Número de dias no mês em que o faturamento foi superior à média mensal: {dias_acima_media}"""
)

print("Questão 4:")
qst4()

palavra = "banana"
print(f"Questão 5:\n\tString inicial: {palavra}\tString invertida: {qst5(palavra)}")
