#Grokking Deep Learning Chapter 3: 1st neural network
'''
This is a simple neural network maps one data input point to the 
output or prediction. This version of the code uses Numpy library
to improve efficiency

inputs: num_toes := Number of toes on the team
        wlrec := win loss record of the team
        nfans := number of fans presnet at the game 

prediction := likelihood that the team wins or loses
'''

import numpy as np 
weight = np.array([ 0.1, 0.2, 0 ])



def neural_network ( input, weight ):
    '''
    Neural network that predicts where the team will win
    inputs: num_toes := Number of toes on the team
            wlrec := win loss record of the team
            nfans := number of fans presnet at the game 
    output: Prediction := percentage that the team will win the game
    '''
    prediction = input.dot( weight )

    return prediction

num_toes = np.array([ 8.5, 9.5, 9.9 , 9.0 ])
wlrec = np.array([ 0.65, 0.8, 0.8, 0.9 ]) 
nfans = np.array([ 1.2, 1.3, 0.5, 1.0 ])

print( 'inputs := [number of toes, win/loss record and number of fans]' )

for i,toes in enumerate ( num_toes ):
    input = np.array ([ num_toes[ i ], wlrec[ i ], nfans[ i ] ])
    predic = neural_network ( input, weight )
    print ('inputs: ', input, " Prediction: ", predic)