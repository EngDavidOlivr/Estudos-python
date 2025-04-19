
# 📘 Calculadora de Fatorial em Python

Este programa em Python permite calcular o **fatorial de um número inteiro não negativo** utilizando uma **função recursiva**. Ele também conta com tratamento de erros para garantir que o usuário digite um valor válido.

---

## 🚀 Funcionalidades

- ✅ Solicita ao usuário um número inteiro não negativo.
- 🧮 Calcula o fatorial do número utilizando recursão.
- 📤 Exibe o resultado formatado na tela.
- 🛡️ Trata entradas inválidas (ex: letras, números negativos).

---

## 🧠 Como funciona

1. A função `fatorial(n)` verifica se `n` é igual a 0 (caso base) e retorna 1.
2. Caso contrário, ela retorna `n * fatorial(n - 1)` (caso recursivo).
3. O programa solicita um número até que uma entrada válida seja informada.
4. Após receber um número válido, o fatorial é calculado e exibido.

---

## 💻 Execução

Para executar o programa, salve-o como `fatorial.py` e rode com:

```bash
python fatorial.py
```

Exemplo de uso:

```bash
Digite um número inteiro não negativo: 5
O fatorial de 5 é 120.
```

---

## ⚠️ Validações

- ❌ Números negativos não são aceitos.
- 🔁 Solicita nova entrada se a anterior for inválida.
- 🧾 Mensagens de erro claras em caso de entrada incorreta.

---

## 📝 Exemplo interativo

```text
Digite um número inteiro não negativo: -3
Por favor, digite um número inteiro não negativo.

Digite um número inteiro não negativo: abc
Entrada inválida. Por favor, digite um número inteiro.

Digite um número inteiro não negativo: 4
O fatorial de 4 é 24.
```

---

## 📄 Licença

Este projeto está disponível sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir.
