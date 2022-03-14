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

  Nome : Matheus Jose Oliveira dos Santos
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
from math import ceil
from cmath import sin, cos, sinh, cosh, tan, exp, log

def main():
    print('EP3 - Comportamento dinâmico do Método de Newton\n')
    arquivo_funcoes = input('Arquivo com as funções: ')

    try:
        f, fp = le_funcoes(arquivo_funcoes)
    except:
        print('\nOops! Não consegui ler as funções do arquivo especificado!')
        return

    arquivo_saida   = input('Arquivo de saída:       ')

    print('\nParâmetros da grade')
    x1 = float(input('x1: '))
    y1 = float(input('y1: '))
    x2 = float(input('x2: '))
    y2 = float(input('y2: '))
    N  = int(input('N : '))

    print('\nParâmetros para o Método de Newton')
    eps = float(input('eps:     '))
    maxiter = int(input('maxiter: '))

    print('\nParâmetros para coloração')
    ro   = float(input('ro:   '))
    alfa = float(input('alfa: '))

    print('\nCalculando imagem... ', end = '')
    I, R = faz_matriz(f, fp, x1, y1, x2, y2, N, eps, maxiter)
    s = calcula_sombras(I)
    C = determina_cores(I, R, ro)
    grava_imagem(I, C, s, alfa, arquivo_saida)
    print('pronto.')

def nova_cor():
    """Devolve uma cor no formato (r, g, b) com r, g, b inteiros em [0, 255]."""

    cores = [ 0xff0000, 0x00ff00, 0x0000ff, 0xffff00, 0x00ffff, 0xff00ff, 0xc0c0c0,
              0xf0f8ff, 0xfaebd7, 0x7fffd4, 0xf0ffff, 0xf5f5dc, 0xffe4c4, 0xffebcd,
              0x8a2be2, 0xa52a2a, 0xdeb887, 0x5f9ea0, 0x9acd32, 0x7fff00, 0xd2691e,
              0xff7f50, 0x6495ed, 0xfff8dc, 0xdc143c, 0x00008b, 0x008b8b, 0xf5f5f5,
              0xb8860b, 0xa9a9a9, 0x006400, 0xbdb76b, 0x8b008b, 0x556b2f, 0xff8c00,
              0x9932cc, 0x8b0000, 0xe9967a, 0x8fbc8f, 0x483d8b, 0x2f4f4f, 0x00ced1,
              0x9400d3, 0xff1493, 0x00bfff, 0x696969, 0x1e90ff, 0xb22222, 0xfffaf0,
              0x228b22, 0xdcdcdc, 0xf8f8ff, 0xffd700, 0xdaa520, 0x808080, 0x008000,
              0xadff2f, 0xf0fff0, 0xff69b4, 0xcd5c5c, 0x4b0082, 0xfffff0, 0xf0e68c,
              0xe6e6fa, 0xfff0f5, 0x7cfc00, 0xfffacd, 0xadd8e6, 0xf08080, 0xe0ffff,
              0xfafad2, 0xd3d3d3, 0x90ee90, 0xffb6c1, 0xffa07a, 0x20b2aa, 0x87cefa,
              0x778899, 0xb0c4de, 0xffffe0, 0x32cd32, 0xfaf0e6, 0x800000, 0x66cdaa,
              0x0000cd, 0xba55d3, 0x9370db, 0x3cb371, 0x7b68ee, 0x00fa9a, 0x48d1cc,
              0xc71585, 0x191970, 0xf5fffa, 0xffe4e1, 0xffe4b5, 0xffdead, 0x000080,
              0xfdf5e6, 0x808000, 0x6b8e23, 0xffa500, 0xff4500, 0xda70d6, 0xeee8aa,
              0x98fb98, 0xafeeee, 0xdb7093, 0xffefd5, 0xffdab9, 0xcd853f, 0xffc0cb,
              0xdda0dd, 0xb0e0e6, 0x800080, 0x663399, 0xbc8f8f, 0x4169e1, 0x8b4513,
              0xfa8072, 0xf4a460, 0x2e8b57, 0xfff5ee, 0xa0522d, 0x87ceeb, 0x6a5acd,
              0x708090, 0xfffafa, 0x00ff7f, 0x4682b4, 0xd2b48c, 0x008080, 0xd8bfd8,
              0xff6347, 0x40e0d0, 0xee82ee, 0xf5deb3, 0xffffff ]

    c = cores[nova_cor.atual % len(cores)]
    nova_cor.atual += 1
    return (c >> 16, (c >> 8) & 0xff, c & 0xff)

nova_cor.atual = 0


def le_funcoes(nome_arquivo):
    """Lê uma função e sua derivada do arquivo de nome especificado."""

    entrada = open(nome_arquivo, 'r')
    f_txt = entrada.readline().strip()
    fp_txt = entrada.readline().strip()
    entrada.close()

    f_in = eval('lambda x: ' + f_txt)
    fp_in = eval('lambda x: ' + fp_txt)

    def f(x):
        try:
            return f_in(x)
        except:
            return None

    def fp(x):
        try:
            return fp_in(x)
        except:
            return None

    return f, fp

# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================
def newton(f, fp, x, eps, maxiter):
    """Executa o método de Newton em f com ponto inicial x.

    ARGUMENTOS:

    - f, fp -- função e sua derivada.

    - x -- ponto inicial.

    - eps -- o algoritmo pára se abs(f(x)) < eps.

    - maxiter -- número máximo de iterações a executar.

    Caso ocorra convergência, devolve (k, x), sendo k o número de
    iterações completadas até a convergência e x a aproximação da
    raiz. Caso contrário, a função devolve (-1, 0), para indicar que
    falhou.

    """
    
    for k in range(maxiter):

        #Verifica se f ou fp retorna None...
        if f(x) is None or fp(x) is None:
            return -1,0;
        
        #Próximo de uma raíz...
        elif abs(f(x))<eps:
            return k,x;

        #Não próximo de uma raíz...
        elif abs(fp(x))<eps:
            return -1,0;

        #Alterando x...
        x = x - (f(x)/fp(x));

    return -1,0;

def faz_matriz(f, fp, x1, y1, x2, y2, N, eps, maxiter):
    """Constrói matrizes com resultado de `newton` para uma grade de pontos.

    ARGUMENTOS:

    - fp, fp -- função e sua derivada.

    - x1, y1 -- coordenadas do canto esquerdo inferior do retângulo
      dentro do qual a grade será escolhida.

    - x2, y2 -- coordenadas do canto direito superior do retângulo
      dentro do qual a grade será escolhida.

    - N -- número de pontos na grade no lado menor do retângulo.

    - eps, maxiter -- parâmetros para função newton.

    A função devolve matrizes I, R de mesmo tamanho, de modo que o
    resultado do método de Newton executado no ponto que corresponde à
    entrada (i, j) das matrizes é (I[i][j], R[i][j]). Em outras
    palavras, a matriz I contém o número de iterações de que o método
    precisou e a matriz R a raiz encontrada.

    """
    delta = min(y2 - y1, x2 - x1) / N
    m = 1 + ceil((y2 - y1) / delta)
    n = 1 + ceil((x2 - x1) / delta)

    #Montando matrizes...
    I=[];
    R=[];
        
    for i in range(m):
        I.append([]);
        R.append([]);
        
        for j in range(n):
            (k,x) = newton(f,fp,complex(x1+j*delta,y2-i*delta),eps, maxiter);
            I[i].append(k);
            R[i].append(x);
            
    return I,R;

def determina_cores(I, R, ro):
    """Associa a cada entrada da matriz R uma cor com base em semelhança.

    ARGUMENTOS:

    - I, R -- matrizes devolvidas pela função faz_matriz.

    - ro -- proximidade requerida para entradas de mesma cor; veja
      enunciado.

    Esta função devolve uma nova matriz, de mesmo tamanho de R,
    contendo para cada entrada sua cor correspondente. Se para uma
    determinada entrada (i, j) temos I[i][j] = -1, então o método de
    Newton falhou; a cor associada à entrada na imagem final deve ser
    preto e a entrada correspondente na matriz C pode ser -1.

    Ao fazer a atribuição de cores, a idéia é que entradas com números
    próximos recebam uma mesma cor. O enunciado do EP descreve em
    linhas gerais como proceder para fazer a associação de cores. Esta
    função deve usar a função nova_cor para obter cores.

    """

    C=[];
    raizes=[]; #lista com raizes
    lcores=[]; #lista com cores
    ref = R[0][0]; #referência para comparação

    #Adicionando valores iniciais as listas abaixo...
    raizes.append(ref);
    lcores.append(nova_cor());
    
    #adiciona linhas a C...
    for i in range(len(R)):
        C.append([]);

    #preenche as linhas com "vazio", obs: não necessário, porém ajudou no debug
    for i in range(len(R)):
        for j in range(len(R[0])):
            C[i].append('vazio');

    #Verifica se é uma raiz conhecida na lista raizes para adicionar a cor (r,g,b)...
    for i in range(len(R)):
        for j in range(len(R[0])):
            vezes=len(raizes); #n vezes que k irá rodar
            flag=True; #var de passagem
            for k in range(vezes):
                #Caso o método de newton falhe, colocar cor preta...
                if I[i][j]==-1:
                    C[i][j]=(0,0,0);
                    flag=False;
                #Sucesso do método de newton...
                else:
                    if abs(R[i][j]-raizes[k]) <= ro:
                        C[i][j]=lcores[k];
                        flag=False;
                        break;
                    
            #Adiciona cor (r,g,b) a matriz C...
            if flag:
                coraux=nova_cor(); #var auxiliar
                raizes.append(R[i][j]);
                lcores.append(coraux);
                C[i][j]=coraux;
    
    return C;            


def calcula_sombras(I):
    """Devolve vetor de níveis de sombreamento da imagem.

    ARGUMENTOS:

    - I -- matriz de iterações devolvida pela função faz_matriz.

    Uma entrada da matriz I igual a k != -1 indica que o método de
    Newton executou k iterações antes de encontrar a aproximação da
    raiz. Seja N = max { I[i][j] : i, j }. Para 0 <= k <= N, seja a[k]
    o número de vezes que o número k ocorre em I e escreva S = a[0] +
    ... + A[N]. Esta função devolve uma lista s indexada de 0 a N
    (inclusive) tal que

    s[k] = 1 - (a[0] + ... + a[k - 1]) / S.

    Note que, se o método de Newton falhou para todos os pontos da
    grade, então N = -1 e a lista s é vazia.

    """
    #Encontrar maior valor da matriz I...
    M=-1;
    for i in range(len(I)):
        for j in range(len(I[0])):
            if I[i][j]>M:
                M=I[i][j];
       
    #se M=-1 retornar lista vazia
    if M==-1:
        return [];
    
    #determinando a lista "a"...
    a=[];
    for k in range(M):
        a.append(0);
        
    for i in range(len(I)):
        for j in range(len(I[0])):
            for k in range(M):
                if k == I[i][j]:
                    a[k]+=1;
                    break;
                
    #Somando a[k] para obter S...
    S=0            
    for k in range(M):
        S+=a[k];

    #Obtendo a lista "s"
    s=[];
    for k in range(M+1):
        sks = 0; #soma até a[k] sobre S
        for t in range(k):
            sks+=a[t];
        sks=sks/S;
        s.append(1-sks);

    return s;
    
def grava_imagem(I, C, s, alfa, nome_arquivo):
    """Grava uma imagem das bacias de atração em formato PPM.

    ARGUMENTOS:

    - I -- matriz de iterações devolvida pela função faz_matriz.

    - C -- matriz devolvida pela função determina_cores.

    - s -- lista de sombras devolvida por calcula_sombras.

    - alfa -- peso do sombreamento.

    - nome_arquivo -- nome do arquivo de saída.

    Se a cor c foi associada a uma entrada, a cor na imagem final é

    (1 - alfa + alfa * s[k]) * c.

    Assim, se alfa = 1, então o sombreamento tem peso total. Se alfa =
    0, então não fazemos sombreamento: cada bacia de atração recebe uma
    cor uniforme.

    """
    #Escrevendo estrutura do arquivo...
    arquivo = open(nome_arquivo+'.ppm','w');
    arquivo.write('P3\n');
    arquivo.write(str(len(C[0]))+' '+str(len(C))+'\n');
    arquivo.write('255\n');

    #Escrevendo os pixels...
    for i in range(len(C)):
        for j in range(len(C[0])):
    
            #Define peso "p"...
            p=1-alfa+alfa*s[I[i][j]];
            
            #Define r,g,b multiplicado pelo peso "p"...
            r,g,b = C[i][j];
            r=r*p;
            g=g*p;
            b=b*p;

            #Escrevendo os pixels...
            arquivo.write(str(r)+' '+str(g)+' '+str(b));
            if j == len(C[0])-1:
                arquivo.write('\n');
            else:
                arquivo.write(' ');
                  
    arquivo.close();


#main()
