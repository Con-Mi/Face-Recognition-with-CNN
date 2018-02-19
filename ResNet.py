import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

class ResidualNet_14(nn.Module):
	def __init__(self):
		super(ResidualNet, self).__init__()
		# Conolutions Layers
		self.conv1 = nn.Conv2d(in_channels = 3, out_channels = , kernel_size = 3)
		self.conv2 = nn.Conv2d(in_channels = , out_channels = , kernel_size = 3)
		
		self.pool = nn.MaxPool2d(kernel_size = 2, stride = 2)
		
		self.conv3 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv4 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
		self.conv5 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv6 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
		self.conv7 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv8 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
		self.conv9 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv10 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
		self.conv11 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv12 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
		self.conv13 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		self.conv14 = nn.Conv2d(in_channels = , out_channels = , kernel_size = )
		
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
