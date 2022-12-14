import key_detect as key

artigo01 = "Seis meses após a morte do Czar Nicolau II e toda sua família A cidade está se preparando para o solstício de inverno, enquanto as tensões crescem \n ainda mais. Os bolcheviques estão no poder e o chamado Exército Branco está unido para uma revolução e restaurar a monarquia.\n Não há o menor respeito à propriedade e à vida de pessoa alguma. \n"
artigo02 = "Em todas as vilas, cidades e lugarejos da Rússia estalam motins e \n insurreições armadas, havendo o povo deposto as autoridades. \n Centenas de vagões repletos de víveres encontram-se paralisados nas estações, em virtude da falta de carvão e pessoal para conduzi-los. \n Porém o sentimento nacionalista do povo russo repele qualquer paz que seja \nfeita com humilhação e prejuízo da Rússia. Os partidários do Czarismo, que contam \ncom grandes e poderosos elementos, vêm desenvolvendo grande propaganda em \n favor da restauração da monarquia especialmente entre os exércitos da frente e os \n camponeses.”"
introducao = "O jogo a seguir consiste de um modelo em que as escolhas do jogador definem os acontecimentos futuros e o final da história, tome cuidado com o que escolhe..."
confiarNikolai = 0

nome = input("Insira seu nome: \n >>> ")

print("\n", introducao)
key.getchar()
print("\nSão Petersburgo, Rússia\n17 de dezembro de 1918\nJornal Pravda\n")
key.getchar()
print("\n", artigo01)
key.getchar()
print("\n", artigo02)
key.getchar()

print("É tarde da noite, as ruas estão desertas, janelas fechadas e luzes apagadas. Por sorte, não \n há ninguém vigiando. Estou acompanhado pelo Gueorgui Júkov, general do exército\n vermelho. Me dirijo ao jornal, estou desconfiado de uma perseguição, ninguém pode\n descobrir que sou o dono.\nOuço um barulho em um beco perto de mim e desvio do meu caminho original para ver do\n que se trata. O general insiste para que continuemos em frente\n")
key.getchar()

certo01 = False
while certo01 == False:
    escolha01 = input(
        "1) Ir até o local e verificar\n2) Ignorar e seguir o caminho\n")
    if escolha01 == "1":
        certo01 = True
        print("\nMeu instinto me diz que há algo de errado e entro no beco. Não encontro a fonte. Outro barulho, um tiro, veio do jornal. \nCorro até lá, o general está morto na entrada do prédio. ")
    elif escolha01 == "2":
        certo01 = True
        print(" \nSigo até o jornal, aceno para o general. Um barulho. O  homem a minha frente está caido no chão. O tiro o matou.")
key.getchar()

print("Corro até o corpo, olho ao redor e vejo uma sombra virando uma esquina. Algo está errado. Corro para tentar alcançar a figura. Nada.")
key.getchar()

print("20 de dezembro de 1918 \n 3 dias após o incidente \n Só se fala na morte de Gueorgui, o jornal está um caos.")
key.getchar()
print("Acordo com o barulho de uma pessoa batendo em minha porta. Olho no relógio, são 4 horas da manhã. Atendo a porta. Um homem de uns 40 anos está parado, suas roupas e sua cara revelam que saiu às pressas de algum lugar.")
key.getchar()
print("\n- Quem é você? Não viu as horas?")
key.getchar()
print("\n- Sou o detetive Petrov, mas pode me chamar de Nikolai. Estou investigando o assassinato do General Gueorgui, pelo que ouvi, você estava lá.")
key.getchar()
print("\n- Olha, pela décima vez, não tenho nada a ver com isso, não vou responder mais perguntas.")
key.getchar()
print("\n- Espera, confio em você. Tenho algumas pistas de quem pode ser, mas preciso da sua ajuda.")
key.getchar()

certo02 = False
while certo02 == False:
    escolha02 = input(
        "1) Confiar em Nikolai\n2) Não confiar em Nikolai\n")
    if escolha02 == "1":
        certo02 = True
        print("\n- Ok, pode entrar. Estou ouvindo.")
        confiarNikolai = confiarNikolai + 1
    elif escolha02 == "2":
        certo02 = True
        print("\n- Olha, não queria ter que chegar a esse ponto, mas já que você está desconfiado. - diz Nikolai.")
        key.getchar()
        print("\nEle me joga uma pasta cheia de provas de que sou o culpado.")
        key.getchar()
        print("\n- Ok, pode entrar. Estou ouvindo.")
key.getchar()

print("\nApós Nikolai entrar ofereço uma xícara de chá e um local para se sentar")
key.getchar()
print("\nNikolai senta e começa a falar:")
key.getchar()
print("\n- Bom, a polícia está de olho em você, você foi o único no local, não havia mais ninguém ao redor. Posso afirmar que você é o principal suspeito. Caso você não queira parar atrás das grades e acabar com seu jornal, tenho uma proposta para você.")
key.getchar()
print("\n- Como você sabe sobre meu jornal?")
key.getchar()
print("\n- Não importa, o ponto aqui é que estou procurando o assassino e preciso da sua ajuda, você parece ser um homem honesto e com sua habilidade de jornalista podemos encontrar o culpado. Claro com uma condição, em troca, quero informações sobre o Duque Dookan.")
key.getchar()
print("\n- Claro, estava muito bom para ser verdade. Por que você quer saber desse Duque?")
key.getchar()
print("\n- Só um suspeito de outra investigação minha. Caso você se mostre digno, talvez eu conte para você.")
key.getchar()

certo03 = False
while certo03 == False:
    escolha03 = input(
        "1) Aceitar proposta\n2) Não aceitar proposta\n")
    if escolha03 == "1":
        certo03 = True
        print("\n- Ok, combinado.")
        key.getchar()
        print("\nEle me entrega um papel com dois endereços.")
        key.getchar()
        print("\n- O primeiro é onde estará a primeira pista que devemos seguir. É importante que você esteja lá logo de manhã. Quando achar, me encontre no segundo local.")
        confiarNikolai = confiarNikolai + 2
    elif escolha03 == "2":
        certo03 = True
        print("\n- Olha, isso tá cheirando mal, então, não, não aceito.")
        key.getchar()
        print("\n- Eu estou tentando ao máximo aqui te convencer, isso é muito importante para mim e também para você. Se você não aceitar, no máximo em uma semana você estará na cadeia. Talvez até sendo executado.")
        key.getchar()
        print("\n- Hum, e o tal Duque? Acha que é fácil conseguir informações assim?")
        key.getchar()
        print("\n- Eu só quero informações para resolver outro caso, com todo meu profissionalismo. ")
        key.getchar()
        print("\n- Posso ter um tempo para pensar pelo menos?")
        key.getchar()
        print("\n- Não temos tempo, tenho uma pista que deve ser seguida hoje mesmo. É agora ou nunca.")
        key.getchar()
        print("\n- Ok, então combinado. ")
        key.getchar()
        print("\n- Ele me entrega um papel com dois endereços.")
        key.getchar()
        print("\n- O primeiro é onde estará a primeira pista que devemos seguir. É importante que você esteja lá logo de manhã. Quando achar, me encontre no segundo local.")
key.getchar()

print("\nFechando a porta, de repente Nikolai entra no batente: ")
key.getchar()
print("\n- Então, só mais uma coisa. Estou hospedado em um hotel do outro lado da cidade e tá meio tarde para voltar, será que posso passar a noite aqui?")
key.getchar()

certo04 = False
while certo04 == False:
    escolha04 = input(
        "1) Oferecer um quarto para Nikolai\n2) Dizer que não há espaço suficiente\n")
    if escolha04 == "1":
        certo04 = True
        print("\n- Pode entrar, tenho um quarto sobrando.")
        confiarNikolai = confiarNikolai + 2
        relogioRoubado = True
    elif escolha04 == "2":
        certo04 = True
        print("\n- Infelizmente não tenho espaço suficiente aqui. ")
        key.getchar()
        print("\n- Ok então,  até amanhã. Não esqueça de procurar bem a pista.")
        relogioRoubado = False
key.getchar()

if relogioRoubado == False:
    print("\n21 de dezembro de 1918\n9h36min")
    key.getchar()
    print("\nEstou atrasado, não ouvi o despertador, deveria chegar no local até as 10h. Saio as pressas, ao chegar noto que é uma biblioteca.")
    key.getchar()

if relogioRoubado == True:
    print("\n21 de dezembro de 1918\n8h35min")
    key.getchar()
    print("\nO despertador tocou e levantou para me arrumar. Saio com a sensação de que está faltando algo. Muito provavelmente é só impressão.\nChego no primeiro local e percebo que é uma biblioteca ")
    key.getchar()

print("\nEntro e me deparo com um homem sentado na recepção. ")
key.getchar()
print("\n- Hm, bom dia. Estou aqui para uma investigação. ")
key.getchar()
print("\n- Ah, sim. Nikolai me falou que você viria. Prazer, sou Alberanski, o gerente da biblioteca. A pista que você procura está na prateleira 7 e lembre-se: Não se conhece completamente uma ciência enquanto não se souber da sua história.")
key.getchar()
print("\nChego até a prateleira e me deparo com o seguintes livros: ")
key.getchar()
print("\n1) Iluminismo - principais autores\n2) A invenção da escrita\n3) Como era a relação feudal na Idade Média\n4) Neolítico e a agricultura\n5) Relação entre duas civilizações: Roma e Grécia\n6) O avanço tecnológico da revolução industrial - Belle Epoque\n7) Independência das colônias americanas")
key.getchar()

tentativa01 = 0
respostaCerta01 = "Narciso"
acertou01 = False
while tentativa01 < 3:
    enigma01 = input(
        "1) Dar resposta\n2) Dica\n")
    if enigma01 == "1":
        resposta01 = input("Insira sua resposta:\n")
        if resposta01 == respostaCerta01:
            print("\n- Narciso, isso!")
            acertou01 = True
            break
        elif resposta01 != respostaCerta01:
            print("\nAcho que não é isso, vou tentar novamente.")
            tentativa01 = tentativa01 + 1
    elif enigma01 == "2":
        print(
            "\nDica: Os títulos parecem formar uma palavra. O que o Alberanski disse mesmo?")
key.getchar()

if tentativa01 == 1:
    confiarNikolai = confiarNikolai + 1
elif tentativa01 == 2:
    confiarNikolai = confiarNikolai + 2
elif tentativa01 == 3:
    confiarNikolai = confiarNikolai + 3

if acertou01 == True:
    print("\nChego até Alberanski e pergunto se ele sabe de algo.")
    key.getchar()
    print("\n- Ah, Narciso. Bom, você pode procurar algo na mitologia grega ou na seção de flores. Tenho muitos livros sobre botânica, principalmente se você quer presentear alguém especial.")
    key.getchar()
    print("\nEstou atrasado, devo encontrar Nikolai em 20 minutos.")
    key.getchar()

    certo05 = False
    while certo05 == False:
        escolha05 = input(
            "1) Consultar o livro de Mitologia Grega\n2) Consultar o livro de Botânica\n3)Ir encontrar Nikolai\n")
        if escolha05 == "1":
            certo05 = True
            print("\nSegundo o mito, Narciso era tão belo e tão vaidoso que, após desprezar inúmeras pretendentes, acabou se apaixonando pelo próprio reflexo. Morreu de fome e sede à beira da fonte de água onde via sua imagem refletida. O mito nos ensina que o excesso de vaidade e falta de empatia pelos outros podem ser prejudiciais.")
            confiarNikolai = confiarNikolai + 1
        elif escolha05 == "2":
            certo05 = True
            print("\nApesar de lindos e muito decorativos, os narcisos, pois significam egoísmo, vaidade, mentira e formalidade. ")
        elif escolha05 == "3":
            certo05 = True
            print("\n- Obrigado, mas estou atrasado. Adeus.")
            confiarNikolai = confiarNikolai + 3
    key.getchar()

if acertou01 == False:
    print("\n- Com licença, Alberanski. Não encontrei nada, você sabe de algo?")
    key.getchar()
    print("\n- Achei que você fosse mais capaz, mas ok. Só saiba que sua flor favorita é Narciso.")
    key.getchar()
    print("\n- An? Como assim?")
    key.getchar()
    print("\n- Adeus jovem, preciso sair para resolver algumas pendências. ")
key.getchar()

print("\nSaio depressa em direção ao restaurante indicado. Avisto Nikolai e vou até a mesa.")
key.getchar()
print("\n- Então, como foi? -  Nikolai Pergunta")
key.getchar()

if acertou01 == True:
    certo06 = False
    while certo06 == False:
        escolha06 = input(
            "1) Revelar pista\n2) Não revelar a pista\n")
        if escolha06 == "1":
            certo06 = True
            print("\n- Sim, Narciso. O que isso significa?")
            key.getchar()
            print("\n- Bem, interessante. Acho que vamos descobrir juntos. Você fez um ótimo trabalho, portanto, vou revelar um pouco dos meus planos.")
            confiarNikolai = confiarNikolai + 2
        elif escolha06 == "2":
            certo06 = True
            print("\n- Não tenho uma pista concreta, mas vou trabalhar com isso.")
            key.getchar()
            print("\n- Interessante. Ok, vou revelar um pouco dos meus planos.")
    key.getchar()

if acertou01 == False:
    certo06 = False
    while certo06 == False:
        escolha06 = input(
            "1) Revelar sua flor favorita\n2) Dizer que não encontrou nada\n")
        if escolha06 == "1":
            certo06 = True
            print("\n- Você sabia que minha flor favorita é Narciso?")
            key.getchar()
            print("\n- O que você quer dizer com isso?")
            key.getchar()
            print("\n- Está é a pista.")
            key.getchar()
            print("\n- Bem, interessante. Acho que vamos descobrir juntos. Você fez um ótimo trabalho, portanto, vou revelar um pouco dos meus planos.")
            confiarNikolai = confiarNikolai + 1
        elif escolha06 == "2":
            certo06 = True
            print("\n- Não tenho uma pista concreta, mas vou trabalhar com isso.")
            key.getchar()
            print("\n- Interessante. Acho que é mais questão de confiança aqui, portanto vou revelar um pouco dos meus planos.")
    key.getchar()

print("\n- Estou escutando.")
key.getchar()
print("\n- Minha filha está desaparecida. Ela fugiu para encontrar esse tal Duque Dookan. Deixou uma carta me avisando. Quando fui a casa desse sujeito ninguém quis me receber e ainda me chamaram de louco! Preciso de informações para desmascarar esse homem. ")
key.getchar()

certo07 = False
while certo07 == False:
    escolha07 = input(
        "1) Revelar uma informação\n2) Dizer que vai investigar\n")
    if escolha07 == "1":
        certo07 = True
        print("\n- Duque Dookan é um infiltrado. Além de manter contato com líderes do exército da Alemanha.  Só isso que eu sei.")
        confiarNikolai = confiarNikolai + 2
    elif escolha07 == "2":
        certo07 = True
        print("\n- Não sei nada sobre esse Duque. Mas vou investigar.")
key.getchar()

print("\n- Bom, agora acho que o crucial é irmos à cena do crime. Tudo bem por você? Sei que pode ser meio delicado para você, então há outro lugar a ser investigado, se você preferir.")
key.getchar()
print("\n- E que lugar seria?")
key.getchar()
print("\n- O escritório do general, consegui a chave e a autorização. ")
key.getchar()

certo08 = False
while certo08 == False:
    escolha08 = input(
        "1) Acompanhar Nikolai a cena do crime\n2) Ir sozinho ao escritório do general\n")
    if escolha08 == "1":
        certo08 = True
        print("\n- Por enquanto prefiro investigar junto com você. Vou à cena do crime.")
        acompanhou = True
        confiarNikolai = confiarNikolai + 3
    elif escolha08 == "2":
        certo08 = True
        print("\n- Não estou me sentindo bem para retornar lá. Prefiro ir ao escritório. ")
        key.getchar()
        print("\n- Beleza, vamos investigar separados e nos reencontrar amanhã então. Mesmo restaurante às 8h.")
        key.getchar()
        print("\n- Combinado. Até amanhã.")
        acompanhou = False
key.getchar()

incriminado = False
if relogioRoubado == True:
    incriminado = True

if acompanhou == True:
    print("\nChegando ao local, vocês se separam. Sua busca não dá nenhum resultado.")
    key.getchar()
    print("\n- Então, algo? - Nikolai pergunta ")
    key.getchar()
    print("\n- Nada e você?")
    key.getchar()
    print("\n- Também nada. Mas tive uma ideia. Fique posicionado onde o General estava, vou testar alguns ângulos.")
    key.getchar()
    print("\nApós entrar em um beco à direita ele grita:")
    key.getchar()
    print("\n- É isso! Veja! - Ele tira algo da lixeira. - A arma do crime está bem aqui.")
    key.getchar()

    print("\n22 de dezembro de 1918\n9h da manhã\nEscritório do general\n")
    key.getchar()
    print("\n- Parece estar tudo certo. - eu digo")
    key.getchar()
    print("\n- Certo até demais. Deve ter algo aqui. - Nikolai responde.")
    key.getchar()
    print("\nAo vasculhar a sala acabo achando um porta joias, ao abrir noto uma mensagem:")
    key.getchar()
    print("\nDividir sessenta por meio, adicione vinte.")
    key.getchar()
    print("\nO que isso significa? ")
    key.getchar()
    print("\n- Ei, olha o que eu achei. ")
    key.getchar()
    print("\nNikolai mostra um cofre que estava escondido. ")
    key.getchar()
    print("\n- Só precisamos da senha agora. ")
    key.getchar()

    tentativa02 = 0
    respostaCerta02 = "140"
    acertou02 = False
    while tentativa02 < 3:
        enigma02 = input(
            "1) Eu sei a senha\n2) Não faço a mínima ideia.\n")
        if enigma02 == "1":
            resposta02 = input("Insira a senha correta:\n")
            if resposta02 == respostaCerta02:
                print(
                    "\n- Ok, deixa eu dar uma olhada. - Nikolai pede com uma certa pressa")
                key.getchar()
                print("\nNikolai vasculha todos os papéis com uma cara de decepcionado.")
                key.getchar()
                print(
                    "\n- Nada. Só esse cartão de um alfaiate. Talvez pode ser uma pista.")
                key.getchar()
                confiarNikolai = confiarNikolai + 1
                acertou02 = True
                break
            elif resposta02 != respostaCerta02:
                print("\nEssa senha não funcionou...")
                key.getchar()
                tentativa02 = tentativa02 + 1
        elif enigma02 == "2":
            tentativa02 = tentativa02 + 3
            acertou02 = False
    key.getchar()

    if acertou02 == True:
        print("\n- Bem, vamos seguir a pista do alfaiate então. Se está aqui no cofre, deve ser pessoal.")
        key.getchar()

    if acertou02 == False:
        print("\n- É, não deu certo")
        key.getchar()
        print("\n- Tudo bem, tá dando nossa hora mesmo. Talvez podemos pensar nisso e retornar depois. ")
        key.getchar()
        print("\n- Ok. - Eu digo um pouco decepcionado")
        key.getchar()
        print("\n- Ah, me lembrei. Um dos meu contatos me conseguiu isso: o endereço do alfaiate do general. Eles se encontraram no último dia, ele pode saber de algo. Vamos?")
        key.getchar()
        print("\n- Claro.")
    key.getchar()

respostaCerta03 = "140"
if acompanhou == False:
    print("\nAo chegar no escritório, já sinto que algo está errado. Tudo parece estar perfeitamente em seu lugar, menos um vaso de flores. Ao me virar, noto um cofre na parede. Qual será a senha?")
    certo09 = False
    while certo09 == False:
        escolha09 = input(
            "1) Investigar estante de livros \n2) Investigar gavetas do arquivo\n3) Investigar porta joias da escrivaninha\n4) Investigar o vaso de flores\n")
        if escolha09 == "1":
            print("\nNada aqui")
            key.getchar()
        elif escolha09 == "2":
            print("\nNada aqui")
            key.getchar()
        elif escolha09 == "3":
            certo09 = True
            print("\nAo abrir o porta joias há algo escrito: ")
            key.getchar()
            print("\nDividir sessenta por meio, adicione vinte.")
            key.getchar()
            print("\nJá sei a senha!")
            key.getchar()
            resposta03 = 0
            while resposta03 != respostaCerta03:
                print("\n1) 30\n2) 50\n3) 80\n4) 140")
                resposta03 = input("Insira a senha correta:\n")
            print("\nIsso! Acertei.")
            key.getchar()
            print("\nAo abrir o cofre há vários documentos, alguns rasurados. Um me chama atenção, o nome Nikolai Petrov está bem no topo do papel, junto com um selo de Júlio César. ")
            key.getchar()
            print("\nNesse documento existe um trecho de sete palavras no sétimo parágrafo que me chamou atenção, aparentemente foi escrito a sete dias")
            key.getchar()
            print("\nZltwyl thualuoh zlbz puptpnvz wvy wlyav, whyjlpyv.")
            key.getchar()
            print("\nÉ um bilhete trocado entre os dois. Codificado. Não sabia que se conheciam, algo está errado. ")
        elif escolha09 == "4":
            print("\nNada aqui")
            key.getchar()
    key.getchar()

    print("\n22 de dezembro de 2018\n9h\n")
    key.getchar()
    print("\n- Então, alguma coisa? - diz Nikolai")
    key.getchar()
    print("\n- Nada importante. Tudo estava perfeitamente normal. E você? Encontrou algo?")
    key.getchar()
    print("\n- Puxa! Má sorte a sua. Bem, consegui duas pistas. A primeira foi a arma do crime dentro de uma lixeira, já encaminhei ela para a polícia, e a segunda pista foi esse cartão que estava junto da arma, pertence a um alfaiate que tinha o General como cliente. Vamos até o estúdio dele?")
    key.getchar()
    print("\n- Claro que podemos, se estava perto da arma a chance dele estar relacionado ao crime é alta.")
    key.getchar()


print("\nEncontramos com o alfaiate, o nome dele é Marc Moreau.")
key.getchar()
print("\n- Bonjour! Comment puis-je t'aider?")
key.getchar()

certo10 = False
while certo10 == False:
    escolha10 = input(
        "1) Ele não fala nosso idioma?\n2) Permanecer em silêncio\n")
    if escolha10 == "1":
        certo10 = True
        print("\n- Parece que não. Você sabe falar francês?")
        key.getchar()
        print("\n- Não, apenas um pouco de Alemão.")
        key.getchar()
        print("\n- Então deixa que eu interrogo ele")
        key.getchar()
        print("\n- Vá em frente")
        confiarNikolai = confiarNikolai + 1
    elif escolha10 == "2":
        certo10 = True
key.getchar()

print("\n- Salut l'ami. - diz Nikolai.")
key.getchar()
print("\n- Qu'as-tu pour aujourd'hui l'ami ? Avez-vous encore crevé votre chaussure?")
key.getchar()
print("\n- Pas aujourd'hui. Celui à côté de moi est le moldu du moment, appliquons lui le plan B2, comme convenu.")
key.getchar()
print("\nMarc me olha com um olhar surpreso.  O que será que estão dizendo?")
key.getchar()
print("\n-  Donc juste pour récapituler, on lui reproche d'avoir utilisé la montre que vous avez volée, il va en prison, écope de la peine de mort, et à la fin on boit ? - diz Marc")
key.getchar()
print("\n- Exactement, maintenant que j'ai fini de parler, dites quelque chose comme si vous niez quelque chose et renvoyez-nous")
key.getchar()
print("\n- Je ne sais pas de quoi tu parles, maintenant si tu veux me faire une faveur et partir, la porte est juste là")
key.getchar()
print("\nNikolai de repente bufa de nervoso.")
key.getchar()
print("\n- O que aconteceu? Ele falou algo? - pergunto.")
key.getchar()
print("\n- Nada. Ele não sabe de nada e agora quer a gente fora daqui.")
key.getchar()
print("\n- E se a gente encurralar ele? Talvez mostrar a arma? - cochicho.")
key.getchar()
print("\nNikolai pisca para mim e vira para o alfaiate.")
key.getchar()
print("\n- Pouvez-vous nous montrer les fonds ?")
key.getchar()
print("\n- Non!")
key.getchar()
print("\nNikolai mostra um distintivo de policial.")
key.getchar()
print("\n- Pensei que você era apenas um detetive particular.")
key.getchar()
print("\n- Ter contatos na polícia é útil às vezes. Por isso, sempre tenho.")
key.getchar()
print("\nVamos até os fundos, Nikolai retira a arma de uma sacola e mostra para o sujeito. No mesmo instante, ele tenta fugir, porém alcançamos ele e o imobilizamos.")
key.getchar()
print("\n- Ok, vamos até a delegacia.")
key.getchar()
print("\nAo chegar lá, havia várias viaturas do lado de fora e vários policiais na recepção.")
key.getchar()
print("\n- Olá, desejo ver o delegado, é urgente. - Nikolai fala para o recepcionista.")
key.getchar()
print("\n- E quem é você? O que há de tão urgente?")
key.getchar()
print("\n- Estou com um suspeito do assassinato do General Júkov. Sou o Detive Petrov.")
key.getchar()
print("\n- Sim senhor, só um instante.")
key.getchar()
print("\nEle volta e nos direciona até a sala do delegado Ivan.")
key.getchar()
print("\n- Olá Detetive Petrov! Então, temos o suspeito?")
key.getchar()
print("\n- Sim, podemos?")
key.getchar()
print("\n- Pra já. Seu amigo pode esperar aqui enquanto interrogamos ele. Fica a vontade, tem água e comida ali caso queira.")
key.getchar()
print("\nEnquanto espero, ouço dois homens conversando.")
key.getchar()
print("\n- Será que encontraram o suspeito mesmo? Não é possível que seja o sapateiro, eu conhecia o pai dele, ele não criaria um filho assim.")
key.getchar()
print("\n- Não mesmo, mas sinto pena do general, não só foi assassinado mas se afogou com o próprio sangue enquanto morria.")
key.getchar()
print("\n- Pois é, o tiro ter acertado o pulmão esquerdo foi um azar, sofreu até o último segundo.")
key.getchar()
print("\n- Pois é, uma pena, mas onde o senhor vai agora doutor?")
key.getchar()
print("\n- Vou terminar a autópsia no corpo do general, tem mais algumas coisas que eu queria confirmar antes de entregá-lo à família.")
key.getchar()

capturado = False
if confiarNikolai <= 10:
    print("\nNikolai disse que o ângulo do tiro foi do lado direito. Nunca acertaria o pulmão esquerdo dessa forma.")
    certo11 = False
    while certo11 == False:
        escolha11 = input(
            "1) Seguir o doutor\n2) Ignorar\n")
        if escolha11 == "1":
            certo11 = True
            print(
                "\nSaio discretamente da sala e sigo o doutor até a sala de autópsia. Entro sem ser percebido.")
            certo12 = False
            while certo12 == False:
                escolha12 = input(
                    "1) Conversar com o doutor\n2) Esperar ele ir embora e investigar\n")
                if escolha12 == "1":
                    certo12 = True
                    print("\n- Hm… olá?")
                    key.getchar()
                    print("\n- Quem é você? O que está fazendo aqui?")
                    key.getchar()
                    print(
                        "\n- Estou ajudando Nikolai com a investigação da morte do general.")
                    key.getchar()
                    print(
                        "\n- Ah, então quer dizer que aquele mau caráter está enganando outro agora?")
                    key.getchar()
                    print("\n- Como assim?")
                    key.getchar()
                    print("\n- Todos que se relacionam com esse sujeito somem sem motivo algum, mas ninguém questiona, pois esses bolinhas ficam ao seu lado. Sempre busquei provas, mas nunca consegui encontrar algo. Principalmente pelo o que ele fez com a Yelena. ")
                    key.getchar()
                    print("\n- Quem seria essa?")
                    key.getchar()
                    print("\n- Uma mulher que ele era apaixonado. Ela sempre aparecia estranha, com medo. Ela conseguiu fugir, com sorte. Dizem que o Duque Dookan está ajudando ela.")
                    key.getchar()
                    print(
                        "\n- Duque Dookan? Não. Ele sequestrou Yelena, ela é filha de Nikolai. Ele está tentando salvar ela.")
                    key.getchar()
                    print("\n- Então é isso que ele diz? Que piada boa. Claro que ela é muito mais nova, mas filha? Seria um relacionamento fraternal muito dos errados então. Pelo jeito ele já fez sua cabeça.")
                    key.getchar()
                    print("\nDe repente, um alarme de emergência toca pela delegacia.")
                    key.getchar()
                    print("\n- Alarme de criminoso à solta? Por quê? - diz o doutor.")
                    key.getchar()
                    print(
                        "\nA porta abre com força. O delegado e Nikolai entram e correm até mim. ")
                    key.getchar()
                    print(
                        "\n- O filho do sapateiro nos falou tudo. Você está preso sobre suspeita do assassinato do general!")
                    capturado = True
                elif escolha12 == "2":
                    print("\nEu espero pacientemente o doutor ir embora, mas ele não aparenta estar terminando seu trabalho tão cedo. Alguns minutos se passam e um alarme de emergência toca pela delegacia e o doutor sai da sala para ver do que se trata. Essa é minha chance. ")
                    key.getchar()
                    certo13 = False
                    while certo13 == False:
                        escolha13 = input(
                            "1) Ir até o corpo\n2)Esperar um pouco mais \n")
                        if escolha13 == "1":
                            certo12 = True
                            certo13 = True
                            print(
                                "\nVou até o corpo e realmente o tiro foi dado no lado esquerdo. Nikolai realmente mentiu.")
                            key.getchar()
                            print(
                                "\nDe repente, a porta é aberta pelo Doutor e Nikolai.")
                            key.getchar()
                            print("\n- Ele está tentando sumir com o corpo!")
                            key.getchar()
                            print("\n- N-não é o que parece…")
                            key.getchar()
                            print(
                                "\n- O filho do sapateiro nos falou tudo. Você está preso sobre suspeita do assassinato do general!")
                            capturado = True
                            break
                        elif escolha13 == "2":
                            certo13 = True
                            print(
                                "\nEu ouço um barulho no corredor e decido ficar escondido um pouco mais. De repente, a porta se abre e ouço duas vozes:")
                            key.getchar()
                            print("\n- Ele deve estar aqui. Precisamos prendê-lo. ")
                            key.getchar()
                            print("\nÉ a voz de Nikolai. ")
                            key.getchar()
                            print(
                                "\n- O filho do sapateiro não estava mentindo. Esse cara realmente é perigoso.")
                            key.getchar()
                            print("\nEspera, eles estão atrás de mim?")
                            key.getchar()
                            print(
                                "\nEles vão embora e decido fugir dali. Preciso de um esconderijo e ajuda.")
                            key.getchar()
                            certo14 = False
                            while certo14 == False:
                                escolha14 = input(
                                    "1) Ir para o escritório do general\n2) Ir para a biblioteca de Alberanski\n")
                                if escolha14 == "1":
                                    certo12 = True
                                    certo14 = True
                                    print(
                                        "\nChegando até lá percebo que está tudo cercado. ")
                                    key.getchar()
                                    print("\n- Ali, ele está ali!")
                                    key.getchar()
                                    print(
                                        "\nTento fugir, mas conseguem me capturar.")
                                    key.getchar()
                                    print(
                                        "\n- Você está preso em flagrante sobre suspeita do assassinato do general!")
                                    key.getchar()
                                    capturado = True
                                elif escolha14 == "2":
                                    certo12 = True
                                    certo14 = True
                                    print(
                                        "\nChego até a biblioteca de Alberanski e vejo as luzes acesas. Bato na porta e rapidamente ele abre.")
                                    key.getchar()
                                    print(
                                        "\n- Estava esperando por você. Sabia que não me decepcionaria. ")
                                    key.getchar()
                                    print("\n- Estão me incriminado.")
                                    key.getchar()
                                    print(
                                        "\n- Eu já sei. Venha, eu posso te ajudar. O General já desconfiava disso tudo, então me deixou provas, preciso da sua habilidade. ")
                                    key.getchar()
                                    print("\n- Como assim ele já sabia?")
                                    key.getchar()
                                    print(
                                        "\n- Pois é, ele era um infiltrado. Você tem muitos inimigos, sabia? Era para você estar morto, ele te salvou. ")
                                    key.getchar()
                                    print(
                                        "\nAlberanski me entrega uma caixa trancada. ")
                                    key.getchar()
                                    print(
                                        "\n- Os papéis estão aqui dentro. Faça sua mágica. É um código.")
                                    key.getchar()
                                    print("\nCódigo: .--. . --. ---")
                                    key.getchar()

                                    tentativa03 = 0
                                    respostaCerta03 = "Pego"
                                    acertou03 = False
                                    while tentativa03 < 3:
                                        enigma03 = input(
                                            "1) Eu decifrei o código\n2) Não faço a mínima ideia.\n")
                                        if enigma03 == "1":
                                            resposta03 = input(
                                                "Insira o código decifrado:\n")
                                            if resposta03 == respostaCerta03:
                                                print(
                                                    "\nAs provas estavam todas lá. Os seus planos, planejava matar não só a mim como várias outras pessoas importantes. A ideia do poder subiu à cabeça. Ele tinha muitos contatos na polícia, e seus nomes estavam ali também.")
                                                key.getchar()
                                                print(
                                                    "\nEstava escrito: confie apenas no Markos.")
                                                key.getchar()
                                                print(
                                                    "\n- Preciso falar com Markos. Me ajude, Alberanski!")
                                                key.getchar()
                                                print(
                                                    "\n- Claro, vou procurar ele. Fique aqui")
                                                key.getchar()
                                                print(
                                                    "\nMeia hora depois, Alberanski aparece com Markos. Conto tudo o que aconteceu e entrego todas as provas.")
                                                key.getchar()
                                                print(
                                                    "\n- Uau, nunca esperava algo assim. Fique aqui até que eu resolva isso. Vai demorar alguns dias, tenho que pegá-los de surpresa. ")
                                                key.getchar()
                                                print("\nAlguns dias depois foi anunciada a prisão de Nikolai e o chefe de polícia, Markos conseguiu evidências suficientes para provar a culpa de ambos sobre o assassinato do general, porém após todos os ocorridos eu não estava seguro, alguns companheiros de Nikolai poderiam tentar me caçar, com isso Markos e Alberanski me ajudaram a recomeçar uma nova vida na Alemanha, espero que dê tudo certo")
                                                key.getchar()
                                                acertou03 = True
                                                break
                                            elif resposta03 != respostaCerta03:
                                                print(
                                                    "\nEssa não é a resposta correta, estou ficando sem tempo...")
                                                key.getchar()
                                                tentativa03 = tentativa03 + 1
                                        elif enigma03 == "2":
                                            tentativa03 = tentativa03 + 3
                                            acertou03 = False
                                    key.getchar()
                                    if acertou03 == False:
                                        print("\n- Não consegui, fracassei.")
                                        key.getchar()
                                        print(
                                            "\n- Desculpa por isso. Bem, o que resta agora é fugir. Tenho alguns contatos se você quiser.")
                                        key.getchar()
                                        print("\n- Claro, obrigado")
                                        key.getchar()
                                        print("\nPassei alguns dias escondido na biblioteca de Alberanski enquanto ele falava com seus contatos, com isso consegui documentos novos para começar uma nova vida na Alemanha, porém com toda a polícia e os contatos de Nikolai atras de mim a fuga foi no mínimo conturbada, mas no fim consegui chegar ao meu destino, mas infelizmente não posso dizer o mesmo de Alberanski que acabou sendo baleado na travessia da fronteira com a França")
                                        key.getchar()
                                        break
                    key.getchar()
        elif escolha11 == "2":
            confiarNikolai = confiarNikolai + 20
            key.getchar()
key.getchar()

if confiarNikolai > 10:
    print("\nContinuo esperando na sala por vários minutos até que um alarme de emergência começa a tocar. O que será que está acontecendo?")
    key.getchar()
    print("\nO Delegado e Nikolai entram de repente e correm em minha direção.")
    key.getchar()
    print("\n- Ei, o que está acontecendo?")
    key.getchar()
    print("\n- O filho do sapateiro nos falou tudo. Você está preso sobre suspeita do assassinato do general!")
    key.getchar()
    capturado = True

if capturado == True:
    print("\n26 de dezembro de 1918\n4 dias depois\nSala do interrogatório\n")
    key.getchar()
    print("\n- Acho melhor você confessar logo que é o trabalho para poupar nosso tempo.")
    key.getchar()
    print("\n- Não sou o culpado. Já disse isso. Não tem nem provas contra mim, só a palavra de um alfaiate.")
    key.getchar()
    if incriminado == True:
        print("\n- Mas sabe uma prova que com certeza prova o culpado? ISSO!")
        key.getchar()
        print("\nEle joga um relógio na mesa. Meu relógio. Como ele estava ali? Se bem que… fazia tempo que não via ele, talvez desde… Nikolai!")
        key.getchar()
        print("\n- O sapateiro nos revelou que você contratou ele na noite do assassinato e como garantia que ele não seria preso, você entregou o seu relógio. Como você explica isso?")
        key.getchar()
        print("\n- Isso é um absurdo, eu estava com ele esses dias atrás, mesmo depois do assassinato.")
        key.getchar()
        print("\n- Você tem como provar isso?")
        key.getchar()
        print("\n- Não…")
        key.getchar()
        print("\n- Então é isso, camarada. Você era o único na cena do crime, seu relógio estava com o atirador e temos a palavra dele e do Nikolai")
        key.getchar()
        print("\n- Nikolai? Como assim? Eu estava ajudando ele.")
        key.getchar()
        print("\n- Obra de mestre né? Claro que ele pediu sua ajuda só para ficar perto e você caiu direitinho. Bem, não vou estender o assunto. Vamos levar você de volta para a cela e logo logo não estará mais aqui.")
        key.getchar()
        print("\nSem muitas opções fui culpado pelo assassinato do general e a data de meu julgamento foi marcada.")
        key.getchar()
        print("\nNo dia do julgamento meu advogado de defesa era um dos contatos de Nikolai, o julgamento foi totalmente parcial e unidirecional, recebi a pena de morte")
        key.getchar()
        print("\nCom isso apenas me resta esperar a data da execução, jamais esperei ser traido dessa forma, mas é o que dizem, mantenha os amigos próximos e os inimigos mais próximos ainda, Nikolai pelo visto seguiu esse ditado a risca")
        key.getchar()
    if incriminado == False:
        print("\n- Ok. Você não vai admitir. Então, vamos a julgamento. Você terá direito a um advogado. E tem uma pessoa ali fora doida para te ver.")
        key.getchar()
        print("\nPassa algum tempo e vejo Alberanski entrando.")
        key.getchar()
        print("\n- Você, graças a Deus. Me ajude, por favor!")
        key.getchar()
        print("\n- Ei calma. Vou te ajudar. O General já desconfiava disso tudo, então me deixou provas, preciso da sua habilidade. ")
        key.getchar()
        print("\n- Como assim ele já sabia?")
        key.getchar()
        print("\n- Pois é, ele era um infiltrado. Você tem muitos inimigos, sabia? Era para você estar morto, ele te salvou. ")
        key.getchar()
        print("\nAlberanski me entrega escondido uma caixa trancada. ")
        key.getchar()
        print("\n- Os papéis estão aqui dentro. Faça sua mágica. É um código.")
        key.getchar()
        print("\nCódigo: .--. . --. ---")
        key.getchar()
        tentativa04 = 0
        respostaCerta04 = "Pego"
        acertou04 = False
        while tentativa04 < 3:
            enigma04 = input(
                "1) Eu decifrei o código\n2) Não faço a mínima ideia.\n")
            if enigma04 == "1":
                resposta04 = input("Insira o código decifrado:\n")
                if resposta04 == respostaCerta04:
                    print("\n- Consegui!")
                    key.getchar()
                    print("\nAs provas estavam todas lá. Os seus planos, planejava matar não só a mim como várias outras pessoas importantes. A ideia do poder subiu à cabeça. Ele tinha muitos contatos na polícia, e seus nomes estavam ali também.")
                    key.getchar()
                    print("\nEstava escrito: confie apenas no Markos.")
                    key.getchar()
                    print("\n- Preciso falar com Markos. Me ajude, Alberanski!")
                    key.getchar()
                    print("\n- Claro, vou procurar ele. Fique aqui")
                    key.getchar()
                    print(
                        "\nMeia hora depois, Alberanski aparece com Markos. Conto tudo o que aconteceu e entrego todas as provas.")
                    key.getchar()
                    print("\n- Uau, nunca esperava algo assim. Fique aqui até que eu resolvo isso. Vai demorar alguns dias, tenho que pegá-los de surpresa. Enquanto isso, volte para a cela e finja que nada disso aconteceu. ")
                    key.getchar()
                    print("\nAlguns dias depois foi anunciada a prisão de Nikolai e o chefe de polícia, Markos conseguiu evidências suficientes para provar a culpa de ambos sobre o assassinato do general, após todos os ocorridos eu fui inocentado, porém não estava seguro, alguns companheiros de Nikolai poderiam tentar me caçar, com isso Markos e Alberanski me ajudaram a recomeçar uma nova vida na Alemanha, espero que dê tudo certo")
                    key.getchar()
                    acertou04 = True
                    break
                elif resposta04 != respostaCerta04:
                    print("\nEssa não é a resposta correta, estou ficando sem tempo...")
                    key.getchar()
                    tentativa04 = tentativa04 + 1
            elif enigma04 == "2":
                tentativa04 = tentativa04 + 3
                acertou04 = False
        key.getchar()
        if acertou04 == False:
            print("\n- Não consegui, fracassei.")
            key.getchar()
            print("\n- Desculpa meu amigo, isso era tudo o que eu tinha")
            key.getchar()
            print(
                "\nAlberanski vai embora. Sou levado para a cela. Não há mais nada o que posso fazer. ")
            key.getchar()
            print("\nSem muitas opções fui culpado pelo assassinato do general e a data de meu julgamento foi marcada.")
            key.getchar()
            print("\nNo dia do julgamento meu advogado de defesa era Alberanski, ele argumentou de forma engenhosa e criativa em meu favor, mas todo o juri havia sido comprado por Nikolai, com isso o máximo que Alberanski conseguiu foi trocar a pena de morte pela prisão perpétua")
            key.getchar()
            print("\nMe despedi de Alberanski e com isso começarei meu primeiro dia na prisão, o primeiro de muitos...")
            key.getchar()
key.getchar()

print("\nFIM!")
key.getchar()
print("\nPARABÉNS " + nome + " VOCÊ FINALIZOU O JOGO!")
key.getchar()
key.getchar()
