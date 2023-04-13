import colorama
from colorama import Style
from os import system
import sys
import time
import random
import string
import pathlib
from phonenumbers import carrier
from phonenumbers import geocoder

#colors--
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#colors--
while True:
 system("clear")
 print(f"""{bgreen}    .....                 ...         
 .H8888888x.  '`+     .xH8%"```"%.    
:888888888888x.  !   x888~ xnHhx. ".  
8~    `"*88888888"  X888X 8**8888k `. 
!      .  `f"''"    8888X<~  `8888L ! 
 ~:...-` :8L <)88:  88888!   .!8*"" ` 
    .   :888:>X88!  `88888!"*888x     
 :~"88x 48888X ^`    `*8888  8888L    
<  :888k'88888X     .x.`888X X888X    
  d8888f '88888X   '888> %8X !8888..- 
 :8888!    ?8888>  '888   8  '8888%`  
 X888!      8888~    "*=="     ""     
 '888       X88f                      
  '%8:     .8*"                       
     ^----~"`
     Criado pôr Phant0m The Great""")
 print(f"""
{white}1{cyan}) {white}Criar CPF falso
{white}2{cyan}) {white}Criar CEP falso
{white}3{cyan}) {white}Criar CNPJ falso
{white}4{cyan}) {white}Criar E-MAIL falso
{white}5{cyan}) {white}Criar IP aleatório
{white}6{cyan}) {white}Informações da ferramenta
{white}7{cyan}) {white}Sair""")
 print('')
 esclh=input(f"""[{green}?{white}] Digite a sua escolha: """)

 if esclh == '1':
  system("clear")
  print(f"""{green}""")
  print('─────█─▄▀█──█▀▄─█─────')
  print('────▐▌──────────▐▌────')
  print('────█▌▀▄──▄▄──▄▀▐█────')
  print('───▐██──▀▀──▀▀──██▌───')
  print('──▄████▄──▐▌──▄████▄──')
  print(f"""{white}""")
  print('')
  print(f"""[{cyan}±{white}] Gerando CPF...""")
  print('')
  print(f"""[{blue}!{white}] CPF gerado com sucesso !""")
  print('')
  print(f"""[{bblue}*{white}] CPF:""",random.randint(00000000000, 99999999999))
  print('')
  input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '2':  
     system("clear")
     print(f"""{green}""")
     print('─────█─▄▀█──█▀▄─█─────')
     print('────▐▌──────────▐▌────')
     print('────█▌▀▄──▄▄──▄▀▐█────')
     print('───▐██──▀▀──▀▀──██▌───')
     print('──▄████▄──▐▌──▄████▄──')
     print(f"""{white}""")
     print('')
     print(f"""[{cyan}±{white}] Gerando CEP...""")
     print('')
     print(f"""[{blue}!{white}] CEP gerado com sucesso !""")
     print('')
     print(f"""[{bblue}*{white}] CEP:""",random.randint(00000000, 99999999))
     print('')
     input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '3':  
     system("clear")
     print(f"""{green}""")
     print('─────█─▄▀█──█▀▄─█─────')
     print('────▐▌──────────▐▌────')
     print('────█▌▀▄──▄▄──▄▀▐█────')
     print('───▐██──▀▀──▀▀──██▌───')
     print('──▄████▄──▐▌──▄████▄──')
     print(f"""{white}""")
     print('')
     print(f"""[{cyan}±{white}] Gerando CNPJ...""")
     print('')
     print(f"""[{blue}!{white}] CNPJ gerado com sucesso !""")
     print('')
     print(f"""[{bblue}*{white}] CNPJ:""",random.randint(00000000000000, 99999999999999))
     print('')
     input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '4':
     system("clear")
     print(f"""{green}""")
     print('─────█─▄▀█──█▀▄─█─────')
     print('────▐▌──────────▐▌────')
     print('────█▌▀▄──▄▄──▄▀▐█────')
     print('───▐██──▀▀──▀▀──██▌───')
     print('──▄████▄──▐▌──▄████▄──')
     print(f"""{white}""")
     print('')
     print(f"""[{cyan}±{white}] Gerando E-MAIL...""")
     email=('mestre@gmail.com', 'test@gmail.com', 'brassiilll@gmail.com', 'gals@gmail.com', 'apenaseu@gmail.com', 'eusimplismentenaoexisto@gmail.com', 'forever@gmail.com', 'issoeserio@gmail.com', 'achouqueeuestavabrincando@gmail.com', 'sorte@gmail.com', 'azar@gmail.com', 'pjsjs@gmail.com', 'apenas@gmail.com', 'vladmir@gmail.com', 'e13KKKnao@gmail.com', 'nobre@gmail.com', 'auaua@gmail.com', 'eisso@gmaio.com', 'email@gmail.com', 'password@gmail.com', 'skin@gmail.com', 'TCL@gmail.com', 'canseidavida@gmail.com', 'canseinao@gmail.com', 'kahdos@gmail.com', 'yes@gmail.com', 'eua@gmail.com', 'global@gamil.com', 'yaisha@gmail.com', 'jsij@gmail.com', 'rapazz@gmail.com', 'hsjsk@gmail.com', 'iaidj@gmail.com', 'jwisj@gmail.com', 'ksishaod@gmail.com', 'jdid@gmail.com', 'kjkoo@gmail.com', 'didisis@gmail.com', 'jjdjs@gmail.com','AAA@gmail.com', 'iiih@gmail.com', 'real@gmail.com', 'confia@gmaio.com', 'espanha@gmail.com', 'hsjsj@gmail.com', 'jdjdff@gmail.com', 'chinaaa@gmail.com', 'jsisilalap@gmail.com', 'hdhuq@gmail.com', 'ppao@gmaio.com', 'jsowjs@gmail.com', 'WYWYWWIA@gmail.com', 'KKKOJ@gmail.com', 'Google@gmail.com', 'FK@gmail.com', 'caraca@gmail.com', 'python@gmail.com', '20vencer70correr@gmail.com', 'aaaaaj@gmail.com', 'uai@gmail.com')
     print('')
     print(f"""[{blue}!{white}] E-MAIL gerado com sucesso !""")
     print('')
     print(f"""[{bblue}*{white}] E-MAIL:""",random.choice(email))
     print('')
     input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '5':
     system("clear")
     print(f"""{green}""")
     print('─────█─▄▀█──█▀▄─█─────')
     print('────▐▌──────────▐▌────')
     print('────█▌▀▄──▄▄──▄▀▐█────')
     print('───▐██──▀▀──▀▀──██▌───')
     print('──▄████▄──▐▌──▄████▄──')
     print(f"""{white}""")
     print('')
     print(f"""[{cyan}±{white}] Gerando IP...""")
     print('')
     print(f"""[{blue}!{white}] IP gerado com sucesso !""")
     print('')
     print(f"""[{bblue}*{white}] IP:""",random.randint(128, 191),'.',random.randint(0, 255),'.',random.randint(0, 255),'.',random.randint(0, 254))
     print('')
     input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '6':
   system("clear")
   print(f"""{green}
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*""")
   print(f"""{white}""")
   print(f"""
   [{yellow}*{white}] Nome da ferramenta: FK
   [{yellow}*{white}] Versão da ferramenta: V1
   [{yellow}*{white}] Criador: Phant0m The Great
   """)
   input('[&] Aperte em [ENTER] para voltar ao menu.')

 elif esclh == '7':
   system("clear")
   print(f"""{green}         ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''""")
   print(f"""{white}""")
   input('[&] Aperte em [ENTER] para sair.')
   print(f"""[{yellow}#{white}] Até a próxima !""")
   sys.exit()
