# Sistema de Cadastro de Funcionários — Academia

Sistema em Python para gerenciamento de registros de funcionários de uma academia por meio de uma interface de linha de comando (CLI). O projeto utiliza listas para armazenamento em memória e concentra cadastro, consulta, edição, exclusão, validações e cálculos salariais em uma única aplicação.

## Funcionalidades

- Cadastro de novos funcionários com 15 atributos.
- Listagem completa dos funcionários cadastrados.
- Consulta de aniversariantes por mês.
- Edição de dados de um funcionário por matrícula.
- Exclusão de funcionário com confirmação.
- Definição do limite de funcionários no início da execução.
- Limite global configurado em `50` funcionários.
- Prevenção de matrículas e CPFs duplicados.
- Validação de datas, telefone, sexo, turno, salário e carga horária.
- Tratamento de entradas inválidas para evitar encerramentos inesperados.
- Cálculo de acréscimos, descontos, salário líquido e valor da hora trabalhada.

## Tecnologias

- **Python 3**
- Biblioteca padrão **`datetime`**

O projeto não utiliza bibliotecas externas, banco de dados, frameworks ou ferramentas adicionais.

## Estrutura dos dados

Os registros são armazenados em uma lista principal:

```python
funcionarios = []
```

Cada funcionário é representado por outra lista com 15 campos:

1. Nome
2. Matrícula
3. Telefone
4. Dia de nascimento
5. Mês de nascimento
6. Ano de nascimento
7. Sexo
8. Salário
9. Logradouro
10. Número do endereço
11. Complemento
12. Carga horária
13. Turno de trabalho
14. CPF
15. Cargo

O acesso aos campos é feito por constantes de índice, como `NOME`, `MATRICULA`, `SALARIO` e `CPF`, mantendo a organização da estrutura vetorizada utilizada no projeto.

## Cálculos implementados

O sistema possui quatro funções específicas de cálculo:

- `CMC_Acrescimos()` — aplica acréscimo conforme o turno:
  - Manhã: `0%`
  - Tarde: `5%`
  - Noite: `20%`
- `CMC_Descontos()` — aplica desconto didático de `8%` sobre o salário-base.
- `CMC_Sal_Liquido()` — calcula salário-base + acréscimos - descontos.
- `CMC_Valor_Hora()` — calcula o valor aproximado da hora com base na carga horária.

> Os percentuais utilizados fazem parte da lógica didática do projeto e não representam necessariamente regras trabalhistas reais.

## Como executar

Certifique-se de ter o Python 3 instalado.

No terminal, execute:

```bash
python cadastro_academia_completo.py
```

Ao iniciar, o sistema solicitará o limite de funcionários para a execução atual e, em seguida, exibirá o menu principal.

## Menu da aplicação

```text
[1] Incluir Novo Funcionário
[2] Gerar Lista de Funcionários
[3] Listar Aniversariantes do Mês
[4] Terminar o Programa
[5] Editar Funcionário
[6] Excluir Funcionário
```

A opção `4` encerra a aplicação. As demais operações retornam ao menu principal após a conclusão.

## Validações e tratamento de erros

O programa possui validações para tornar a entrada de dados mais segura e consistente, incluindo:

- números inteiros e decimais;
- datas inexistentes ou futuras;
- campos obrigatórios;
- matrícula e CPF duplicados;
- CPF com 11 dígitos;
- telefone com quantidade mínima de números;
- sexo e turno de trabalho;
- carga horária positiva;
- confirmações de exclusão.

Também são utilizados blocos `try/except` para impedir que erros comuns de entrada interrompam a execução do sistema.

## Limitações e possíveis evoluções

A versão atual mantém todos os registros apenas em memória. Ao encerrar o programa, os dados cadastrados são perdidos.

Possíveis evoluções incluem:

- persistência em arquivo ou banco de dados;
- validação completa dos dígitos verificadores do CPF;
- pesquisa por outros campos além da matrícula;
- relatórios e filtros adicionais;
- interface gráfica ou versão web.

---

Projeto desenvolvido com foco em organização de código, modularização por funções, validação de entradas e manipulação de estruturas de dados em Python.
