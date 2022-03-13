"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Matheus José Oliveira dos Santos
  NUSP : --------
  Turma: 9
  Prof.: Denis Maua

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
#
#   FUNÇÕES FORNECIDAS: NÃO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta é a função principal do seu programa. Ela contém os comandos que
    obtêm os parâmetros necessários para criação do jogo (número de linhas,
    colunas e cores), e executa o laço principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÇÃO NÃO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lê parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o número de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuração inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laço principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos válidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** Você destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento inválido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print ()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print ("Você destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaços vazios com novas gemas geradas aleatoriamente.

    As gemas são representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]


# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representação do tabuleiro e a preenche com
    espaços vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []
    #
    #print("***********************************")
    #print("*** Implemente a função criar() ***")
    #print("***********************************")
    #exit(0)

    #adiciona listas a matriz
    for i in range(num_linhas):
        matriz.append([]);

    #preenche as listas com espaços: " "
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[i].append(" ");
    #
    return matriz

def exibir (tabuleiro):
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''
    #
    #print("************************************")
    #print("*** Implemente a função exibir() ***")
    #print("************************************")

    #printar linha de números
    print("     ",end="");
    for k in range(len(tabuleiro[0])):
        print(k,end="");
        print(" ",end="");
    print();

    #printar linha de -
    print("   +",end="");
    for k in range(len(tabuleiro[0])*2 +1):
        print("-",end="");
    print("+");

    #printar tabuleiro
    for i in range(len(tabuleiro)): #linha
        print(" ",end="");
        print(i,end="");
        print(" |",end="");
        for j in range(len(tabuleiro[i])): #coluna
            print(" "+tabuleiro[i][j],end="");
        print(" |",end="");
        print();

    #printar linha de -
    print("   +",end="");
    for k in range(len(tabuleiro[0])*2 +1):
        print("-",end="");
    print("+");
    
def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posições (linha1, coluna1) e (linha2, coluna2) caso
    seja válida (isto é, gemas são adjacentes e geram cadeias), caso contrário
    não altera o tabuleiro.

    Retorna `True` se permutação é válida e `False` caso contrário.
    '''
    #
    #print("************************************")
    #print("*** Implemente a função trocar() ***")
    #print("************************************")

    formacadeia=False;
    #caso seja adjacente...
    #(Assumindo que o usuário digite apenas valores dentro da matriz tabuleiro)
    if ((coluna1+1 == coluna2 and linha1 == linha2) or
        (coluna1-1 == coluna2 and linha1 == linha2) or
        (coluna1 == coluna2 and linha1+1 == linha2) or
        (coluna1 == coluna2 and linha1-1 == linha2)):
        
        #fazer troca no tabuleiro
        letraaux=tabuleiro[linha2][coluna2];
        tabuleiro[linha2][coluna2]=tabuleiro[linha1][coluna1];
        tabuleiro[linha1][coluna1]=letraaux;
        #verificar se forma cadeias horizontais
        if not identificar_cadeias_horizontais(tabuleiro) == []:
            formacadeia=True;
            exibir(tabuleiro);
        #verificar se forma cadeias verticais
        if not identificar_cadeias_verticais(tabuleiro) == []:
            formacadeia=True;
        #Caso contrário voltar para a posição antes da troca
        if not formacadeia:
            letraaux=tabuleiro[linha2][coluna2];
            tabuleiro[linha2][coluna2]=tabuleiro[linha1][coluna1];
            tabuleiro[linha1][coluna1]=letraaux;
    
    #
    return formacadeia


def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaços (' ').

    Retorna número de gemas eliminadas.
    '''
    num_eliminados = 0
    #
    #print("***********************************************")
    #print("*** Implemente a função eliminar(tabuleiro) ***")
    #print("***********************************************")
    
    cadh = identificar_cadeias_horizontais(tabuleiro); #horizontal
    cadv = identificar_cadeias_verticais(tabuleiro); #vertical
    
    #lembrete: não alterar a ordem dos seguintes laços:
    for m in range(len(cadh)): #primeiro laço
        if(m<len(cadh)):
            num_eliminados += eliminar_cadeia(tabuleiro,cadh[m]);

    for n in range(len(cadv)): #segundo laço
        if(n<len(cadv)):
            num_eliminados += eliminar_cadeia(tabuleiro,cadv[n]);
    #
    return num_eliminados

def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o número da linha da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    #   
    #print("*************************************************************")
    #print("*** Implemente a função identificar_cadeias_horizontais() ***")
    #print("*************************************************************")

    for i in range(len(tabuleiro)): #verificar linha
        if(i<len(tabuleiro)):
            for j in range(len(tabuleiro[i])): # verificar coluna
                if(j<len(tabuleiro[i])):
                    letra=tabuleiro[i][j];
                    k=1; #contador
                    procurar=True;
                    while procurar:
                        if(j+k<len(tabuleiro[j])):
                            if (letra == tabuleiro[i][j+k]):
                                k+=1;
                            else:
                                procurar=False;
                        else:
                            procurar=False;
                    if(k>=3):
                        cadeias.append([i,j,i,j+k-1]);
                    j+=k;
    #
    return cadeias

def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o número da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o número da coluna das gemas da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia

    Não modifica o tabuleiro.
    '''
    cadeias = []
    #
    #print("***********************************************************")
    #print("*** Implemente a função identificar_cadeias_verticais() ***")
    #print("***********************************************************")
    for j in range(len(tabuleiro[0])): #verificar coluna
        if(j<len(tabuleiro[0])):
            for i in range(len(tabuleiro)): #verificar linha
                if(i<len(tabuleiro)):
                    letra=tabuleiro[i][j];
                    k=1; #contador
                    procurar=True;
                    while procurar:
                        if(i+k<len(tabuleiro)):
                            if(letra == tabuleiro[i+k][j]):
                                k+=1;
                            else:
                                procurar=False;
                        else:
                            procurar=False;
                    if(k>=3):
                        cadeias.append([i,j,i+k-1,j]);
                    i+=k;
    #
    return cadeias

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaço `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o número da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o número da coluna da gema mais à esquerda (menor) da cadeia
    - `linha_f`: o número da linha mais inferior (maior) da cadeia
    - `coluna_f`: o número da coluna da gema mais à direita (maior) da cadeia

    Retorna o número de gemas eliminadas.
    '''
    num_eliminados = 0
    #
    #print("*********************************************")
    #print("*** Implemente a função eliminar_cadeia() ***")
    #print("*********************************************")

    corretor=0; #evita contar o mesmo pto 2x
    if(cadeia[0]==cadeia[2]): #horizontal
        for j in range(cadeia[3]-cadeia[1]+1):
            tabuleiro[cadeia[0]][cadeia[1]+j]=" ";
        num_eliminados=cadeia[3]-cadeia[1]+1;
            
    elif(cadeia[1]==cadeia[3]): #vertical
        for i in range(cadeia[2]-cadeia[0]+1):
            if(tabuleiro[cadeia[0]+i][cadeia[1]] == " "):
                corretor-=1; #evita contar o mesmo pto 2x
            tabuleiro[cadeia[0]+i][cadeia[1]]=" ";
        num_eliminados=cadeia[2]-cadeia[0]+1+corretor;
    #
    return num_eliminados


def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaços vazios sem nenhuma gema acima.
    '''
    #
    #print("**************************************")
    #print("*** Implemente a função deslocar() ***")
    #print("**************************************")

    for j in range(len(tabuleiro[0])):
        deslocar_coluna(tabuleiro,j);

def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaços vazios.
    '''
    #
    #print("*******************************************")
    #print("*** Implemente a função desloca_linha() ***")
    #print("*******************************************")

    m=len(tabuleiro)-1;
    while m>=0:
        prvazio = True; #procura espaços vazios
        k=1;
        if(tabuleiro[m][i]==" " and (m-1)>=0):
            while prvazio:
                if(tabuleiro[m-k][i]==" " and (m-k)>=0):
                    k+=1;
                else:
                    prvazio=False;
            if (m-k>=0):
                tabuleiro[m][i]=tabuleiro[m-k][i];
                tabuleiro[m-k][i]=" ";
        m-=1;

def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos válidos, False caso contrário.
    '''
    #
    #print("********************************************************")
    #print("*** Implemente a função existem_movimentos_validos() ***")
    #print("********************************************************")
    existe=True;
    m,n = obter_dica(tabuleiro);
    if m == -1:
        existe=False;
    #
    return existe


def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posição (linha, coluna) de uma gema que faz parte de uma
    permutação válida.

    Se não houver permutação válida, retorne -1,-1.
    '''
    linha = -1
    coluna = -1
    #
    #print("****************************************")
    #print("*** Implemente a função obter_dica() ***")
    #print("****************************************")

    tabuleiroaux=[]; #tabuleiro auxiliar
    flag = True; #indicador de passagem

    #copia tabuleiro para tabuleiro auxiliar
    for i in range(len(tabuleiro)):
        tabuleiroaux.append([]);

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            tabuleiroaux[i].append(tabuleiro[i][j]);      
    teste=len(tabuleiroaux[0]);
    #verifica se existe algum movimento que possa ser feito e retorna coordenada dele
    for i in range(len(tabuleiroaux)):
        for j in range(len(tabuleiroaux[0])):
            if flag:
                #verificação horizontal
                if (j+1!=len(tabuleiroaux[0])) and trocar(i,j,i,j+1,tabuleiroaux):
                    linha=i;
                    coluna=j;
                    flag = False;
                elif (j-1!=-1) and trocar(i,j,i,j-1,tabuleiroaux):
                    linha=i;
                    coluna=j;
                    flag = False;
                #verificação vertical
                elif (i+1!=len(tabuleiroaux)) and trocar(i,j,i+1,j,tabuleiroaux):
                    linha=i;
                    coluna=j;
                    flag = False;
                elif (i-1!=-1) and trocar(i,j,i-1,j,tabuleiroaux):
                    linha=i;
                    coluna=j;
                    flag = False;

    #
    return linha, coluna

main()
