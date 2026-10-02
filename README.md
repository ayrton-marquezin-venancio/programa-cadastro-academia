# Sistema de Cadastro de Funcionários — Academia

Sistema de gerenciamento de funcionários desenvolvido em **Python**, com execução em terminal e foco em organização de código, validação de dados, manipulação de listas e construção de um fluxo completo de cadastro.

O projeto foi estruturado para representar, de forma didática e funcional, algumas operações comuns em sistemas administrativos: **cadastro, consulta, edição, exclusão e processamento de informações de funcionários**. Apesar de simples, a aplicação foi organizada de modo a separar responsabilidades em funções específicas e manter uma lógica clara de execução.

---

## Visão geral

A aplicação gerencia funcionários de uma academia utilizando uma estrutura de dados baseada em **listas em memória**.

Cada funcionário é representado por uma lista com 15 campos, e todos os registros são armazenados dentro de uma lista principal chamada `funcionarios`.

O sistema permite:

- incluir novos funcionários;
- consultar todos os registros;
- localizar aniversariantes por mês;
- editar dados existentes;
- excluir funcionários;
- calcular informações salariais;
- validar entradas;
- impedir duplicidades importantes;
- manter o programa em execução por meio de um menu interativo.

A lógica foi construída sem banco de dados, frameworks ou bibliotecas externas, permitindo que todo o funcionamento seja observado diretamente no código.

---

## Objetivo do projeto

A proposta técnica do projeto é simular um pequeno sistema administrativo de RH para uma academia, trabalhando conceitos fundamentais de programação de maneira integrada.

Entre os principais conceitos aplicados estão:

- estruturas de dados;
- listas aninhadas;
- funções;
- constantes;
- laços de repetição;
- estruturas condicionais;
- tratamento de exceções;
- validação de dados;
- busca sequencial;
- atualização de registros;
- exclusão de elementos;
- modularização lógica;
- interação com o usuário por terminal.

O sistema também busca demonstrar uma preocupação com situações reais de uso. Um funcionário pode não apenas ser cadastrado, mas também ter seus dados atualizados ao longo do tempo ou ser removido em caso de desligamento.

---

## Modelo de dados

O projeto utiliza uma lista principal:

```python
funcionarios = []
```

Cada funcionário é armazenado como uma lista com exatamente 15 campos:

```text
0  - Nome
1  - Matrícula
2  - Telefone
3  - Dia de nascimento
4  - Mês de nascimento
5  - Ano de nascimento
6  - Sexo
7  - Salário
8  - Logradouro
9  - Número do endereço
10 - Complemento
11 - Carga horária
12 - Turno de trabalho
13 - CPF
14 - Cargo
```

Para evitar o uso de números diretamente em várias partes do código, foram definidas constantes:

```python
NOME = 0
MATRICULA = 1
TELEFONE = 2
DIA = 3
MES = 4
ANO = 5
SEXO = 6
SALARIO = 7
LOGRADOURO = 8
NUMERO_ENDERECO = 9
COMPLEMENTO = 10
CARGA_HORARIA = 11
TURNO_TRABALHO = 12
CPF = 13
CARGO = 14
```

Isso permite escrever:

```python
funcionario[SALARIO]
```

em vez de:

```python
funcionario[7]
```

Essa escolha melhora a legibilidade e reduz o risco de utilizar posições incorretas.

---

## Limite de funcionários

O sistema possui um limite global configurado por meio da constante:

```python
MAX_FUNCIONARIOS = 50
```

Além desse limite absoluto, o usuário define no início da execução quantos funcionários deseja permitir naquela sessão.

Exemplo:

```text
Defina o limite de funcionários desta execução [1-50]:
```

Dessa forma, o sistema trabalha com dois níveis de controle:

1. um limite máximo definido pelo programa;
2. um limite operacional escolhido pelo usuário.

A inclusão de novos registros é bloqueada quando qualquer um desses limites é atingido.

---

## Funcionalidades

### 1. Cadastro de funcionários

A inclusão de um novo funcionário solicita os 15 campos definidos no modelo de dados.

Antes de inserir o registro na lista principal, o sistema realiza diversas validações, como:

- matrícula não duplicada;
- CPF não duplicado;
- CPF com 11 dígitos;
- data de nascimento válida;
- data não futura;
- telefone com quantidade mínima de números;
- salário válido;
- carga horária maior que zero;
- sexo dentro das opções aceitas;
- turno de trabalho válido;
- campos obrigatórios não vazios.

Após a validação, o funcionário é adicionado com:

```python
funcionarios.append(funcionario)
```

---

### 2. Listagem completa

A opção de listagem percorre todos os funcionários cadastrados e exibe os dados armazenados.

Além das informações cadastrais, o sistema calcula dinamicamente:

- acréscimos;
- descontos;
- salário líquido;
- valor aproximado da hora trabalhada.

Esses valores não são armazenados como novos campos. Eles são recalculados com base nas informações atuais do funcionário.

Essa decisão evita redundância e garante que alterações em salário, turno ou carga horária sejam refletidas imediatamente.

---

### 3. Consulta de aniversariantes

O sistema permite informar um mês entre `1` e `12` e buscar todos os funcionários cujo campo `MES` corresponda ao valor informado.

Os registros encontrados são armazenados temporariamente em uma lista auxiliar:

```python
aniversariantes = []
```

Depois, são ordenados pelo dia do nascimento antes da exibição.

Esse recurso demonstra:

- filtragem;
- criação de lista auxiliar;
- ordenação;
- consulta baseada em critérios.

---

### 4. Edição de funcionário

A edição é realizada por meio da matrícula.

O sistema:

1. solicita a matrícula;
2. localiza o funcionário;
3. exibe um resumo do registro;
4. apresenta um submenu com os campos editáveis;
5. atualiza apenas o campo escolhido.

A edição reutiliza as mesmas funções de validação do cadastro.

Isso é especialmente importante para CPF e matrícula. Durante a edição, o próprio funcionário é ignorado na verificação de duplicidade, evitando que seu valor atual seja interpretado como duplicado.

Exemplo conceitual:

```python
ler_matricula(funcionarios, indice_ignorado=indice)
```

e:

```python
ler_cpf(funcionarios, indice_ignorado=indice)
```

Essa abordagem mantém consistência entre inclusão e atualização de registros.

---

### 5. Exclusão de funcionário

A exclusão também utiliza a matrícula como identificador de busca.

Antes de remover o funcionário, o programa:

- localiza o registro;
- exibe dados resumidos;
- solicita confirmação com `S` ou `N`.

A remoção ocorre somente após confirmação:

```python
funcionarios.remove(funcionario)
```

Caso o usuário escolha não continuar, a operação é cancelada.

---

## Menu principal

O sistema utiliza um menu textual para controlar o fluxo da aplicação:

```text
[1] Incluir Novo Funcionário
[2] Gerar Lista de Funcionários
[3] Listar Aniversariantes do Mês
[4] Terminar o Programa
[5] Editar Funcionário
[6] Excluir Funcionário
```

A execução permanece ativa dentro de um laço enquanto a opção `4` não for escolhida.

Esse comportamento concentra todas as operações em uma única sessão de uso.

---

## Funções de cálculo

O programa possui quatro funções específicas para cálculos relacionados ao salário.

### `CMC_Acrescimos(salario, turno)`

Aplica um percentual conforme o turno:

```text
Manhã = 0%
Tarde = 5%
Noite = 20%
```

### `CMC_Descontos(salario)`

Aplica um desconto didático de:

```text
8% sobre o salário-base
```

### `CMC_Sal_Liquido(salario, acrescimos, descontos)`

Utiliza a fórmula:

```text
salário líquido = salário-base + acréscimos - descontos
```

### `CMC_Valor_Hora(salario, carga_horaria)`

Calcula:

```text
valor da hora = salário-base / carga horária
```

A função também protege contra divisão por zero.

> Os percentuais adotados fazem parte da lógica didática do projeto e não representam necessariamente regras trabalhistas reais.

---

## Validação de dados

Uma parte importante do projeto está concentrada nas funções de leitura e validação.

### Inteiros

A função `ler_inteiro()` utiliza `try/except` para impedir que entradas como letras encerrem o programa.

Também aceita limites mínimo e máximo.

### Valores decimais

`ler_float()` aceita números com ponto ou vírgula:

```text
1500.50
1500,50
```

### Datas

A data de nascimento é validada com:

```python
from datetime import date
```

Isso permite rejeitar situações como:

```text
31/02
```

ou datas futuras.

### Matrícula

A matrícula funciona como um dos principais identificadores do sistema e não pode ser repetida.

### CPF

O sistema:

- remove pontos, hífens e espaços;
- exige exatamente 11 dígitos;
- impede duplicidades.

A versão atual não implementa o algoritmo completo de validação dos dígitos verificadores do CPF.

### Sexo

São aceitas as opções:

```text
M
F
O
```

### Turno

São aceitos:

```text
Manhã
Tarde
Noite
```

O programa também aceita `manha` sem acento e normaliza o valor para `Manhã`.

---

## Tratamento de erros

O projeto utiliza tratamento de exceções para evitar que erros simples de entrada interrompam completamente a execução.

Entre as exceções tratadas estão:

```python
ValueError
TypeError
IndexError
ZeroDivisionError
KeyboardInterrupt
EOFError
```

O objetivo é manter o sistema operacional mesmo quando o usuário insere informações inválidas.

A abordagem combina validação preventiva com tratamento de exceções.

---

## Organização do código

O programa está organizado em blocos lógicos:

```text
1. Importações
2. Limite do sistema
3. Constantes dos campos
4. Funções de cálculo
5. Funções de leitura e validação
6. Funções auxiliares
7. Cadastro
8. Listagem
9. Aniversariantes
10. Edição
11. Exclusão
12. Menu
13. Programa principal
```

Essa separação reduz a quantidade de lógica concentrada em uma única função e facilita manutenção, testes e evolução do projeto.

---

## Busca de funcionários

A função responsável por localizar funcionários utiliza uma busca sequencial pela matrícula.

Conceitualmente, o algoritmo percorre a lista até encontrar uma correspondência.

Em termos de complexidade, a busca possui custo aproximado de:

```text
O(n)
```

onde `n` representa a quantidade de funcionários cadastrados.

Para a escala atual do projeto, esse método é simples e suficiente.

Em um sistema de maior porte, a estrutura poderia ser substituída ou complementada por mecanismos mais eficientes, como banco de dados e índices de busca.

---

## Fluxo da aplicação

O fluxo principal pode ser resumido da seguinte forma:

```text
Início
  ↓
Definição do limite
  ↓
Exibição do menu
  ↓
Escolha da operação
  ↓
Execução da função correspondente
  ↓
Retorno ao menu
  ↓
Opção 4
  ↓
Encerramento
```

A função `main()` centraliza essa lógica.

O programa é iniciado por:

```python
if __name__ == "__main__":
    main()
```

Esse padrão evita a execução automática do sistema caso o arquivo seja importado futuramente como módulo em outro projeto.

---

## Tecnologias utilizadas

- **Python 3**
- **datetime** — biblioteca padrão do Python
- Terminal / linha de comando

Não são utilizados:

- pandas;
- NumPy;
- frameworks;
- banco de dados;
- bibliotecas externas;
- interface gráfica.

Isso torna o projeto simples de executar e fácil de estudar.

---

## Como executar

É necessário possuir Python 3 instalado.

No terminal, acesse a pasta do projeto e execute:

```bash
python cadastro_academia_completo.py
```

Em alguns ambientes Windows também é possível utilizar:

```bash
py cadastro_academia_completo.py
```

Não é necessário instalar dependências adicionais.

---

## Decisões de projeto

Algumas decisões foram tomadas para manter o sistema simples, didático e coerente com a proposta.

### Uso de listas

Os registros foram mantidos em listas em vez de dicionários, classes ou banco de dados.

Essa escolha reforça o uso de estruturas vetorizadas e permite trabalhar diretamente com índices.

### Constantes para índices

As constantes em letras maiúsculas evitam o uso repetitivo de números mágicos no código.

### Reutilização de validações

As mesmas funções de validação são utilizadas em cadastro e edição, reduzindo duplicação de lógica.

### Cálculos sob demanda

Os valores derivados do salário não são armazenados. São calculados durante a exibição.

### Busca por matrícula

A matrícula foi adotada como principal referência para localizar registros em operações de edição e exclusão.

---

## Limitações atuais

A aplicação foi construída como um sistema local e em memória.

Por isso:

- os dados são perdidos ao encerrar o programa;
- não existe persistência em banco de dados ou arquivo;
- a busca é sequencial;
- não há autenticação;
- não há níveis de usuário;
- não existe histórico de alterações;
- não há interface gráfica;
- o CPF não possui validação completa dos dígitos verificadores;
- as regras salariais são didáticas.

Essas limitações fazem parte da versão atual e também indicam caminhos naturais para evolução.

---

## Possíveis evoluções

O projeto pode ser expandido futuramente com:

- persistência em JSON, CSV ou banco de dados;
- SQLite, PostgreSQL ou MySQL;
- validação completa de CPF;
- pesquisa por nome, cargo ou CPF;
- filtros por turno e cargo;
- relatórios;
- histórico de alterações;
- autenticação;
- perfis de acesso;
- exportação de dados;
- interface gráfica;
- API;
- aplicação web;
- testes automatizados;
- separação do código em módulos e pacotes.

Uma evolução natural seria substituir o armazenamento em memória por um banco de dados sem alterar a lógica principal de cadastro, consulta, edição e exclusão.

---

## Conceitos demonstrados

Este projeto reúne, em uma única aplicação, vários fundamentos importantes de desenvolvimento em Python:

```text
✓ variáveis e constantes
✓ listas
✓ listas aninhadas
✓ funções
✓ parâmetros
✓ retorno de valores
✓ estruturas condicionais
✓ loops
✓ validação de dados
✓ tratamento de exceções
✓ busca
✓ ordenação
✓ CRUD básico
✓ separação de responsabilidades
✓ fluxo de aplicação
```

Embora seja um sistema de pequeno porte, a estrutura utilizada representa uma base importante para compreender como aplicações maiores organizam operações sobre dados.

---

## Considerações finais

O **Sistema de Cadastro de Funcionários — Academia** foi desenvolvido para transformar conceitos fundamentais de Python em uma aplicação completa e interativa.

Mais do que simplesmente cadastrar dados, o projeto procura trabalhar o ciclo de vida de um registro:

```text
Criar → Consultar → Atualizar → Excluir
```

Esse fluxo aproxima o exercício de situações reais de desenvolvimento de software e cria uma base para futuras versões com persistência, banco de dados, interfaces e arquiteturas mais avançadas.
