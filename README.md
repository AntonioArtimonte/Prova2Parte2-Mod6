# Introdução

No projeto, foi utilizado o modelo YOLOv8 já treinado para detectar faces, o mesmo pode ser acessado clicando [aqui](https://github.com/derronqi/yolov8-face), após isto, o mesmo infere sob cada frame do vídeo e adicionar sob os frames os retângulos nos locais onde o mesmo identificou faces.

## Instruções de Execução

Afim de inicializar o projeto de detecção de rostos no vídeo do Messi, basta fazer os seguintes passos:

1. 

Checar instalação do python e versão

```bash
python3 --version
```

Ou

```bash
python --version
```

Se o mesmo retornar python não existe ou algo do tipo, instale o python de acordo com seu S.O, caso retornar, porém retornar uma versão menor que python3.11, deve-se instalar a versão do python3.11 afim de baixar a biblioteca do ultralytics.

2. 

Inicializar o ambiente virtual do python

```bash
cd Prova

python3 -m venv venv
```

3. Instalar as depêndencias

```bash
python3 -m pip install -r requirements.txt
```

ou

```bash
python -m pip install -r requirements.txt
```

4. Rodar o arquivo principal

```bash
python3 main.py
```

ou

```bash
python main.py
```

## Vídeo mostrando o funcionamento

Afim de avaliar o funcionamento, segue abaixo um vídeo utilizado para representar o mesmo

[Vídeo](https://drive.google.com/file/d/1DHaXqLLBNSyhgxtY0Htlb5Y9RZpdfptP/view?usp=sharing)

## Questões teóricas

### Questão 2.1

O método escolhido: YOLOv8 ou CNN funciona da seguinte maneira: primeiramente ele pega a imagem e divide a mesma em uma grid, após isso ele utiliza uma rede neural convolucional para identificar as "caixas", no caso os retângulos que ficam em volta dos objetos detectados, além de gerar um nível de confidência para cada caixa que representa a probabilidade daquilo ser verdadeiro. O diferencial do YOLOv8 é o fato do mesmo extrair informações da imagem com a mesma em diferentes escalas graças a rede neural, o que acaba promovendo uma melhor acurácia. Além disso a mesma apresenta a técnica (NMS) para reduzir confusão na imagem, removendo redundâncias.

### Questão 2.2

A classificação correta seria:

1. CNN
2. Haar Cascade
3. NN Linear
4. Filtros de correlação cruzada


Em termos de se é o ou não possível resolver o problema, o mais prático a ser utilizado é o CNN, ele requer um treinamento afim de identificar os objetos/faces, todavia ele acaba no fim apresentando uma acurácia muito melhor. Todavia para treinar o mesmo requer um alto poder de processamento, logo, se já possui um modelo dele treinado, é o melhor a se utilizar, todavia se é necessário treinar um novo modelo, ele pode requerer certo poder de processamento. O mesmo possui facil implementação e possui uma alta versatilidade, levando em conta que é facil de treinar o mesmo com um dataset novo.

Já o Haar Cascade, possui uma acurácia OK, e é facilmente executável, ou seja, não requer muito poder de processamento, levando em consideração que ele não necessita ser treinado, apenas aperfeiçoado através dos seus parâmetros como o `MinNeighbours` e `Scale`. Logo, para resolver o problema de detecção de faces que não requer uma acurácia muito boa, ele é muito bom, por apresentar uma facil implementação, porém a versatilidade do mesmo é complexo, levando em conta que para detectar outros objetos, ele pode apresentar certa dificuldade ao treinamento.

O NN Linear possui uma baixa viabilidade, levando em conta suas limitações para detecções de objetos. Além de possuir uma baixa facilidade de implementação, levando em conta que são bibliotecas do python de difícil utilização, além de possuir uma baixa versatilidade graças a suas limitações

O Filtro de correlação cruzada, também possui várias limitações devido a sua simplicidade. Para implementar o mesmo é necessário ter um alto conhecimento técnico, além de possuir baixa versatilidade comparado aos outros 3.

Logo, no tema proposto de identificar faces, o melhor modelo segue sendo o CNN por sua simplicidade e acurácia.

### Questão 2.3

Já, para detecção de emoções, segue abaixo a classificação

1. CNN
2. Haar Cascade
3. NN Linear
4. Filtros de correlação cruzada

A classificação segue a mesma pois, como dito anteriormente, o CNN é o melhor modelo para se utilizar afim de importar novos datasets, ou criar soluções com pesos novos.

O Haar Cascade necessitaria de grandes modificações afim de adicionar a representação de emoções, além de possuir uma acurácia ainda menor. Provocando uma dificuldade de implementação.

Já as outras duas soluções NN Linear e os Filtros de correlação cruzada simplesmente são simples demais para utilização na detecção de emoções, o que provocaria em muitos Falsos Positivos, não sendo adequados para o problema.

### Questão 2.4

As soluções não são capazes de detectar se a pessoa está feliz e isto influenciar no próximo frame. Afim de adicionar isto as soluções, seria possível realizar um sistema de dicionário com as emoções, como por exemplo:

```python
emotions = {
    feliz: 1,
    normal: 2,
    bravo: 3
}
```

Após isto, seria possível adicionar pesos a cada uma das emoções e analisar, se de um frame para o outro as mesmas tiveram uma mudança muito brusca em relação ao frame passado, e se isto de fato ocorreu, alterar o resultado para uma média entre o valor do frame antigo e o valor do frame atual. Assim sendo, adicionando um sistema de influenciação. Onde dependendo do tamanho da variação, será utilizado uma emoção diferente.


### Questão 2.5

**EL BALON DE OR VAI PARA VINIUS MALVADEZA JUNIOR**

## Autor

Antonio Artimonte Vaz Guimarães