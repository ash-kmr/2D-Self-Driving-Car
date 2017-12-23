# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:47:23 2017

@author: hp
"""
#importing required libraries
import random 
import os
import numpy as np
import torch
import torch.nn
import torch.autograd as autograd

class NeuralNetwork(torch.nn.Module):
    
    def __init__(self ,n_inputs, n_actions):
        super(NeuralNetwork, self).__init__()
        self.input_size = n_inputs
        self.n_outputs = n_actions
        self.fullyConnected1 = torch.nn.Linear(input_size, 30)
        self.fullyConnected2 = torch.nn.Linear(30, n_actions)
        
    def forwardprop(self, input_param):
        x = torch.nn.functional.leaky_relu(self.fullyConnected1(input_param))
        q = self.fc2(x)
        return q
    
#class for experience replay
class exp_mem():
    def __init__(self, capacity):
        self.cap = capacity
        self.mem = []
         