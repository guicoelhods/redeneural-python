# models/dnd_neural_network.py
import torch
import torch.nn as nn
import torch.optim as optim

class DndNeuralNetwork(nn.Module):
    """
    Classe da rede neural para o aprendizado de dados do DnD.
    """
    def __init__(self, input_size, hidden_size, output_size):
        """
        Construtor da rede neural.

        Args:
            input_size (int): Número de neurônios na camada de entrada.
            hidden_size (int): Número de neurônios na camada oculta.
            output_size (int): Número de neurônios na camada de saída.
        """
        super(DndNeuralNetwork, self).__init__()

        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        """
        Método forward da rede neural.

        Args:
            x (torch.Tensor): Tensor de entrada.

        Returns:
            torch.Tensor: Tensor de saída.
        """
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.softmax(out)
        return out

def train_dnd_neural_network(model, dataloader, optimizer, criterion, num_epochs):
    """
    Função para treinar a rede neural.

    Args:
        model (nn.Module): Instância da rede neural a ser treinada.
        dataloader (DataLoader): Instância do DataLoader contendo os dados de treinamento.
        optimizer (torch.optim.Optimizer): Otimizador para atualizar os pesos da rede neural.
        criterion (torch.nn.modules.loss._Loss): Função de perda para avaliar a precisão da rede neural.
        num_epochs (int): Número de épocas para treinamento.

    Returns:
        nn.Module: Instância da rede neural treinada.
    """
    for epoch in range(num_epochs):
        for data in dataloader:
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs.float())
            loss = criterion(outputs, labels.long())
            loss.backward()
            optimizer.step()

    return model
