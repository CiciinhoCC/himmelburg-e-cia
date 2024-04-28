import numpy as np
import copy

def sum_lista(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

def simplificar(n,m):
    while min(n,m) > 6:
        n -= 1
        m -= 1

    return n,m

def print_stats(stats,inm = False):
    stats_str = ''
    stat_types = ['atk','blk','esq']
    for ind, i in enumerate(stats):
        if i != 0:
            stats_str += f'{i} {stat_types[ind]}{"-I" if inm else ""} '
    return stats_str
        
class Ataque:
    def __init__(self, nome, stats, stats_i, rolagem = 0):
        self.nome = nome
        self.stats = stats
        self.stats_i = stats_i
        self.rolagem = rolagem

    def __str__(self):
        return f"{self.nome} - {print_stats(self.stats)} {print_stats(self.stats_i,True)}"

class Arma(Ataque):
    def __init__(self,nome,stats, stats_i, ataques, rolagem = 0):
        super().__init__(nome, stats, stats_i)
        self.ataques = [Ataque(f"ataque ({self.nome})", self.stats,self.stats_i)]+copy.deepcopy(ataques)
        self.rolagem = rolagem

        self.imb = 0

    #Arma(self.nome,self.stats,self.stats_i,self.ataques,self.rolagem)
    def imbue(self,imbue):
        imbutido = copy.deepcopy(self)
        imbutido.imb = imbue
        for i in imbutido.ataques:
            i.stats = np.add(i.stats,imbutido.imb.stats)
            i.stats_i = np.add(i.stats_i,imbutido.imb.stats_i)
        return imbutido

    def __str__(self):
        ataques = ''
        rolagem = ['força', 'resistência', 'agilidade','percepção','inteligência'][self.rolagem]
        for i in self.ataques:
            ataques += f'{str(i)} \n'
        return f'{self.nome}: \n rolagem: {rolagem} \n {ataques}'

class ArteEMagia(Ataque):
    def __init__(self,nome,stats, stats_i, ataques, rolagem = 0):
        super().__init__(nome, stats, stats_i)

        self.rolagem = rolagem
        self.ataques = copy.deepcopy(ataques)


        for i in self.ataques:
            i.stats = np.add(i.stats,self.stats)
            i.stats_i = np.add(i.stats_i,self.stats_i)

        self.imb = 0

    def add(self, ataque):
        adicionado = copy.deepcopy(self)
        for i in ataque:
            i.stats = np.add(i.stats,adicionado.stats)
            i.stats_i = np.add(i.stats_i,adicionado.stats_i)
        adicionado.ataques += ataque
        return adicionado

    def imbue(self,imbue):
        imbutido = copy.deepcopy(self)
        imbutido.imb = copy.deepcopy(imbue)
        for i in imbutido.ataques:
            i.stats = np.add(i.stats,imbutido.imb.stats)
            i.stats_i = np.add(i.stats_i,imbutido.imb.stats_i)
        return imbutido

    def __str__(self):
        stats_str = f"{print_stats(self.stats)} {print_stats(self.stats_i,True)}"
        
        rolagem = ['força', 'resistência', 'agilidade','percepção','inteligência'][self.rolagem]

        ataques = ''
        for i in self.ataques:
            ataques += f'{str(i)} \n'
        return f'{self.nome}: \n {stats_str} \n rolagem: {rolagem} \n {ataques}'
    
class Armadura(Ataque):
    def __init__(self,nome,stats, stats_i, vida = 0):
        super().__init__(nome, stats, stats_i)
        self.vida = vida

    def __str__(self):
            stats_str = f"{print_stats(self.stats)} {print_stats(self.stats_i,True)}"


            return f"{self.nome} - {stats_str} {self.vida} vida"

class Personagem:
    def __init__(self, nome, stats, level, defesa, armas, artes, magias, armadura):
        self.nome = nome
        self.stats = stats
        self.buff = [0,0,0]
        self.level = level
        self.armadura = armadura

        self.armadura_stats = {
            'stats': [0,0,0],
            'stats_i': [0,0,0],
            'vida': 0
        }
        for i in self.armadura:
            if i != 0:
                self.armadura_stats['stats']=np.add(i.stats, self.armadura_stats['stats'])
                self.armadura_stats['stats_i']=np.add(i.stats_i, self.armadura_stats['stats_i'])
                self.armadura_stats['vida']= i.vida + self.armadura_stats['vida']
        self.vida = self.stats[1] * (2+level+defesa)


        self.armas = armas
        self.artes = artes
        self.magias = magias
        self.arma_arte_magia = self.armas + self.artes + self.magias

        self.ataques = []
        self.ataques.append(Ataque('sem arma',[0,2,2],[0,0,0]))
        for i in self.arma_arte_magia:
            for j in i.ataques:
                if f' ({i.nome})' not in j.nome: j.nome += f' ({i.nome})'
                if i.imb != 0: 
                    if f' ({i.imb.nome})' not in j.nome: j.nome += f' (imbue: {i.imb.nome})'
                if j.rolagem == 0: j.rolagem = i.rolagem
                self.ataques.append(j)

    def buffar(self,stats):
        self_buff = self
        self_buff.buff = stats
        return self_buff
    
    def get_ataque(self):
        print(f'Stats: {self.get_stats()}')
        if self.buff != [0,0,0]: print(f'Buffs: {self.get_stats_buff()}')
        armadura, armadura_i = self.get_armadura()
        print(f'Armadura: {armadura} {armadura_i}')
        for ind,i in enumerate(self.ataques):
            print(f'{ind} - {str(i)}')
    
        inp = input(">> selecione um ataque: ")
        while True:
            if self.ataques[int(inp)]:
                break
            inp = input(">> selecione um ataque: ")
        return self.ataques[int(inp)]
    
    def atacar(self, player):
        print(f'------------ \n Como {self.nome} vai atacar {player.nome}? \n ------------')
        armadura_vida = self.armadura_stats['vida']
        print(f'{self.nome}: {self.vida} ({self.vida + armadura_vida}) vida')
        armadura_vida = player.armadura_stats['vida']
        print(f'{player.nome}: {player.vida} ({player.vida + armadura_vida}) vida')
        golpe = self.get_ataque()

        ataque = golpe.stats[0] + self.armadura_stats['stats'][0]
        if golpe.rolagem == 3:
            ataque += self.stats[3]
        elif golpe.rolagem in [1,2] and self.stats[golpe.rolagem] > self.stats[0]:
            ataque += self.stats[golpe.rolagem]
        else:
            ataque += self.stats[0]
        ataque += self.buff[0]

        dano_float = (ataque + self.level)/3
        dano = int(np.round(dano_float)) 

        print(f'------------ \n Como {player.nome} se defenderá de {ataque} de ataque? \n ------------')
        block = player.get_ataque()
        
        bloqueio = block.stats[1] + player.stats[1] + golpe.stats_i[1] + player.buff[1] + player.armadura_stats['stats'][1] + self.armadura_stats['stats_i'][1]
        esquiva = block.stats[2] + player.stats[2] + golpe.stats_i[2] + player.buff[2] + player.armadura_stats['stats'][2] + self.armadura_stats['stats_i'][2]
        
        if bloqueio >= esquiva:
            defesa = bloqueio
            defesa_tipo = "bloqueio"
        else:
            defesa = esquiva
            defesa_tipo = "esquiva"

        roll_ataque, roll_defesa = simplificar(ataque,defesa)
        
        if ataque <=0:
            print(f'{self.nome} perde')
        elif defesa <=0:
            print(f'{player.nome} perde, {self.get_dados(dano)} ({dano}) de dano')
        else:
            print(f'{defesa} de {defesa_tipo}')
            print(f'{self.nome} rola {self.get_dados(roll_ataque)} ({ataque}), {player.nome} rola {self.get_dados(roll_defesa)} ({defesa})')
            print (f'se {self.nome} ganhar, rola {self.get_dados(dano)} ({round(dano_float,1)}) de dano')
            win = input(f'>> Quem ganhou? "A" para {self.nome} (segundo ataque) ou "D" para {player.nome} (contra-ataque): ')
            if win == 'A':
                self.atacar(player)
            elif win == 'D':
                player.atacar(self)
            else:
                quit()

    def get_dados(self,valor):
        dados = ['','d4','d6','d8','d10','d12','d20']
        d20 = int(np.floor(valor/6))
        d_outros = valor % 6
        if d_outros == 0:
            return f'{d20}d20'
        elif d20 >= 1:
            return f'{d20}d20 + {dados[d_outros]}'
        else:
            return dados[d_outros]
        
    def get_stats_buff(self):
        return print_stats(self.buff)

    def get_stats(self):
        stat_type = ['frc','res','agi','prc','int']
        stats_str = ''
        for ind, i in enumerate(self.stats):
                if i != 0:
                    stats_str += f'{i} {stat_type[ind]} '
        return stats_str
    
    def get_armadura(self):      
        armadura_stats = print_stats(self.armadura_stats['stats'])
        armadura_stats_i = print_stats(self.armadura_stats['stats_i'])
        return (armadura_stats, armadura_stats_i)
    
    def __str__(self):
        stats_str = self.get_stats()
        armadura_stats, armadura_stats_i = self.get_armadura()
        armadura_vida = self.armadura_stats["vida"]
        
        armas = ''
        artes = ''
        magias = ''
        armadura = ''
        for i in self.armas:
            armas += f'{str(i)}'
        for i in self.artes:
            artes += f'{str(i)}'
        for i in self.magias:
            magias += f'{str(i)}'
        for i in self.armadura:
            armadura += f'{str(i)} \n' if i != 0 else ' '
        armadura += f'total: {armadura_stats}{armadura_stats_i}{armadura_vida} vida'

        return f'--{self.nome}-- \n level {self.level}, {self.vida}({self.vida + armadura_vida}) vida \n {stats_str} \n -armas- \n {armas} \n -artes marciais- \n {artes} \n -magias- \n {magias} \n -armadura- \n {armadura}'