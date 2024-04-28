from classes import Ataque, Arma, ArteEMagia, Armadura, Personagem
# ARMAS
    
## GOLPES

arremesso_lanca = Ataque('arremesso',[3,0,0],[0,-2,-1],3)
empalar = Ataque('empalar',[4,0,0],[0,-2,0])
rajada_lanca = Ataque('rajada (armas)',[2,0,0],[0,-2,-2],3)
golpe_relampago = Ataque('golpe relâmpago',[4,0,2],[0,0,-2])
corte_voador = Ataque('corte voador',[3,0,0],[0,-1,-2],3)
salto_katana = Ataque('salto (armas)',[2,0,4],[0,0,0])
queima_roupa = Ataque('queima-roupa',[5,0,0],[0,-1,-1])
fuzilada = Ataque('fuzilada',[3,0,0],[0,-2,-10], 3)
redemoinho = Ataque('redemoinho',[2,2,0],[0,-1,-1])
avancada_grab = Ataque('avançada (grab)',[3,0,0],[0,-1,0])
avancada_golpe = Ataque('avançada (3 golpes)',[2,0,0],[0,1,0])
vendaval = Ataque('vendaval',[3,0,0],[0,-1,-1],3)
quebra_cranio_grab = Ataque('quebra-crânio (grab)',[3,0,0],[0,-1,0])
quebra_cranio_golpe = Ataque('quebra-crânio (2 golpes)',[4,0,0],[0,1,0])
arremesso_faca = Ataque('arremesso',[3,0,0], [0,-2,-2],3)
meia_luas = Ataque('meia luas',[4,0,0],[0,-2,-1])
redemoinho_montante = Ataque('redemoinho',[4,2,0],[0,-1,0])


guspir_acido = Ataque('guspir ácido',[4,1,0],[0,-2,0])
rabada = Ataque('rabada',[4,0,0],[0,-2,-10])

enraizar = Ataque('enraizar',[4,0,0],[0,-2,-10])
chicoteada = Ataque('chicoteada',[5,0,0],[0,-2,-1])

## ARMAS

lanca = Arma('lança', [3,3,0],[0,0,0],[arremesso_lanca,empalar,rajada_lanca],0)
katana = Arma('katana', [4,0,3],[0,0,0],[golpe_relampago,corte_voador,salto_katana],2)
pistola = Arma('pistola', [5,-10,0], [0,-3,-10],[queima_roupa,fuzilada],3)
espada = Arma('espada',[3,3,1],[0,0,0],[redemoinho,avancada_grab,avancada_golpe,corte_voador])
alabarda = Arma('alabarda',[3,3,1],[0,0,0],[empalar,vendaval,quebra_cranio_grab,quebra_cranio_golpe])
faca = Arma('faca',[2,0,4],[0,-1,0],[arremesso_faca],2)
garra = Arma('garra', [3,0,3],[0,0,-1],[corte_voador],2)
escudo = Arma('escudo',[2,4,0],[0,0,-1],[],1)
espada_dupla = Arma('espadas duplas',[3,0,2],[0,-1,0],[meia_luas,golpe_relampago],2)
montante = Arma('montante',[3,3,0],[0,-1,-1],[redemoinho_montante])

tubarao = Arma('tubarão',[4,0,0],[0,-10,-2],[guspir_acido,rabada])
arvore = Arma('árvore',[3,3,0],[0,0,0],[enraizar,chicoteada])

# MAGIAS

## FEITIÇOS

tiro = Ataque('tiro', [2,0,0],[0,0,0])
rajada = Ataque('rajada', [4,3,0],[0,0,0], 3)
rajada_melee = Ataque('rajada de perto', [4,3,0],[0,0,0])
explosao = Ataque('explosão', [3,2,0], [0,-10,0])
explosao_pos = Ataque('explosão posicionada', [2,2,0], [0,-10,0],3)
salto = Ataque('salto',[0,0,5],[0,0,0])

pilastra = Ataque('pilastra', [5,3,0],[0,-2,-2])
acorrentar = Ataque('acorrentar', [4,0,0],[0,1,1])

## ELEMENTOS

golpes_magia = [tiro,rajada,rajada_melee,explosao,salto]

golpes_redward = [pilastra,acorrentar]

agua = ArteEMagia('água',[0,-1,0],[0,-1,0],golpes_magia,0)
terra = ArteEMagia('terra',[2,0,0],[0,0,1],golpes_magia,0)
fogo = ArteEMagia('fogo',[1,0,0],[0,0,0],golpes_magia,0)
ar = ArteEMagia('ar',[-1,0,0],[0,-2,-1],golpes_magia,0)
raio = ArteEMagia('raio',[-1,0,0],[0,0,-2],golpes_magia,0)

magma = ArteEMagia('magma',[3,0,0],[0,0,1],golpes_magia,0)


# ARTES MARCIAIS

## TÉCNICAS

soco = Ataque('soco', [2,0,0], [0,0,0])
voadora = Ataque('voadora', [3,0,3],[0,0,-1])
estrondo = Ataque('estrondo', [3,2,0],[0,-10,0])
ofensiva_grab = Ataque('ofensiva (grab)', [3,0,0],[0,0,1])
ofensiva_golpe = Ataque('ofensiva (3 golpes)', [2,0,0],[0,1,0])
tiro = Ataque('tiro', [3,2,0],[0,-1,-1])


## ESTILOS

golpes_artes = [soco,voadora,estrondo]
golpes_artes_mestre = [ofensiva_grab,ofensiva_golpe,tiro]

punho_marinheiro = ArteEMagia('punho do marinheiro',[-1,0,0],[0,0,0],golpes_artes,2)
punho_marinheiro_c75 = ArteEMagia('punho do marinheiro',[1,0,1],[0,1,0],golpes_artes,2)

soco_ardente_c0 = ArteEMagia('soco ardente',[-1,0,0],[0,0,0],golpes_artes)
soco_ardente_c25 = ArteEMagia('soco ardente',[0,0,1],[0,0,0],golpes_artes)
soco_ardente_c50 = ArteEMagia('soco ardente',[0,-1,1],[0,0,-1],golpes_artes)
soco_ardente_c75 = ArteEMagia('soco ardente',[0,-1,2],[0,0,-1],golpes_artes)

combate_basico = ArteEMagia('combate básico', [0,0,0],[0,0,0],golpes_artes,0)
combate_basicao = ArteEMagia('combate basicão', [0,0,0],[0,0,0],[soco],0)

canela_aco = ArteEMagia('canela de aço',[1,0,-1],[0,0,0],golpes_artes)
canela_aco_m3 = ArteEMagia('canela de aço',[2,0,-1],[0,0,1],golpes_artes)

# ARMADURA

armadura_couro = Armadura('armadura de couro', [2,0,0], [0,0,0], 4)
tunica_tubarao = Armadura('túnica de tubarão', [2,1,1], [0,0,0], 5)
kimono = Armadura('kimono', [2,0,0], [0,0,0], 4)
capacete_ferro = Armadura('capacete de ferro',[0,0,0],[0,0,0],2)
armadura_ferro = Armadura('armadura de ferro',[0,2,-1],[0,0,0],4)
armadura_tubarao = Armadura('armadura de tubarão',[1,2,0],[0,0,0],5)
bracelete_rubro = Armadura('bracelete rubro', [1,0,0],[0,0,0])
manopla_bronze = Armadura('manopla de bronze', [0,2,0],[0,0,0])
manopla_tubarao = Armadura('manopla de tubarão', [0,3,0],[0,0,0], 2)
amuleto_esq = Armadura('amuleto de amazonita (esq)', [0,0,2],[0,0,0])
capa_fleoganhere = Armadura('capa da fleoganhere',[1,0,2],[0,-1,0])


# PERSONAGENS

osel = Personagem('osel',[4,3,3,2,3],5,1,[espada_dupla], [canela_aco_m3], [ar], [0,tunica_tubarao,manopla_bronze,0])
japa = Personagem('o japa',[2,3,5,4,1],5,3,[katana,pistola,faca], [combate_basico], [], [0,tunica_tubarao,amuleto_esq,0])
vort = Personagem('vortigern',[4,5,2,1,3],5,2,[lanca, escudo, garra],[combate_basico],[fogo.add([explosao_pos])],[capacete_ferro,armadura_tubarao,manopla_tubarao,bracelete_rubro])
marcos = Personagem('marcos',[3,4,4,2,2],6,0,[],[punho_marinheiro_c75],[],[0,armadura_couro,0,0])

pirata = Personagem('pirata',[3,4,4,2,2],2,0,[espada],[combate_basico],[agua],[0,0,0,0])
guarda_himmellburg = Personagem('guarda de himmelburg',[3,4,3,3,2],4,0,[espada],[],[fogo],[0,0,0,0])
guarda_himmellburg_raio = Personagem('guarda de himmelburg',[2,3,4,4,2],4,0,[espada],[],[raio],[0,0,0,0])
guarda_marmore = Personagem('guarda de mármore',[4,3,3,3,2],2,0,[alabarda],[],[terra],[0,0,0,0])

dente_fogo = Personagem('dente-de-fogo', [5,5,2,4,1],18,0,[tubarao],[],[],[0,0,0,0])

pugilista_ep3 = Personagem('pugilista (ep3)',[4,3,3,3,2], 3, 0, [], [punho_marinheiro_c75], [raio], [0,0,amuleto_esq,0])
guerreiro_ep3 = Personagem('guerreiro (ep3)',[4,4,3,2,2], 3, 0, [espada], [], [], [0,0,bracelete_rubro,0])
mago_ep3 = Personagem('mago (ep3)',[2,3,3,5,2],3,1,[],[],[terra],[0,0,manopla_bronze,0])

driade = Personagem('dríade',[7,6,2,2,1],5,0,[arvore],[],[],[0,0,0,0])

drakenkemp = Personagem('drakenkemp',[4,3,7,4,3],10,0,[espada_dupla.imbue(soco_ardente_c75)],[soco_ardente_c75.add(golpes_artes_mestre)],[],[0,armadura_ferro,capa_fleoganhere,0])
redward = Personagem('redward',[6,5,2,6,2],10,0,[],[combate_basicao.imbue(terra)],[magma,terra.add(golpes_redward)],[0,armadura_ferro,capa_fleoganhere,0])


#japa.atacar(drakenkemp)

driade.atacar(osel.buffar([0,-2,-2]))

# barco himmelburg:
## 100 vida, 3 vel, 6 man, 3 estab, 4 alc, 5 cool, 10 dano

#todo
#+1 esquiva katana do japa
