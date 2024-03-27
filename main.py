import numpy as np
        
class Ataque:
    def __init__(self, nome, stats, stats_i):
        self.nome = nome
        self.stats = stats
        self.stats_i = stats_i
        self.rolagem = 0

    def __str__(self):
        stats_str = ''
        stat_types = ['atk','blk','esq','cat']
        for ind, i in enumerate(self.stats):
            if i != 0:
                stats_str += f'{i} {stat_types[ind]} '
        for ind, i in enumerate(self.stats_i):
            if i != 0:
                stats_str += f'{i} {stat_types[ind]}-I '


        return f"{self.nome} - {stats_str}"

class Arma(Ataque):
    def __init__(self,nome,stats, stats_i, ataques, rolagem):
        super().__init__(nome, stats, stats_i)
        self.ataques = list(Ataque("ataque", self.stats,self.stats_i)+ataques)
        self.rolagem = rolagem

    def __str__(self):
        ataques = ''
        rolagem = ['força', 'resistência', 'agilidade','percepção','inteligência'][self.rolagem]
        for i in self.ataques:
            ataques += f'{str(i)} \n'
        return f'{self.nome}: \n rolagem: {rolagem} \n {ataques}'

class ArteEMagia(Ataque):
    def __init__(self,nome,stats, stats_i, ataques, rolagem):
        super().__init__(nome, stats, stats_i)

        self.rolagem = rolagem
        self.ataques = ataques

        for i in self.ataques:
            i.stats = np.add(i.stats,self.stats)
            i.stats_i = np.add(i.stats_i,self.stats_i)

    def __str__(self):
        stats_str = ''
        stat_types = ['atk','blk','esq','cat']
        for ind, i in enumerate(self.stats):
            if i != 0:
                stats_str += f'{i} {stat_types[ind]} '
        for ind, i in enumerate(self.stats_i):
            if i != 0:
                stats_str += f'{i} {stat_types[ind]}-I '
        
        rolagem = ['força', 'resistência', 'agilidade','percepção','inteligência'][self.rolagem]

        ataques = ''
        for i in self.ataques:
            ataques += f'{str(i)} \n'
        return f'{self.nome}: \n {stats_str} \n rolagem: {rolagem} \n {ataques}'
    
class Armadura(Ataque):
    def __init__(self,nome,stats, stats_i, vida):
        super().__init__(nome, stats, stats_i)
        self.vida = vida

    def __str__(self):
            stats_str = ''
            stat_types = ['atk','blk','esq','cat']
            for ind, i in enumerate(self.stats):
                if i != 0:
                    stats_str += f'{i} {stat_types[ind]} '
            for ind, i in enumerate(self.stats_i):
                if i != 0:
                    stats_str += f'{i} {stat_types[ind]}-I '


            return f"{self.nome} - {stats_str}. {self.vida} vida"

class Personagem:
    def __init__(self, nome, stats, level, defesa, armas, artes, magias, armadura):
        self.nome = nome
        self.stats = stats
        self.level = level
        self.armadura = armadura
        self.armadura_stats = {
            'stats': 0,
            'stats_i': 0,
            'vida': 0
        }
        for i in self.armadura:
            if i != 0:
                self.armadura_stats['stats']=np.add(i.stats, self.armadura_stats['stats'])
                self.armadura_stats['stats_i']=np.add(i.stats_i, self.armadura_stats['stats_i'])
                self.armadura_stats['vida']= i.vida + self.armadura_stats['vida']
        self.vida = stats[1] * (2+level+defesa)

        self.armas = armas
        self.artes = artes
        self.magias = magias

        self.ataques = []
        self.ataques.append(Ataque('sem arma',[0,2,2,0],[0,0,0,0]))
        for i in self.armas:
            for j in i.ataques:
                j.nome += f" ({i.nome})"
                j.rolagem = i.rolagem
                self.ataques.append(j)
        for i in self.artes:
            for j in i.ataques:
                j.nome += f" ({i.nome})"
                j.rolagem = i.rolagem
                self.ataques.append(j)
        for i in self.magias:
            for j in i.ataques:
                j.nome += f" ({i.nome})"
                j.rolagem = i.rolagem
                self.ataques.append(j)
    
    def get_ataque(self):
        print(f'Stats: {self.get_stats()}')
        for ind,i in enumerate(self.ataques):
            print(f'{ind} - {str(i)}\n')
    
        inp = input(">> selecione um ataque: ")
        while True:
            if self.ataques[int(inp)]:
                break
            inp = input(">> selecione um ataque: ")
        return self.ataques[int(inp)]
    
    def atacar(self, player, dist, cat):
        print(f'------------ \n Como {self.nome} vai atacar {player.nome}? \n ------------')
        golpe = self.get_ataque()
        if cat and dist:
            ataque = golpe.stats[0] + max(self.stats[1:3])
        elif cat and not dist:
            ataque = golpe.stats[0] + max(self.stats[0:2])
        elif dist and not cat:
            ataque = golpe.stats[0] + self.stats[3]
        elif self.stats[golpe.rolagem] > self.stats[0]:
            ataque = golpe.stats[0] + self.stats[ataque.rolagem]
        else:
            ataque = golpe.stats[0] + self.stats[0]
        dano = int(np.round((ataque + self.level + self.armadura_stats['stats'][0])/3))
        print(f'------------ \n Como {player.nome} se defenderá de {ataque} de ataque? \n ------------')
        block = player.get_ataque()
        if player.stats[1] + block.stats[1] + golpe.stats_i[1] > player.stats[2] + block.stats[2] + golpe.stats_i[2]:
            defesa = block.stats[1] + player.stats[1] + golpe.stats_i[1]
        else:
            defesa = block.stats[2] + player.stats[2] + golpe.stats_i[2]
        if ataque <=0:
            print(f'{self.nome} perde')
        elif defesa <=0:
            print(f'{player.nome} perde, {self.get_dados(dano)} ({dano}) de dano')
        else:
            print(f'{defesa} de defesa')
            print(f'{self.nome} rola {self.get_dados(ataque)}, {player.nome} rola {self.get_dados(defesa)}')
            print (f'se {self.nome} ganhar, rola {self.get_dados(dano)} ({dano}) de dano')
            cat = input(f'>> se {player.nome} ganhar ele pode contra-atacar, digite "S" se ele vai: ')
            if cat == 'S':
                player.atacar(self, dist, True)
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

    def get_stats(self):
        stat_type = ['frc','res','agi','prc','int']
        stats_str = ''
        for ind, i in enumerate(self.stats):
                if i != 0:
                    stats_str += f'{i} {stat_type[ind]} '
        return stats_str
    
    def get_armadura(self):
        stat_types = ['atk','blk','esq','cat']            
        armadura_stats = '' 
        armadura_stats_i = ''            
        for ind, i in enumerate(self.armadura_stats['stats']):
                if i != 0:
                    armadura_stats += f'{i} {stat_types[ind]} '
        for ind, i in enumerate(self.armadura_stats['stats_i']):
                if i != 0:
                    armadura_stats_i += f'{i} {stat_types[ind]}-I '
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
        





# MAGIAS

## FEITIÇOS

rajada = Ataque('rajada', [3,2,0,2],[0,0,0,0])
explosao = Ataque('explosão', [3,2,0,0], [0,-10,0,0])

## ELEMENTOS

ar = ArteEMagia('ar',[-1,0,0,0],[0,-2,-1,0],[rajada,explosao],0)

# ARTES MARCIAIS

## TÉCNICAS

soco = Ataque('soco', [2,0,0,0], [0,0,0,0])
voadora = Ataque('voadora', [3,0,2,2],[0,0,0,0])

## ESTILOS

combate_basico = ArteEMagia('combate básico', [0,0,0,0],[0,0,0,0],[soco,voadora],0)

# ARMADURA

armadura_couro = Armadura('armadura de couro', [2,0,0,0], [0,0,0,0], 4)


# PERSONAGENS

osel = Personagem('osel',[4,3,3,2,3], 2, 0, [], [combate_basico], [ar], [0,armadura_couro,0,0])

osel.atacar(osel,False,False)
            
