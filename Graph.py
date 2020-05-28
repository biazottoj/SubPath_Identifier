#G(V,A)
#G[U,V]


#Cria um dicionário onde cada chave é uma aresta
#E o valor é um boolean (True ou False)
# que indica de a aresta foi visitada
def edgesVisiting(edges: list):
 visited = {}
 for edge in edges:
  visited[edge] = False
#visited{'0 1': False, '0 2': False}
 return visited

#Função que percorre as arestas
# procurando se para o vértice vertex
# há alguma aresta não visitada
def hasNext(vertex: str, edgesVisited: dict):
    #vertex = 1
    #edges = {'0 1' :False, '0 2': False}
    #e = '0 1'
    #O valor de "e" contem vertex?

#str in str
    next = None #== NULL
    #vertex = 1
    #0 1, 0 2, 1 2
    for e in edgesVisited.keys():
        if vertex in e and \
                edgesVisited[e] == False:
            next = e #'0 1'
            break
    return next

#Função que cria o circuito
# percorrendo as arestas
# ligadas ao vértices
def createCircuit(edges: dict, startingVertex: str, op: str):

    #Como para criar a lista de subcaminhos eu preciso chamar essa função várias vezes
    #Precisei colocar o parametro 'op', ele indica para que eu estou usando essa função

    #Se eu tiver usando para criar um circuito, ou seja, op == 'circuit',
    #ele chama a função para criar a lista de arestas

    #Se ele receber a op == 'subpath', ele utiliza as edges que estão vindo por parâmetro
    if (op == 'circuit'):
        # Cria o dicionário de visitas às arestas
        visitedEdges = edgesVisiting(edges)
    else:
        # Utiliza a que está vindo por parâmetro
        visitedEdges = edges

    #Recebe o vertice inicial por parâmetro
    currentVertex = startingVertex

    #Cria uma pilha onde serão inseridos
    # os vértices percorridos
    stack = []

    #e = {'0 1', 0 2, 1 2

    #0 -> 1 -> 2 -> 0
    #circuit = ['0', 2,

    #Cria um circuito onde os vértices serão inseridos
    circuit = []

    #Encontra uma aresta ligada ao vertice que
    # ainda não foi percorrida
    next = hasNext(currentVertex, visitedEdges)

    #visited = {'0 1': False, '1 2': False}
    #currrentVertex = 1
    #next = hasNext()
    #next = 0

    # Coloca o vértice inicial na pulha
    stack += [currentVertex]

    #Percorre os vértices buscando arestas não
    # percorridas enquanto houverem vértices na pilha
    #stack 0 1 2
    while len(stack) > 0:
        #Idem ao trecho anterior
        next = hasNext(currentVertex, visitedEdges)
        stack += [currentVertex]

        #Executa enquando o retorno da função hasNext()
        # for diferente de None
        #Se a função hasNext() retorna
        # None quer dizer que o vertice
        #Que foi passada como parâmetro
        # não possui nenhum aresta sem visita
        while next != None:

            #Indica que aresta foi visitada
            visitedEdges[next] = True

            #Coloca atribui o destino da aresta
            # como currentVertice
            #Com esse código, a aresta pode ser
            # fornecida com: u,v ou v,u

            #next = 0 1
            #next = 1 0
            # 1 2
            #currentVertex == 0

            if next[0] == currentVertex:
                currentVertex = next[2]
            else:
                currentVertex = next[0]

            #Insere o currentVertice na Pilha
            stack += [currentVertex]

            #Busca o próiximo destino
            next = hasNext(currentVertex, visitedEdges)

        #Remove o útlimo elemento da pilha
        stack.pop()

        #Adiciona o vértice removido ao circuito
        circuit += [currentVertex]

        #stack = 0 1 2
        #circut = 1


        #Atribui a currentVertice o próximo elemento da
        # pilha
        currentVertex = stack[len(stack) - 1]

        # current = 3
        #Remove o elemento inserido na Pilha
        stack.pop()

        # stack = 0 1 2

    #Retorna o circuito
    return circuit, visitedEdges

#NOVA FUNÇÃO
#Encontra uma aresta que ainda não foi visitada
def isEmpty(edges: dict):
    next = None

    #dict={k0:v0, k1:v1, ....}
    #list[K:v
    for edge, status in edges.items():
        if status == False:
            next = edge
            break
    return next

#NOVA FUNÇÃO
#Identifica os subciclo do grafo
def createSubpath(edges: list):

    #Inicia a lista de arestas
    visitedEdges = edgesVisiting(edges)

    #Busca a primeira aresta que ainda não foi visitada
    next = isEmpty(visitedEdges)

    #Inicia a variável que vai guardar os caminhos que existem no grafo
    listOfSubpath = []

    #Roda enquanto houver alguma aresta n
    while (next != None):

        #A função createCircuit foi editada para retornar 2 valores
        #O primeiro é o caminho identificado, que será guardado em 'subpath'
        #O segundo é a lista de arestas, por que eu preciso guardar um registro
        #de quais arestas já foram visitadas
        subpath, visitedEdges = createCircuit(visitedEdges, next[0],'subpath')

        #Concatena o subcaminho na lista de subcaminhos
        listOfSubpath += [subpath]

        #Encontra a próxima aresta que não foi visitada
        next = isEmpty(visitedEdges)

    #Retorna a lista de subpaths
    return listOfSubpath




