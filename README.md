Aqui está um exemplo de um README detalhado para o arquivo Python que você desenvolveu:

---

# Avaliação Técnica - Targett Systems

Este repositório contém a implementação de cinco algoritmos, desenvolvidos como parte de uma avaliação técnica para uma vaga de estágio na **Targett Systems**. Cada algoritmo foi projetado para resolver uma questão específica, conforme descrito a seguir.

## Estrutura do Projeto

O código principal está contido no arquivo `main.py`. Ele é dividido em funções, cada uma correspondente a uma questão da avaliação.

### Questão 1

**Descrição:**
- Calcula a soma de uma sequência de números inteiros de 1 até um valor definido (neste caso, `13`).

**Função:**
- `qst1()`: Retorna a soma de todos os números de 1 até 13.

### Questão 2

**Descrição:**
- Verifica se um número pertence à sequência de Fibonacci.

**Função:**
- `qst2(n)`: Recebe um número `n` e retorna `True` se `n` pertence à sequência de Fibonacci e `False` caso contrário.

### Questão 3

**Descrição:**
- Calcula o menor e o maior valor de faturamento diário em um mês, bem como o número de dias em que o faturamento foi superior à média mensal. Os dados de faturamento são fornecidos em formato JSON.

**Função:**
- `qst3(data)`: Recebe os dados de faturamento diário como entrada e retorna:
  - O menor valor de faturamento.
  - O maior valor de faturamento.
  - O número de dias em que o faturamento foi superior à média mensal.

**Dados:**
- Os dados de faturamento são carregados a partir do arquivo `faturamento_qst3.json`.

### Questão 4

**Descrição:**
- Calcula o percentual de representação que cada estado teve dentro do valor total de faturamento mensal de uma distribuidora.

**Função:**
- `qst4()`: Calcula e imprime o percentual de faturamento para os estados de SP, RJ, MG, ES, e "Outros".

### Questão 5

**Descrição:**
- Inverte os caracteres de uma string sem utilizar funções prontas, como `reverse()`.

**Função:**
- `qst5(string_base)`: Recebe uma string como entrada e retorna a string invertida.

## Execução do Código

Para executar o código, siga as etapas abaixo:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/avaliacao-targett.git
    cd avaliacao-targett
    ```

2. **Garanta que você tem o Python instalado:**

    Certifique-se de que o Python está instalado na sua máquina. Você pode verificar isso executando `python --version` no terminal.

3. **Execute o arquivo Python:**

    ```bash
    python main.py
    ```

4. **Visualize a saída:**

    O código imprimirá as respostas das cinco questões no terminal, com a formatação apropriada.

## Arquivos

- `main.py`: Contém todo o código-fonte para resolver as questões da avaliação.
- `faturamento_qst3.json`: Arquivo JSON que armazena os dados de faturamento utilizados na Questão 3.
