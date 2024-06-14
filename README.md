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

**Observação:** Meu computador está tendo algum conflito relacionado ao OpenCV, e não estou conseguindo utilizar o VideoWrite para salvar vídeos em minha máquina, todavia o mesmo deve funcionar na hora de executar em sua máquina. 

## Questões teóricas

### Questão 2.1

O método escolhido: YOLOv8 ou CNN funciona da seguinte maneira: primeiramente ele pega a imagem e divide a mesma em uma grid, após isso ele utiliza uma rede neural convolucional para identificar as "caixas", no caso os retângulos que ficam em volta dos objetos detectados, além de gerar um nível de confidência para cada caixa que representa a probabilidade daquilo ser verdadeiro. O diferencial do YOLOv8 é o fato do mesmo extrair informações da imagem com a mesma em diferentes escalas graças a rede neural, o que acaba promovendo uma melhor acurácia. Além disso a mesma apresenta a técnica (NMS) para reduzir confusão na imagem, removendo redundâncias.

### Questão 2.2

A classificação correta seria:

1. CNN
2. Haar Cascade
3. NN Linear
4. Filtros de correlação cruzada


Em termos de se é o ou não possível resolver o problema, o mais prático a ser utilizado é o CNN pois é a melhor opção para detecção de faces. Pois são capazes de aprender padrões complexos e não-lineares, além de serem capazes de generalizar bem para novos dados. além de possuir facilidade de treinamento e implementação levando em conta que para implementar uma CNN, basta apenas utilizar a biblioteca ultralytics e no caso deste projeto, um modelo ja treinado.

Já o Haar Cascade é uma técnica de detecção de objetos que utiliza um classificador em cascata para detectar objetos em imagens ou vídeos. O classificador em cascata é treinado a partir de um grande número de imagens positivas e negativas. O classificador em cascata é composto por vários classificadores em cascata, cada um dos quais é treinado para detectar um padrão específico. O Haar Cascade é eficiente e rápido, mas não é tão preciso quanto as CNNs. Para implementar o mesmo é necessário utilizar a biblioteca OpenCV e um arquivo XML que contém as características do objeto a ser detectado. No quesito de versatilidade e eficiência, o Haar Cascade é uma boa opção para detecção de faces, mas não é tão eficiente quanto as CNNs.

Agora o NN linear é um modelo de rede neural que consiste em uma única camada de neurônios. Cada neurônio é conectado a todos os neurônios da camada de entrada. O NN linear é simples e fácil de implementar, mas não é tão eficiente quanto as CNNs e o Haar Cascade. O NN linear é limitado em sua capacidade de aprender padrões complexos e não-lineares. Para implementar o NN linear, basta utilizar uma biblioteca de Deep Learning como PyTorch ou TensorFlow. No quesito de versatilidade e eficiência, o NN linear não é uma boa opção para detecção de faces, pois é limitado em sua capacidade de aprender padrões complexos e não-lineares.

E o filtro de correlação cruzada é uma técnica de processamento de imagem que é usada para detectar padrões em imagens. O filtro de correlação cruzada é aplicado a uma imagem de entrada e a um filtro de convolução. O filtro de convolução é uma matriz que é deslizada sobre a imagem de entrada para calcular a saída. O filtro de correlação cruzada é eficiente e rápido, mas não é tão preciso quanto as CNNs e o Haar Cascade. Para implementar o filtro de correlação cruzada, basta utilizar uma biblioteca de processamento de imagem como OpenCV. No quesito de versatilidade e eficiência, o filtro de correlação cruzada não é uma boa opção para detecção de faces, pois não é tão preciso quanto as CNNs e o Haar Cascade.

Logo, no tema proposto de identificar faces, o melhor modelo segue sendo o CNN por sua simplicidade e acurácia.

### Questão 2.3

Já, para detecção de emoções, segue abaixo a classificação

1. CNN
2. Haar Cascade
3. NN Linear
4. Filtros de correlação cruzada

O melhor modelo para a detecção de emoções através da imagem de uma face é a CNN, pois ela é capaz de aprender padrões complexos e não-lineares em imagens, o que é essencial para a detecção de emoções. Os outros modelos, como Haar Cascade, NN Linear e filtros de correlação cruzada, são mais simples e não são capazes de aprender padrões complexos em imagens, o que pode limitar sua capacidade de detectar emoções com precisão.

O Haar Cascade é um classificador de objetos em imagens que utiliza características de Haar para detectar objetos. Ele é um modelo simples e eficiente para a detecção de objetos em imagens, mas não é capaz de aprender padrões complexos em imagens, o que pode limitar sua capacidade de detectar emoções com precisão.

O NN Linear por ter uma unica camada de neurônios não é capaz de identificar padrões complexos em imagens, limitando o mesmo da detecção de emoções.

Os filtros de correlação cruzada seguem no mesmo princípio do NN Linear, onde ele não é capaz de identificar padrões complexos em imagens, o que acaba sendo impossível sob a detecção de emoções

### Questão 2.4

As soluções não são capazes de detectar se a pessoa está feliz e isto influenciar no próximo frame. Afim de adicionar isto as soluções, devera aplicar um algoritmo com o `Método Lucas-Kanade` por exemplo que é capaz de rastrear objetos em movimento em uma sequência de frames. Dessa forma, o algoritmo seria capaz de considerar variações de um frame para outro e, assim, detectar faces com maior precisão.

### Questão 2.5

**EL BALON DE OR VAI PARA VINI MALVADEZA JUNIOR O ILUMINADO**


## Autor

Antonio Artimonte Vaz Guimarães