import torch
import torch.nn as nn
from typing import Tuple

class IntentNet(nn.Module):
    """
    Simple neural network untuk intent classification.
    
    Architecture:
        Input -> Linear(input_size, 64) -> ReLU -> Linear(64, num_classes) -> Output
    """
    
    def __init__(self, input_size: int, num_classes: int):
        """
        Args:
            input_size: Vocabulary size
            num_classes: Number of intent classes
        """
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Dropout(0.2),  # Add dropout untuk regularization
            nn.Linear(64, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor of shape (batch_size, input_size)
        
        Returns:
            Logits tensor of shape (batch_size, num_classes)
        """
        return self.net(x)
