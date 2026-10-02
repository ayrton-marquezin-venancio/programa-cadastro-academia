# ============================================================
# SISTEMA DE CADASTRO DE FUNCIONÁRIOS DE UMA ACADEMIA
# ============================================================

from datetime import date


# ------------------------------------------------------------
# LIMITE ABSOLUTO DO SISTEMA
# ------------------------------------------------------------

MAX_FUNCIONARIOS = 50


# ------------------------------------------------------------
# POSIÇÕES DOS 15 CAMPOS NO REGISTRO DE CADA FUNCIONÁRIO
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# FUNÇÕES DE CÁLCULO
# ------------------------------------------------------------

def CMC_Acrescimos(salario, turno):
  
    if salario < 0:
        return 0.0

    if turno == "Manhã":
        percentual = 0.00

    elif turno == "Tarde":
        percentual = 0.05

    elif turno == "Noite":
        percentual = 0.20

    else:
        percentual = 0.00

    return salario * percentual


def CMC_Descontos(salario):
    
    if salario < 0:
        return 0.0

    return salario * 0.08


def CMC_Sal_Liquido(salario, acrescimos, descontos):
  
    return salario + acrescimos - descontos


def CMC_Valor_Hora(salario, carga_horaria):
    
    if carga_horaria <= 0:
        return 0.0

    return salario / carga_horaria


# ------------------------------------------------------------
# FUNÇÕES DE LEITURA E TRATAMENTO DE ERROS
# ------------------------------------------------------------

def ler_inteiro(mensagem, minimo, maximo=None):

    while True:
        try:
            valor = int(input(mensagem).strip())

            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_float(mensagem, minimo):
    
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            valor = float(texto)

            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ler_texto(mensagem):
    
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("Este campo é obrigatório e não pode ficar vazio.")


def ler_telefone():
    
    while True:
        telefone = input("Telefone: ").strip()
        somente_numeros = "".join(
            caractere for caractere in telefone if caractere.isdigit()
        )

        if len(somente_numeros) >= 8:
            return telefone

        print("Telefone inválido. Digite um telefone com pelo menos 8 números.")


def ler_data_nascimento():
   
    while True:
        dia = ler_inteiro("Dia de nascimento: ", 1, 31)
        mes = ler_inteiro("Mês de nascimento: ", 1, 12)
        ano = ler_inteiro("Ano de nascimento: ", 1900, date.today().year)

        try:
            nascimento = date(ano, mes, dia)

            if nascimento > date.today():
                print("A data de nascimento não pode estar no futuro.")
                continue

            return dia, mes, ano

        except ValueError:
            print("Data inexistente. Digite a data novamente.")


def ler_matricula(funcionarios, indice_ignorado=None):
    
    while True:
        matricula = ler_texto("Matrícula: ")
        repetida = False

        for indice, funcionario in enumerate(funcionarios):
            
            if indice == indice_ignorado:
                continue

            if funcionario[MATRICULA].lower() == matricula.lower():
                repetida = True
                break

        if repetida:
            print("Essa matrícula já está cadastrada.")
        else:
            return matricula


def ler_cpf(funcionarios, indice_ignorado=None):
    
    while True:
        cpf_digitado = input("CPF (11 números): ").strip()

        cpf = cpf_digitado.replace(".", "")
        cpf = cpf.replace("-", "")
        cpf = cpf.replace(" ", "")

        if not cpf.isdigit():
            print("CPF inválido. Utilize apenas números, pontos ou hífen.")
            continue

        if len(cpf) != 11:
            print("CPF inválido. O CPF deve possuir exatamente 11 dígitos.")
            continue

        repetido = False

        for indice, funcionario in enumerate(funcionarios):

            if indice == indice_ignorado:
                continue

            if funcionario[CPF] == cpf:
                repetido = True
                break

        if repetido:
            print("Esse CPF já está cadastrado.")

        else:
            return cpf


def ler_sexo():

    while True:
        sexo = input("Sexo [M/F/O]: ").strip().upper()

        if sexo in ("M", "F", "O"):
            return sexo

        print("Opção inválida. Digite M, F ou O.")


def ler_turno():

    while True:
        turno = input("Turno [Manhã/Tarde/Noite]: ").strip().lower()

        if turno in ("manhã", "manha"):
            return "Manhã"

        if turno == "tarde":
            return "Tarde"

        if turno == "noite":
            return "Noite"

        print("Turno inválido. Digite Manhã, Tarde ou Noite.")


def ler_confirmacao(mensagem):
   
    while True:
        resposta = input(mensagem).strip().upper()

        if resposta in ("S", "N"):
            return resposta

        print("Opção inválida. Digite apenas S ou N.")


# ------------------------------------------------------------
# FUNÇÕES AUXILIARES DE BUSCA E EXIBIÇÃO
# ------------------------------------------------------------

def localizar_funcionario_por_matricula(funcionarios, matricula):
    
    for indice, funcionario in enumerate(funcionarios):
        if funcionario[MATRICULA].lower() == matricula.lower():
            return indice

    return -1


def exibir_dados_resumidos(funcionario):

    print("Nome:", funcionario[NOME])
    print("Matrícula:", funcionario[MATRICULA])
    print("CPF:", funcionario[CPF])
    print("Cargo:", funcionario[CARGO])


# ------------------------------------------------------------
# OPÇÃO 1 - INCLUIR NOVO FUNCIONÁRIO
# ------------------------------------------------------------

def incluir_novo_funcionario(funcionarios, limite):

    if len(funcionarios) >= limite:
        print("\nNão é possível cadastrar outro funcionário.")
        print(f"O limite definido para esta execução é de {limite} funcionário(s).")
        return

    if len(funcionarios) >= MAX_FUNCIONARIOS:
        print("\nO sistema atingiu o máximo absoluto de 15 funcionários.")
        return

    print("\n" + "=" * 60)
    print("NOVO FUNCIONÁRIO")
    print("=" * 60)

    nome = ler_texto("Nome: ")
    matricula = ler_matricula(funcionarios)
    telefone = ler_telefone()

    print("\nData de nascimento")
    dia, mes, ano = ler_data_nascimento()

    sexo = ler_sexo()
    salario = ler_float("Salário-base: R$ ", 0)

    print("\nEndereço")
    logradouro = ler_texto("Logradouro: ")
    numero_endereco = ler_texto("Número do endereço: ")
    complemento = input("Complemento (opcional): ").strip()

    carga_horaria = ler_float("Carga horária mensal: ", 1)
    turno_trabalho = ler_turno()
    cpf = ler_cpf(funcionarios)
    cargo = ler_texto("Cargo: ")

    funcionario = [
        nome,
        matricula,
        telefone,
        dia,
        mes,
        ano,
        sexo,
        salario,
        logradouro,
        numero_endereco,
        complemento,
        carga_horaria,
        turno_trabalho,
        cpf,
        cargo,
    ]

    funcionarios.append(funcionario)

    print("\nFuncionário cadastrado com sucesso!")
    print(f"Funcionários cadastrados: {len(funcionarios)}/{limite}")


# ------------------------------------------------------------
# OPÇÃO 2 - GERAR LISTA DE FUNCIONÁRIOS
# ------------------------------------------------------------

def gerar_lista_funcionarios(funcionarios):

    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n" + "=" * 74)
    print("LISTA DE FUNCIONÁRIOS")
    print("=" * 74)
    print(f"Total cadastrado: {len(funcionarios)} funcionário(s)")

    for numero, funcionario in enumerate(funcionarios, start=1):
        try:
            salario = funcionario[SALARIO]
            turno = funcionario[TURNO_TRABALHO]
            carga_horaria = funcionario[CARGA_HORARIA]

            acrescimos = CMC_Acrescimos(salario, turno)
            descontos = CMC_Descontos(salario)
            salario_liquido = CMC_Sal_Liquido(
                salario,
                acrescimos,
                descontos,
            )
            valor_hora = CMC_Valor_Hora(
                salario,
                carga_horaria,
            )

            print("\n" + "-" * 74)
            print(f"FUNCIONÁRIO {numero}")
            print("-" * 74)

            print("Nome:", funcionario[NOME])
            print("Matrícula:", funcionario[MATRICULA])
            print("Telefone:", funcionario[TELEFONE])

            print(
                "Nascimento:",
                f"{funcionario[DIA]:02d}/"
                f"{funcionario[MES]:02d}/"
                f"{funcionario[ANO]}",
            )

            print("Sexo:", funcionario[SEXO])
            print("CPF:", funcionario[CPF])
            print("Cargo:", funcionario[CARGO])
            print("Turno:", funcionario[TURNO_TRABALHO])
            print("Carga horária mensal:", funcionario[CARGA_HORARIA], "horas")

            print(
                "Endereço:",
                funcionario[LOGRADOURO],
                ",",
                funcionario[NUMERO_ENDERECO],
            )

            if funcionario[COMPLEMENTO]:
                print("Complemento:", funcionario[COMPLEMENTO])
            else:
                print("Complemento: não informado")

            print("\nCálculos")
            print("Salário-base: R$ %.2f" % salario)
            print("Acréscimos: R$ %.2f" % acrescimos)
            print("Descontos: R$ %.2f" % descontos)
            print("Salário líquido: R$ %.2f" % salario_liquido)
            print("Valor da hora: R$ %.2f" % valor_hora)

        except (IndexError, TypeError, ValueError, ZeroDivisionError) as erro:
            print("\nNão foi possível exibir completamente este registro.")
            print("Motivo:", erro)
            print("O programa continuará listando os demais funcionários.")


# ------------------------------------------------------------
# OPÇÃO 3 - LISTAR ANIVERSARIANTES DO MÊS
# ------------------------------------------------------------

def listar_aniversariantes_mes(funcionarios):
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    mes_consulta = ler_inteiro(
        "\nDigite o mês que deseja consultar [1 a 12]: ",
        1,
        12,
    )

    aniversariantes = []

    for funcionario in funcionarios:
        try:
            if funcionario[MES] == mes_consulta:
                aniversariantes.append(funcionario)

        except (IndexError, TypeError):
            continue

    print("\n" + "=" * 60)
    print(f"ANIVERSARIANTES DO MÊS {mes_consulta:02d}")
    print("=" * 60)

    if not aniversariantes:
        print("Nenhum aniversariante encontrado nesse mês.")
        return

    aniversariantes.sort(key=lambda funcionario: funcionario[DIA])

    for funcionario in aniversariantes:
        print(
            f"{funcionario[DIA]:02d}/{funcionario[MES]:02d} - "
            f"{funcionario[NOME]} - "
            f"Matrícula: {funcionario[MATRICULA]}"
        )


# ------------------------------------------------------------
# OPÇÃO 5 - EDITAR FUNCIONÁRIO
# ------------------------------------------------------------

def editar_funcionario(funcionarios):
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n" + "=" * 60)
    print("EDITAR FUNCIONÁRIO")
    print("=" * 60)

    matricula_busca = input(
        "Digite a matrícula do funcionário que deseja editar: "
    ).strip()

    indice = localizar_funcionario_por_matricula(
        funcionarios,
        matricula_busca,
    )

    if indice == -1:
        print("\nFuncionário não encontrado.")
        return

    funcionario = funcionarios[indice]

    print("\nFuncionário encontrado:")
    exibir_dados_resumidos(funcionario)

    while True:
        print("\n" + "-" * 60)
        print("QUAL DADO DESEJA ALTERAR?")
        print("-" * 60)
        print("[1] Nome")
        print("[2] Matrícula")
        print("[3] Telefone")
        print("[4] Data de nascimento")
        print("[5] Sexo")
        print("[6] Salário")
        print("[7] Logradouro")
        print("[8] Número do endereço")
        print("[9] Complemento")
        print("[10] Carga horária")
        print("[11] Turno de trabalho")
        print("[12] CPF")
        print("[13] Cargo")
        print("[14] Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            funcionario[NOME] = ler_texto("Novo nome: ")
            print("\nDados atualizados com sucesso.")

        elif opcao == "2":
            funcionario[MATRICULA] = ler_matricula(
                funcionarios,
                indice_ignorado=indice,
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "3":
            funcionario[TELEFONE] = ler_telefone()
            print("\nDados atualizados com sucesso.")

        elif opcao == "4":
            print("\nNova data de nascimento")
            dia, mes, ano = ler_data_nascimento()
            funcionario[DIA] = dia
            funcionario[MES] = mes
            funcionario[ANO] = ano
            print("\nDados atualizados com sucesso.")

        elif opcao == "5":
            funcionario[SEXO] = ler_sexo()
            print("\nDados atualizados com sucesso.")

        elif opcao == "6":
            funcionario[SALARIO] = ler_float(
                "Novo salário-base: R$ ",
                0,
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "7":
            funcionario[LOGRADOURO] = ler_texto(
                "Novo logradouro: "
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "8":
            funcionario[NUMERO_ENDERECO] = ler_texto(
                "Novo número do endereço: "
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "9":
            funcionario[COMPLEMENTO] = input(
                "Novo complemento (pode ficar vazio): "
            ).strip()
            print("\nDados atualizados com sucesso.")

        elif opcao == "10":
            funcionario[CARGA_HORARIA] = ler_float(
                "Nova carga horária mensal: ",
                1,
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "11":
            funcionario[TURNO_TRABALHO] = ler_turno()
            print("\nDados atualizados com sucesso.")

        elif opcao == "12":
            funcionario[CPF] = ler_cpf(
                funcionarios,
                indice_ignorado=indice,
            )
            print("\nDados atualizados com sucesso.")

        elif opcao == "13":
            funcionario[CARGO] = ler_texto("Novo cargo: ")
            print("\nDados atualizados com sucesso.")

        elif opcao == "14":
            print("\nRetornando ao menu principal.")
            break

        else:
            print("\nOpção inválida. Digite um número de 1 a 14.")


# ------------------------------------------------------------
# OPÇÃO 6 - EXCLUIR FUNCIONÁRIO
# ------------------------------------------------------------

def excluir_funcionario(funcionarios):
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n" + "=" * 60)
    print("EXCLUIR FUNCIONÁRIO")
    print("=" * 60)

    matricula_busca = input(
        "Digite a matrícula do funcionário que deseja excluir: "
    ).strip()

    indice = localizar_funcionario_por_matricula(
        funcionarios,
        matricula_busca,
    )

    if indice == -1:
        print("\nFuncionário não encontrado.")
        return

    funcionario = funcionarios[indice]

    print("\nFuncionário encontrado:")
    exibir_dados_resumidos(funcionario)

    confirmacao = ler_confirmacao(
        "\nDeseja realmente excluir este funcionário? [S/N]: "
    )

    if confirmacao == "S":
        funcionarios.remove(funcionario)
        print("\nFuncionário excluído com sucesso.")
    else:
        print("\nExclusão cancelada.")


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------

def mostrar_menu(funcionarios, limite):
    print("\n" + "=" * 60)
    print("SISTEMA DE CADASTRO SIMPLES - ACADEMIA")
    print("=" * 60)
    print(f"Funcionários cadastrados: {len(funcionarios)}/{limite}")
    print("[1] Incluir Novo Funcionário")
    print("[2] Gerar Lista de Funcionários")
    print("[3] Listar Aniversariantes do Mês")
    print("[4] Terminar o Programa")
    print("-" * 60)
    print("FUNCIONALIDADES ADICIONAIS")
    print("[5] Editar Funcionário")
    print("[6] Excluir Funcionário")
    print("=" * 60)


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():
    funcionarios = []

    print("=" * 60)
    print("CADASTRO DE FUNCIONÁRIOS DE UMA ACADEMIA")
    print("=" * 60)
    print(f"O sistema aceita no máximo {MAX_FUNCIONARIOS} funcionários.")

    limite = ler_inteiro(
        f"Defina o limite de funcionários desta execução [1-{MAX_FUNCIONARIOS}]: ",
        1,
        MAX_FUNCIONARIOS,
    )

    opcao = ""

    try:
        while opcao != "4":
            mostrar_menu(funcionarios, limite)
            opcao = input("Escolha uma opção: ").strip()

            try:
                if opcao == "1":
                    incluir_novo_funcionario(funcionarios, limite)

                elif opcao == "2":
                    gerar_lista_funcionarios(funcionarios)

                elif opcao == "3":
                    listar_aniversariantes_mes(funcionarios)

                elif opcao == "4":
                    print("\nPrograma encerrado com sucesso.")

                elif opcao == "5":
                    editar_funcionario(funcionarios)

                elif opcao == "6":
                    excluir_funcionario(funcionarios)

                else:
                    print("\nOpção inválida. Digite apenas 1, 2, 3, 4, 5 ou 6.")

            except (ValueError, TypeError, IndexError, ZeroDivisionError) as erro:
                print("\nOcorreu um erro durante a operação.")
                print("Motivo:", erro)
                print("O programa continuará em execução.")

    except (KeyboardInterrupt, EOFError):
        print("\n\nEntrada interrompida pelo usuário.")
        print("Programa encerrado sem falha inesperada.")


if __name__ == "__main__":
    main()
