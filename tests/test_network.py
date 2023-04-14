import torch
import numpy as np
from models.neural_network import MyNeuralNetwork

def test_network():
    # Definir parâmetros da rede neural
    input_size = 3
    hidden_size = 5
    output_size = 1

    # Criar rede neural
    net = MyNeuralNetwork(input_size, hidden_size, output_size)

    # Testar a rede neural com dados de exemplo
