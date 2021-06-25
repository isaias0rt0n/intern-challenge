# Date: 25-06-2021
# Code Author: Isaias 0rt0n

from teste import escola, cadernos_prova
from pessoa import Aluno
from prova import Caderno


# metodo para criar uma lista de objetos do tipo Aluno
def createListObjectsStudents(listStudents) -> list:
    lstStudents = []
    for i in range(len(listStudents)):  # percorre os elementos da lista e instancia um objeto do tipo Aluno
        student = Aluno(
            listStudents[i]['nome'],
            listStudents[i]['matricula'],
            listStudents[i]['proficiencia_mt'],
            listStudents[i]['proficiencia_pt']
        )
        lstStudents.append(student)  # adiciona a uma lista
    return lstStudents


# metodo para criar uma lista de objetos do tipo Caderno
def createListObjectsNotebooks(listNotebooks: list) -> list:
    lstNotebooks = []
    for i in range(len(listNotebooks)): # percorre os elementos da lista e instancia um objeto do tipo Caderno
        notebook = Caderno(
            listNotebooks[i]['disciplina'],
            listNotebooks[i]['codigo'],
            listNotebooks[i]['dificuldade']
        )
        lstNotebooks.append(notebook)   # adiciona a uma lista
    return lstNotebooks


# metodo para calcular nível de dificuldade mais próximo do aluno
def calculateLevel(code: float, lst_dificuldades: list) -> int:
    valor = {value: abs(value - code) for value in lst_dificuldades}    # calcula o desvio padrão de todos os valores da lista recebida
    return min(valor, key=valor.get)    # retorna o valor(nível de dificuldade) da menor diferença(mais próximo)


# metodo para buscar o objeto que atende ao nível de proeficiência do aluno
def searchNotebook(lst_Notebooks: list, level: int, discipline: str) -> object:
    for obj in lst_Notebooks:   # percorre os objetos da lista recebida
        if obj.dificuldade == str(level) and obj.disciplina == discipline:  # verifica qual disciplina atende ao nível
            return obj


# metodo para retornar uma lista de dicionarios contendo os alunos e seus respectivos cadernos
def selectNotebookToStudent(lstNotebooks: list, lstStudents: list) -> list:
    listNotebookToStudent = []

    for obj_i in lstStudents:   # percorre a lista de objetos do tipo Aluno
        difficulty_level = []
        for obj_j in lstNotebooks:  # percorre a lista de objetos do tipo Caderno
            difficulty_level.append(int(obj_j.dificuldade))  # adiciona na lista a dificuldade do caderno

        level_mt = calculateLevel(float(obj_i.proficiencia_mt), difficulty_level)  # calcular qual nível mais próximo da proeficiência(matematica)
        level_lt = calculateLevel(float(obj_i.proficiencia_pt), difficulty_level)

        obj_notebook_mt = searchNotebook(lstNotebooks, level_mt, 'matemática')  # busca e retorna o obj caderno de acordo com o nível de proeficiência
        obj_notebook_lp = searchNotebook(lstNotebooks, level_lt, 'portugues')

        # adiciona ao dicionario as instancias dos alunos e seus cadernos
        dictionary = ({
            'aluno': obj_i,
            'caderno_mt': obj_notebook_mt,
            'caderno_lp': obj_notebook_lp
        })

        listNotebookToStudent.append(dictionary)    # adiciona a uma lista os dicionários
    return listNotebookToStudent


if __name__ == '__main__':
    lstObjNotebooks = createListObjectsNotebooks(cadernos_prova)    # cria lista de objetos do tipo caderno
    lstObjStudents = createListObjectsStudents(escola['alunos'])    # cria lista de objetos do tipo Aluno

    # passa as lista para obter a lista de dicionarios contendo os alunos e os respectivos cadernos
    notebookToStudent = selectNotebookToStudent(lstObjNotebooks, lstObjStudents)
    print(notebookToStudent)

    # Teste programa
    for obj in notebookToStudent:
        print(obj['aluno'].nome, obj['aluno'].proficiencia_mt, obj['aluno'].proficiencia_pt, sep=' | ')
        print(obj['caderno_mt'].disciplina, obj['caderno_mt'].dificuldade, sep=' | ')
        print(obj['caderno_lp'].disciplina, obj['caderno_lp'].dificuldade, sep=' | ')
        print()
