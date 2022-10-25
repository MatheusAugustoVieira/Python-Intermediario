from random import randint
from time import sleep
import emoji
from pygame import mixer
print('\033[1;36m-=\033[m' * 12)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(emoji.emojize('''Suas opções:
[ 0 ] \033[1;31mPEDRA\033[m :fist:
[ 1 ] \033[1;34mPAPEL\033[m :hand:
[ 2 ] \033[1;33mTESOURA\033[m :v:''', use_aliases=True))
jogador = int(input('Qual a sua jogada? '))
print('\033[1;35mJO\033[m')
sleep(1)
print('\033[1;35mKEN\033[m')
sleep(1)
print('\033[1;35mPO!!!\033[m')
print('\033[1;36m-=\033[m' * 12)
print(emoji.emojize('\033[1;36;40mComputador jogou {} \033[m :computer:'.format(itens[computador]), use_aliases=True))
print(emoji.emojize('\033[1;35;40mJogador jogou {}\033[m :video_game:'.format(itens[jogador]), use_aliases=True))
print('\033[1;36m-=\033[m' * 12)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print(emoji.emojize('\033[1;35;40mEMPATE\033[m :sleepy:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    elif jogador == 1:
        print(emoji.emojize('\033[1;32;40mJOGADOR VENCE\033[m :sparkles:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
        mixer.init()
        mixer.music.load('ex021.mp3')
        mixer.music.play()
        input(emoji.emojize('\033[7;29;40mCurte o som\033[m :sound:', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1;31;40mCOMPUTADOR VENCE\033[m :dizzy_face:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    else:
        print(emoji.emojize('JOGADA INVÁLIDA! :x:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print(emoji.emojize('\033[1;31;40mCOMPUTADOR VENCE\033[m :dizzy_face:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    elif jogador == 1:
        print(emoji.emojize('\033[1;35;40mEMPATE\033[m :sleepy:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    elif jogador == 2:
        print(emoji.emojize('\033[1;32;40mJOGADOR VENCE\033[m :sparkles:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
        mixer.init()
        mixer.music.load('ex021.mp3')
        mixer.music.play()
        input(emoji.emojize('\033[7;29;40mCurte o som\033[m :sound:', use_aliases=True))
    else:
        print(emoji.emojize('JOGADA INVÁLIDA! :x:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print(emoji.emojize('\033[1;32;40mJOGADOR VENCE\033[m :sparkles:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
        mixer.init()
        mixer.music.load('ex021.mp3')
        mixer.music.play()
        input(emoji.emojize('\033[7;29;40mCurte o som\033[m :sound:', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[1;31;40mcOMPUTADOR VENCEU\033[m :dizzy_face:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    elif jogador == 2:
        print(emoji.emojize('\033[1;35;40mEMPATE\033[m :sleepy:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
    else:
        print(emoji.emojize('JOGADA INVÁLIDA! :x:', use_aliases=True))
        print('\033[1;36m-=\033[m' * 12)
