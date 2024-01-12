#importation
import pygame
from pygame.locals import *
import pygame, sys
#initialisation
pygame.init()
ecran=pygame.display.set_mode((0,0), pygame.FULLSCREEN)

rect_vide=pygame.image.load("./img/rect_vide.png").convert()
a=pygame.image.load("./img/A.png").convert()
b=pygame.image.load("./img/B.png").convert()
c=pygame.image.load("./img/C.png").convert()
d=pygame.image.load("./img/D.png").convert()
e=pygame.image.load("./img/E.png").convert()
f=pygame.image.load("./img/F.png").convert()
g=pygame.image.load("./img/G.png").convert()
h=pygame.image.load("./img/H.png").convert()
i=pygame.image.load("./img/I.png").convert()
j=pygame.image.load("./img/J.png").convert()
k=pygame.image.load("./img/K.png").convert()
l=pygame.image.load("./img/L.png").convert()
m=pygame.image.load("./img/M.png").convert()
n=pygame.image.load("./img/N.png").convert()
o=pygame.image.load("./img/O.png").convert()
p=pygame.image.load("./img/P.png").convert()
q=pygame.image.load("./img/Q.png").convert()
r=pygame.image.load("./img/R.png").convert()
s=pygame.image.load("./img/S.png").convert()
t=pygame.image.load("./img/T.png").convert()
u=pygame.image.load("./img/U.png").convert()
v=pygame.image.load("./img/V.png").convert()
w=pygame.image.load("./img/W.png").convert()
x=pygame.image.load("./img/X.png").convert()
y=pygame.image.load("./img/Y.png").convert()
z=pygame.image.load("./img/Z.png").convert()
ecran.blit(a,(30,100))
zoneClicableA=pygame.Rect((30,100),(50,70))
ecran.blit(b,(80,100))
zoneClicableB=pygame.Rect((60,100),(50,70))
ecran.blit(c,(130,100))
zoneClicableC=pygame.Rect((90,100),(50,70))
ecran.blit(d,(180,100))
zoneClicableD=pygame.Rect((120,100),(50,70))
ecran.blit(e,(230,100))
zoneClicableE=pygame.Rect((150,100),(50,70))
ecran.blit(f,(280,100))
zoneClicableF=pygame.Rect((180,100),(50,70))
ecran.blit(g,(330,100))
zoneClicableG=pygame.Rect((210,100),(50,70))
ecran.blit(h,(380,100))
zoneClicableH=pygame.Rect((240,100),(50,70))
ecran.blit(i,(30,170))
zoneClicableI=pygame.Rect((30,170),(50,70))
ecran.blit(j,(80,170))
zoneClicableJ=pygame.Rect((60,170),(50,70))
ecran.blit(k,(130,170))
zoneClicableK=pygame.Rect((90,170),(50,70))
ecran.blit(l,(180,170))
zoneClicableL=pygame.Rect((120,170),(50,70))
ecran.blit(m,(230,170))
zoneClicableM=pygame.Rect((150,170),(50,70))
ecran.blit(n,(280,170))
zoneClicableN=pygame.Rect((180,170),(50,70))
ecran.blit(o,(330,170))
zoneClicableO=pygame.Rect((210,170),(50,70))
ecran.blit(p,(380,170))
zoneClicableP=pygame.Rect((240,170),(50,70))
ecran.blit(q,(30,240))
zoneClicableQ=pygame.Rect((30,240),(50,70))
ecran.blit(r,(80,240))
zoneClicableR=pygame.Rect((60,240),(50,70))
ecran.blit(s,(130,240))
zoneClicableS=pygame.Rect((90,240),(50,70))
ecran.blit(t,(180,240))
zoneClicableT=pygame.Rect((120,240),(50,70))
ecran.blit(u,(230,240))
zoneClicableU=pygame.Rect((150,240),(50,70))
ecran.blit(v,(280,240))
zoneClicableV=pygame.Rect((180,240),(50,70))
ecran.blit(w,(330,240))
zoneClicableW=pygame.Rect((210,240),(50,70))
ecran.blit(x,(380,240))
zoneClicableX=pygame.Rect((240,240),(50,70))
ecran.blit(y,(30,310))
zoneClicableY=pygame.Rect((210,310),(50,70))
ecran.blit(z,(80,310))
zoneClicableZ=pygame.Rect((240,310),(50,70))




ecran.fill("white")











taille=8
essais=8
h=50
for i in range(taille):
    for j in range(essais):
        ecran.blit(rect_vide,(50*(i+1),h+(j*80)))
        zoneClicablerect=pygame.Rect((30*(i+1),h+(j*80)),(50,70))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

