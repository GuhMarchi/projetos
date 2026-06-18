alunos = {}
cursos = {}
matriculas = []

def cadastrar_aluno(idAluno, nome, email, cpf, dt_nascimento, telefone):
    alunos[idAluno] ={
        'nome':nome,
        'email':email,
        'cpf': cpf,
        'dt_nascimento':dt_nascimento,
        'telefone': telefone
    }
    print(f"Alunos {nome} Cadastrado com sucesso!")

def cadastrar_curso(idCurso, nome_curso, descricao, carga_horaria, instrutor):
    cursos[idCurso] = {
        'nome_curso': nome_curso,
        'descricao': descricao,
        'carga_horaria': carga_horaria,
        'instrutor': instrutor
    }
    print(f"Curso {nome_curso} Cadastrado com sucesso!")

def realizar_matricula(idAluno, idCurso, dt_matricula, status):
    if idAluno not in alunos:
        print("Aluno não encontrado!")
        return
    if idCurso not in cursos:
        print("Curso não encontrado!")
        return
    
    matriculas.append({
        'idAluno': idAluno,
        'idCurso': idCurso,
        'dt_matricula': dt_matricula,
        'status': status
    })
    print(f"Matrícula realizada: {alunos[idAluno]['nome']} -> {cursos[idCurso]['nome_curso']}")
    
def listar_alunos_por_curso(idCurso):
    if idCurso not in cursos:
       print("Curso não encontrado!")
       return
    print(f"Alunos matriculados em {cursos[idCurso]['nome_curso']}:")
    for m in matriculas:
        if m['idCurso'] == idCurso:
             print(f"  - {alunos[m['idAluno']]['nome']}")
        
        
cadastrar_aluno(1, 'Ana Silva', 'ana@email.com', '123.456.789-00', '2000-01-01', '16999999999')
cadastrar_aluno(2, 'Beto Souza', 'beto@email.com', '987.654.321-00', '1999-05-10', '16988888888')

cadastrar_curso(101, 'Python Basico', 'Introducao ao Python', 40, 'Prof. Heber')
cadastrar_curso(102, 'Banco de Dados', 'Introducao ao SQL', 60, 'Prof. Heber')

realizar_matricula(1, 101, '2025-01-01', 'ativo')
realizar_matricula(2, 102, '2025-01-02', 'ativo')

listar_alunos_por_curso(101)
listar_alunos_por_curso(102)
cadastrar_aluno(3, 'Carlos Pereira', 'carlos@email.com', '456.789.123-00', '2000-03-15', '16977777777')
