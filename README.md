# Sobre
Esse é um site sobre filmes que é gerado automaticamente através de código escrito em python.


## Pré-Requisitos
- [Python 2.7.9](https://www.python.org/downloads/release/python-279)
- [Chrome Browser](https://www.google.com/chrome)


## Gerando o site
1. Clone esse repositório para o seu pc.

2. Abra o IDLE do Python 2.7.9 e mande abrir o documento `entertainment_center.py`

3. Com o arquivo aberto no IDLE mande rodar no menu `Run` > `Run Module`
   >Ele irá gerar um arquivo fresh_tomatoes.html na sua pasta e irá 
   >abrir o arquivo automaticamento no seu browser padrão.

obs: Se você mudar as classes ou as informações passadas nas classes e mandar rodar novamente
     será gerado um novo `.html` com as mudanças.
     
   Classe Movie para o filme Mestre dos Mares:
    
```python
     mestre_mares = media.Movie("Mestre dos Mares",
                           "Em 1805, o CapitÃ£o Jack Aubreyand e Stephen " +
                           "Maturin sÃ£o ordenados a perseguir e capturar " +
                           "uma poderosa embarcaÃ§Ã£o francesa na costa da " +
                           "AmÃ©rica do Sul. Durante o percurso, o capitÃ£o " +
                           "tem que exigir um esforÃ§o quase sobrehumano " +
                           "de sua tripulaÃ§Ã£o, exausta e faminta, para " +
                           "poder prosseguir com seu objetivo.",
                           "https://images-na.ssl-images-amazon.com/" +
                           "images/I/51DEBDSPNFL.jpg",
                           "https://www.youtube.com/watch?v=KhNbvIUMaug")
```
     
 ## Outras Informações
  O arquivo `media.py` contém a declaração da classe Movie e o arquivo `fresh_tomatoes.py` 
  contém o código onde gera o html automáticamente passando os filmes para ele.
