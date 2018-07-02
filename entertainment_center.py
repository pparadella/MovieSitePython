import media
import fresh_tomatoes


# criando cada filme chamando a classe movie e passando informacoes
escola_rock = media.Movie("Escola de Rock",
                          "Um filme sobre um músico onde consegue" +
                          "um emprego pra ensinar crianças.",
                          "https://upload.wikimedia.org/wikipedia/pt/thumb/1" +
                          "/1b/Schoolrockposter.jpg/" +
                          "210px-Schoolrockposter.jpg",
                          "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

gladiador = media.Movie("Gladiador",
                        "Um grande general de Roma é transformado em " +
                        "Gladiador e tem que batalhar por sua vida e de Roma.",
                        "https://1.bp.blogspot.com/-gyjFuc5OTpQ/VyIlE_dOrsI/" +
                        "AAAAAAAAXV8/-8Hn4TpVO8kAmIJ-WUboSiUh0ry1nP-bACLcB/" +
                        "s1600/gladiador%2Bposter.jpg",
                        "https://www.youtube.com/watch?v=do9zep1n8cU")

jogos_vorazes = media.Movie("Jogos Vorazes",
                            "A história é estabelecida em um período " +
                            "distópico pós-apocalíptico na nação de " +
                            "Panem, onde garotos e garotas de 12 a " +
                            "18 anos devem participar dos Jogos " +
                            "Vorazes, um evento anual televisionado " +
                            "na qual os 'tributos' precisam lutar " +
                            "até a morte até que sobre apenas um, " +
                            "que é coroado vencedor.",
                            "https://upload.wikimedia.org/wikipedia/" +
                            "pt/4/42/HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=zhW-KWCw92c")

mestre_mares = media.Movie("Mestre dos Mares",
                           "Em 1805, o Capitão Jack Aubreyand e Stephen " +
                           "Maturin são ordenados a perseguir e capturar " +
                           "uma poderosa embarcação francesa na costa da " +
                           "América do Sul. Durante o percurso, o capitão " +
                           "tem que exigir um esforço quase sobrehumano " +
                           "de sua tripulação, exausta e faminta, para " +
                           "poder prosseguir com seu objetivo.",
                           "https://images-na.ssl-images-amazon.com/" +
                           "images/I/51DEBDSPNFL.jpg",
                           "https://www.youtube.com/watch?v=KhNbvIUMaug")

matrix = media.Movie("Matrix",
                     "Thomas A. Anderson vive uma vida dupla. " +
                     "De dia, é um programador para uma companhia " +
                     "de software. De noite é um hacker, invadindo " +
                     "sistemas de computador ilegalmente e roubando " +
                     "informações, sob o apelido de Neo. Durante a " +
                     "sua vida como pirata informático, Neo cruza-se " +
                     "com uma pergunta constante: 'O que é a Matrix?'.",
                     "https://upload.wikimedia.org/wikipedia/pt/c/" +
                     "c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

senhor_aneis = media.Movie("Senhor dos Aneis",
                           "Este filme leva-nos para um mundo onde anéis " +
                           "forjados por anões reinam com o seu poder. No " +
                           "entanto, há um anel que é o mais poderoso de " +
                           "todos e, se cair em mãos erradas, pode ter um " +
                           "poder destrutivo.",
                           "https://vignette.wikia.nocookie.net/terramedia/" +
                           "images/c/cd/LOTR1.jpg",
                           "https://www.youtube.com/watch?v=IUerKBZHnBs")

# colocando os filmes numa array
movies = [escola_rock, gladiador, jogos_vorazes,
          mestre_mares, matrix, senhor_aneis]
# gerando o site a partir dos filmes na array
fresh_tomatoes.open_movies_page(movies)
