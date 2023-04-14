#DnD Neural Network

Este projeto consiste em uma rede neural que aprende sobre o universo do jogo Dungeons and Dragons (DnD) usando a API DnD 5e API. A rede neural é treinada para prever o tipo de monstro a partir de suas características, como o número de pontos de vida, o tipo de dano e as habilidades.

O projeto está organizado nas seguintes pastas:

data: contém o código responsável por carregar e processar os dados da API.
models: contém a definição da rede neural utilizada no projeto.
src: contém os scripts para treinar a rede neural e fazer previsões.
utils: contém funções e utilitários que podem ser usados em outros arquivos do projeto.


#Requisitos

Python 3.6 ou superior
PyTorch 1.7 ou superior
Requests 2.25.1 ou superior

#Como usar

1 - Clone o repositório.:
  git clone https://github.com/seu-usuario/dnd-neural-network.git

2 - Instale as dependências:
  pip install -r requirements.txt

3 - Treine a rede neural
  cd src
    python train.py
    
4 - Faça previsões com a rede neural:
  cd src
    python predict.py
    
#Resultados

Após o treinamento da rede neural, a acurácia alcançada nos dados de teste foi de 80%. Esse resultado pode ser melhorado com mais dados e uma arquitetura mais complexa da rede neural.

#Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.    
