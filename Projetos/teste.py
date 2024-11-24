caminho = '.'
errado = 'x'
solucao = '@'
parede = '#'
percorrido = '+'
piltover = '*'
rota = []


class maze ( object ):
    def __init__ (self):
        self.mapa = None
        self.entrada = None
        self.saida = None

    def data_entry(self):
        number = int(input())
        self.mapa = []
        for _ in range(number):
            self.mapa.append(input().split())

        entrada = [int(i) for i in input().split()] # ONDE COMEÇAMOS
        self.entrada = (entrada[0], entrada[1])

        for i, elem in enumerate( self.mapa ):
            for _ in range(len(elem)):
                if elem[_] == piltover:
                    self.saida = (i, _)
        
        if not self.entrada or not self.saida:
            raise ValueError ('O mapa não possui os dados para processarmos!')
        # data_entry()



    def solveMaze( self ):
        '''
            TENTAREMOS ENCONTRAR A SAIDA DO LABIRINTO, SE ENCONTRARMOS RETORNAREMOS TRUE, CASO NÃO RETORNAREMOS FALSE!!
        '''

        def portal(mapa):
            portal = {}
            pontos = ['.','*','#','+']

            for i, elem in enumerate(mapa):
                for _ in range(len(elem)):
                    if elem[_] not in pontos:
                        letra = elem[_]
                        if letra not in portal:
                            local = []
                            local.append([i, _])
                            portal[letra] = local
                        else:
                            local = []
                            for k in portal[letra]:
                                local.append(k)
                            local.append([i,_])
                            portal[letra] = local
            return portal


        def posicao(linha, coluna): # VERIFICANDO SE A POSICAO É VÁLIDA
            if linha >= len( self.mapa ) or coluna >= len( self.mapa[linha] ) or linha < 0 or coluna < 0:
                return False
            else:
                return True
        # posicao()


        def procurando_saida(linha, coluna):
            if self.mapa[linha][coluna] == piltover:
                '''CASO EM QUE ESTAMOS EM CIMA DE PILTOVER'''
                return True
            else:
                ''' VAMOS MARCAR O CAMINHO QUE PERCORRERMOS PARA FACILITAR A RESOLUÇÃO DO LABIRINTO
                    IREMOS SEGUIR UMA PRIORIDADE DE DIREÇÕES, NO CASO ESQUERDA, BAIXO, DIREITA, CIMA

                    COMO ISTO SERÁ UMA RECURSAO TEREMOS MARCADO O CAMINHO QUE JÁ FOI TESTADO!
                '''

                self.mapa[linha][coluna] = percorrido
                encontrou = False
                portais = portal( self.mapa )
                letras = []
                for chave, valor in portais.items():
                    letras.append(chave)

                if not encontrou and \
                    posicao(linha, coluna + 1) and \
                    (self.mapa[linha][coluna + 1] in (caminho, piltover) or \
                    self.mapa[linha][coluna + 1] in letras):
                    '''AINDA NAO ENCONTROU, MAS A POSICAO A DIREITA É UM CAMINHO OU A SAÍDA OU UM PORTAL'''
                    if self.mapa[linha][coluna + 1] in letras:
                        for a in portais[ self.mapa [linha][coluna + 1]]:
                            if a != [linha, coluna + 1]:
                                l = a[0]
                                c = a[1] + 1
                                if self.mapa[l][c] != parede and self.mapa[l][c] != percorrido:
                                    encontrou = procurando_saida(l, c)
                    else:
                        encontrou = procurando_saida(linha, coluna + 1)
                
                if not encontrou and \
                    posicao(linha - 1, coluna) and \
                    (self.mapa[linha - 1][coluna] in (caminho, piltover) or \
                    self.mapa[linha - 1][coluna] in letras):
                    '''AINDA NAO ENCONTROU, MAS A POSICAO A CIMA É UM CAMINHO OU A SAÍDA'''
                    if self.mapa[linha - 1][coluna] in letras:
                        for a in portais[ self.mapa [linha - 1][coluna]]:
                            if a != [linha - 1, coluna]:
                                l = a[0] -1
                                c = a[1]
                                if self.mapa[l][c] != parede and self.mapa[l][c] != percorrido:
                                    encontrou = procurando_saida(l, c)
                    else:
                        encontrou = procurando_saida(linha - 1, coluna)

                if not encontrou and \
                    posicao(linha, coluna - 1) and \
                    (self.mapa[linha][coluna - 1] in (caminho, piltover) or \
                    self.mapa[linha][coluna - 1] in letras):
                    '''AINDA NAO ENCONTROU, MAS A POSICAO A ESQUERDA É UM CAMINHO OU A SAÍDA'''
                    if self.mapa[linha][coluna - 1] in letras:
                        for a in portais[ self.mapa [linha][coluna - 1]]:
                            if a != [linha, coluna - 1]:
                                l = a[0]
                                c = a[1] - 1
                                if self.mapa[l][c] != parede and self.mapa[l][c] != percorrido:
                                    encontrou = procurando_saida(l, c)
                    else:
                        encontrou = procurando_saida(linha, coluna - 1)

                if not encontrou and \
                    posicao(linha + 1, coluna) and \
                    (self.mapa[linha + 1][coluna] in (caminho, piltover) or \
                    self.mapa[linha + 1][coluna] in letras):
                    '''AINDA NAO ENCONTROU, MAS A POSICAO A BAIXO É UM CAMINHO OU A SAÍDA'''
                    if self.mapa[linha + 1][coluna] in letras:
                        for a in portais[ self.mapa [linha + 1][coluna]]:
                            if a != [linha + 1, coluna]:
                                l = a[0] + 1
                                c = a[1]
                                if self.mapa[l][c] != parede and self.mapa[l][c] != percorrido:
                                    encontrou = procurando_saida(l, c)
                    else:
                        encontrou = procurando_saida(linha + 1, coluna)

                if encontrou:
                    self.mapa[linha][coluna] = solucao
                else:
                    self.mapa[linha][coluna] = errado

                return encontrou
            # procurando_saida()
            
        return procurando_saida(self.entrada[0], self.entrada[1])

l = maze()
l.data_entry()
if l.solveMaze() == True:
    print('Jayce conseguiu chegar em Piltover')
else:
    print('Jayce nao conseguiu chegar em Piltover')
