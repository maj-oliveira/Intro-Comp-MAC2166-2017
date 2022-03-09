"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Matheus Jose Oliveira dos Santos
  NUSP : 10335826
  Turma: 9
  Prof.: Denis Maua

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""
# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()
    
    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols   = int(input('Número de colunas do tabuleiro: '))
    x0      = int(input('Posição x inicial da cobrinha : '))
    y0      = int(input('Posição y inicial da cobrinha : '))
    t       = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")
        
    else:
        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1: 
            d = d * 10 + 2
            i = i + 1
        
        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
            
            # lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))
            
            if direcao != 5:
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

    print()        
    print("Tchau!")
    

# ======================================================================

def primdig(n):
    """Devolve o primeiro digito de um numero.
    """
    
    primeirodig=n//10**(num_digitos(n)-1);
    
    return primeirodig;

# ======================================================================

def num_digitos(n):
    """ (int) -> int

    Devolve o número de dígitos de um número.

    ENTRADA
    - n: número a ser verificado 

    """
    
    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    cont=0;
    while n>=1:
        n=n/10;
        cont+=1;
    
    return cont;
 
# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrário.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    
    """
    
    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    estaocupado = False; #var que indica se a cobra esta em tal posicao
    xaux = x0; #aux e abreviacao para auxiliar
    yaux = y0;
    cont = num_digitos(d);

    while cont>=0:
        cont-=1;
        daux=(d%10)*10;
        
        if(x==xaux and y==yaux):
            estaocupado = True;

        if(primdig(daux) == 1):
            xaux+=1;
        elif(primdig(daux) == 2):
            xaux-=1;
        elif(primdig(daux) == 3):
            yaux+=1;
        elif(primdig(daux) == 4):
            yaux-=1;

        #Retira o ultimo digito
        d=d//10;
        
    return estaocupado;


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
         
    """

    # Escreva sua função a seguir
    
    print();
    jy=0; #posicao y, linha
    
    while jy<nlinhas+2:
        ix=0; #posicao x, coluna
        if(jy==0 or jy==nlinhas+1):
            while ix<ncols+2:
                print("#", end="");#parede 
                ix+=1;
            print();
        else:
            print("#",end=""); #parede 
            ix+=1;
            while ix<ncols+1:
                if not pos_ocupada(nlinhas,ncols,ix-1,jy-1,x0,y0,d):
                    print(".",end="");
                else:
                    if(ix-1==x0 and jy-1==y0): #cabeca da cobra
                        print("C", end="");
                    else: 
                        print("*",end=""); #corpo da cobra
                ix+=1;
            print("#",end=""); #parede 
            print();
        
        jy+=1;
        

    print();
    #caso debug == true: mostrar vars;
    if debug:
        print("d =",d);
        print("x0 =",x0);
        print("y0 =",y0);
        print();

# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direção dada.    
    A função devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento é impossível (pois a cobra vai colidir consigo mesma ou
    com a parede), então a função devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃO COM SI MESMA" ou "COLISÃO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: número de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequência de deslocamentos que levam a posição da cauda da cobra
         até a cabeça; o dígito menos significativo é a direção na cabeça
    - direcao: direção na qual a cabeça deve ser movida
    
    """

    # Escreva sua função a seguir e corrija o valor devolvido no return
    
    coli = False;
    #Qual numero foi apertado
    if direcao == 1:
        if (x0-1)<0:
            print("\nCOLISÃO COM A PAREDE");
            coli=True;
        elif pos_ocupada(nlinhas,ncols,x0-1,y0,x0,y0,d):
            print("\nCOLISÃO COM SI MESMA");
            coli=True;
        else:
            x0-=1;
    elif direcao == 2:
        if (x0+2)>ncols:
            print("\nCOLISÃO COM A PAREDE");
            coli=True;
        elif pos_ocupada(nlinhas,ncols,x0+1,y0,x0,y0,d):
            print("\nCOLISÃO COM SI MESMA");
            coli=True;
        else:
            x0+=1;
    elif direcao == 3:
        if (y0-1)<0:
            print("\nCOLISÃO COM A PAREDE");
            coli=True;
        elif pos_ocupada(nlinhas,ncols,x0,y0-1,x0,y0,d):
            print("\nCOLISÃO COM SI MESMA");
            coli=True;
        else:
            y0-=1;
    elif direcao == 4:
        if (y0+2)>nlinhas:
            print("\nCOLISÃO COM A PAREDE");
            coli=True;
        elif pos_ocupada(nlinhas,ncols,x0,y0+1,x0,y0,d):
            print("\nCOLISÃO COM SI MESMA");
            coli=True;
        else:
            y0+=1;

    #atualiza var d

    if not coli:
        d=d*10+direcao;
        #Retira o primeiro digito de d
        d=d-primdig(d)*10**(num_digitos(d)-1);
    
    return x0, y0, d;

# ======================================================================

debug = False; #colocar True para exibir variaveis para debug

#Iniciar programa
main();

# ======================================================================
#FIM
