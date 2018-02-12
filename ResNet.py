import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

class ResidualNet(nn.Module):
	def __init__(self):
		super(ResidualNet, self).__init__()
		# Conolutions Layers
		self.conv1 = nn.Conv2d(in_channels = 3, out_channels = , kernel_size = 3)
		self.conv2 = nn.Conv2d(in_channels = , out_channels = , kernel_size = 3)
		self.pool = nn.MaxPool2d(kernel_size = stride = 1)
		self.conv3 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv4 = nn.Conv2d(n_channels = , out_channels = , kernel_size = )
		
		# CLassifier
		self.fc1 = nn.Linear()
		self.fc2 = nn.Linear()
		self.fc3 = nn.Linear()
		
	def forward(self, x):
		# Feature extraction
		x = self.pool(F.relu(self.conv2(self.conv2(x))))
		x = self.pool(F.relu(self.conv4(self.conv3(x))))
		
		# Classification
		x = x.view()
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x
