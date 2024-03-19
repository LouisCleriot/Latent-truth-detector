import numpy as np
import torch
import torch.nn as nn   
import torch.nn.functional as F

class AutoAttentionFixeOutput(nn.Module): 
    def __init__(self):
        super(AutoAttentionFixeOutput, self).__init__()
        Dx = 4096
        Nx = 50
        self.Dq = Dx//Nx
        self.WQ = nn.Linear(Dx,self.Dq,bias=False)
        self.WK = nn.Linear(Dx,self.Dq,bias=False)
        self.WV = nn.Linear(Dx,2,bias=False)
    def forward(self, x):
        #x size : 1xvarx4046
        x = x.squeeze(0)
        #x size : varx4046
        x = F.pad(x, (0,0,0,50-x.size(0)))
        #x size : 50x4046
        Q = self.WQ(x) #size : 50xDq
        K = self.WK(x).t() #size : Dqx50
        V = self.WV(x).t() #size : 2x50
        
        e = torch.mm(Q,K)/np.sqrt(self.Dq)
        A = F.softmax(e, dim=1) #size : 50x50
        y = torch.mm(V,A).sum(1)
        return y
        