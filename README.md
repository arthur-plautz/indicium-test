# Indicium Desafio Técnico

# Setup

Para executar o programa, são necessárias algumas tecnologias instaladas:
  - Python v3.6: https://www.python.org/downloads/
  - Pip: https://pip.pypa.io/en/stable/installing/
  - Numpy: https://www.scipy.org/install.html#pip-install

Tendo as tecnologias acima instaladas, navegue até o diretório onde estão os arquivos do programa e execute o comando "python master.py".

# Uso

O programa irá aguardar a entrada de dados para o formato de saída, e para o mês referente à representatividade por setor, para a segunda saída requerida no documento de explanação do desafio técnico.

A primeira entrada de dados deve ser uma string:
  - "Documento": Para receber os arquivos no formato CSV em quatro arquivos distintos, sendo dois oficiais, e dois de subdivisão;
  - "Objeto": Para visualizar a saída de dados referentes às consultas solicitadas;

A segunda entrada de dados deve ser um número, referente ao mês para a filtragem dos resultados por setor.

# Arquitetura

A linguagem Python foi escolhida visto permitir uma objetividade maior quanto à execução das funcionalidades solicitadas. Para auxiliar na conversão dos documentos formato TSV, foi utilizada uma biblioteca nativa de python, 'csv', usada para a manipulação de arquivos do gênero. Também foi utilizada a biblioteca 'Numpy' para a manipulação de matrizes, visto que a conversão dos arquivos para python resulta em matrizes bidimensionais.
A modularidade das funções foi utilizada para a melhor organização do ambiente e melhor coesão das funcionalidades. O modelo de programação escolhido foi a programação funcional, visto não ser um sistema muito complexo de início, e não tendo muitos elementos, de modo que se tornou uma opção mais eficaz dentre outros modelos.

As funções definidas podem ser separadas de acordo com seus módulos: Operações e Conversão; Funções de operação são funcões diretamente ligadas às consultas propostas aos dados disponibilizados, enquanto funções de conversão, visão a conversão dos dados de python para csv e de tsv para python.
A lógica básica utilizada na estrutura das funções é de varredura de matrizes, que chegam à complexidade máxima de matrizes tridimensionais, de modo que as comparações entre valores pontuais resultam na filtragem e separação dos dados de acordo com as consultas propostas.

# Saída de dados

A saída de dados consiste em quatro arquivos principais:
- valor_contato_mes: Esta seria a primeira saída de dados oficial, requerida no documento de explanação do desafio;
- valor_setor: Esta seria a segunda saída de dados oficial, requerida no documento de explanação do desafio;
- valor_contato: A primeira subdivisão da primeira saída oficial;
- valor_mes: A segunda subdivisão da primeira saída oficial;


