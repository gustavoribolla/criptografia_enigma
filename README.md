# Criptografia usando Enigma

## Introdução:

O projeto consiste na criação de uma API Rest e de uma biblioteca de criptografia usando a Enigma.

A Enigma foi uma máquina eletromecânica de criptografia criada por Alan Turing durante a Segunda Guerra Mundial que criptografava as mensagens que eram transmitidas para que os aliados não conseguissem nenhuma informação caso as interceptassem. A quebra da Enigma e as informações obtidas com isso são dois dos grandes fatores que levaram ao fim da guerra em 1945 e foi um dos marcos mais importantes da história da computação, fazendo Alan Turing ser considerado um dos pais da Computação.

## Implementação:

1. Certifique-se de ter o python instalado em seu computador;<br>
2. Clone esse repositório para algum lugar de sua máquina;<br>
3. Instale as bibliotecas necessárias contidas no arquivo "requirements.txt" através do comando "pip install -r requirements.txt".<br>

## Funções e Equações:

### 1. Para One Hot:

Criação de uma matriz identidade 26x26 (alfabeto_matriz) usando np.eye;<br>
Iteração sobre cada caractere da mensagem (msg) e busca do índice correspondente no alfabeto;<br>
Construção de uma matriz (msg_matriz) contendo os vetores correspondentes a cada caractere da mensagem;<br>
Retorna matriz.

### 2. Para String: 

Iteração sobre as colunas da matriz M;<br>
Para cada coluna, itera sobre as linhas e verifica se o valor é 1;<br>
Para cada valor 1 encontrado, adiciona a letra correspondente do alfabeto à string;<br>
Retorna mensagem em string.

### 3. Cifrar: 

Chama para_one_hot() para converter a mensagem em uma representação matricial;<br>
Realiza o produto de matriz entre a matriz de codificação P e a matriz da mensagem;<br>
Converte a matriz cifrada em uma string usando para_string();<br>
Retorna palavra cifrada.

### 4. Decifrar: 

Calcula a inversa da matriz de codificação P usando np.linalg.inv();<br>
Chama para_one_hot() para converter a mensagem em uma representação matricial;<br>
Realiza o produto de matriz entre a inversa da matriz P e a matriz da mensagem;<br>
Converte a matriz decifrada em uma string usando para_string();<br>
Retorna palavra original.

### 5. Enigma: 

Chama para_one_hot() para converter a mensagem em uma representação matricial;<br>
Inicializa a matriz da mensagem cifrada como a matriz da mensagem original.

Para cada coluna na matriz da mensagem cifrada, realiza o seguinte:<br>
Calcula a matriz resultante da multiplicação entre P e a matriz da mensagem cifrada;<br>
Atualiza a coluna da matriz da mensagem cifrada com os valores da matriz resultante;<br>
Multiplica a matriz de codificação P pela matriz de embaralhamento E;<br>
Converte a matriz da mensagem cifrada em uma string usando para_string();<br>
Retorna palavra cifrada.

### 6. De_Enigma: 

Calcula as inversas das matrizes de codificação P e de embaralhamento E usando np.linalg.inv();<br>
Chama para_one_hot() para converter a mensagem em uma representação matricial;<br>
Inicializa a matriz da mensagem decifrada como a matriz da mensagem original.

Para cada coluna na matriz da mensagem decifrada, realiza o seguinte:<br>
Calcula a matriz resultante da multiplicação entre a inversa de P e a matriz da mensagem decifrada;<br>
Atualiza a coluna da matriz da mensagem decifrada com os valores da matriz resultante;<br>
Multiplica a matriz inversa de P pela matriz inversa de E;<br>
Converte a matriz da mensagem decifrada em uma string usando para_string();<br>
Essas são as operações matriciais realizadas em cada função do código;<br>
Retorna palavra original.


## Arquivo Demo:

Arquivo separado por inputs, que chama as funções feitas no arquivo "functions.py" para poder testar com precisão.
 
1. Rode o arquivo "demo.py"<br>
2. Escolha uma opção, entre: Cifra Simples, Cifra Enigma, Decifra Simples, Decifra Engima e Sair, respectivamente.<br>
3. Escreva o número da opção que deseja testar e em seguida, a palavra escolhida.

## API:

Execute o arquivo Python para iniciar o servidor Flask e com o servidor em execução, você pode testar os endpoints da API. Você pode fazer isso usando ferramentas como cURL, Postman ou até mesmo escrevendo um pequeno script Python para enviar solicitações HTTP.

## Rotas:

### 1. Inicial:
Através da rota ('/'), retorna 200 se a API estiver funcionamento.

### 2. Cifrar:
Através da rota ('/cifra'), método POST que devolve, dado uma palavra, sua forma cifrada.

### 3. Decifrar:
Através da rota ('/decifra'), método POST que devolve, dado uma palavra cifrada, sua forma decifrada.

### 4. Enigma:
Através da rota ('/enigma'), método POST que devolve, dado uma palavra, sua forma Enigma.

### 5. De Enigma:
Através da rota ('/de_enigma'), método POST que devolve, dado uma palavra formato Enigma, sua forma original.

## Biblioteca Python:
Para que as funções criadas possam ser utilizadas por outros programdores, as disponibilazamos como uma biblioteca. Para utilizar a biblioteca basta instala-la com o seguinte código:

```
pip install codificador-de-matrizes-rafaela-ribolla==0.0.1
```
E então importar a biblioteca no arquivo, o que pode ser feito pelo código:
```
import codificador-de-matrizes-rafaela-ribolla
```

## Referências:
1. [ChatGPT](https://chat.openai.com/) para saciar dúvidas relacionadas ao desenvolvimento;<br>
2. [Site Horizontes](https://horizontes.sbc.org.br/index.php/2016/11/alan-turing-e-a-enigma/) para pesquisa da Enigma de Alan Turing;
3. [Site Medium](https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14) para pesquisa sobre publicação da biblioteca;
4. [Site Clickup](https://doc.clickup.com/36904728/d/h/1367rr-543/246df89507b2ab3) para pesquisa sobre publicação da biblioteca;;

## Equipe:
Projeto desenvolvido por Gustavo Colombi Ribolla e Rafaela Aférri.