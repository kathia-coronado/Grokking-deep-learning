#Grokking Deep Learning Chapter 3: 1st neural network
'''
This is a simple neural network maps one data input point to the 
output or prediction.

inputs: num_toes := Number of toes on the team
        wlrec := win loss record of the team
        nfans := number of fans presnet at the game 

prediction := likelihood that the team wins or loses
'''
weight = [ 0.1, 0.2, 0 ] 

def wt_sum (inp, wt):
    '''    
    function computes the weighted sum or dot product  of the 
    inputs with the weights.
    
    inpura : wt := list of the weights of the system 
             inp := list of the inputs of the system 
    '''
    assert ( len ( wt ) == len ( inp ) )

    output = 0 

    for i in range ( len ( wt ) ):
        output += wt[ i ] * inp[ i ]

    return output

def neural_network ( input, weight ):
    '''
    Neural network that predicts where the team will win
    inputs: num_toes := Number of toes on the team
            wlrec := win loss record of the team
            nfans := number of fans presnet at the game 
    output: Prediction := percentage that the team will win the game
    '''
    prediction = wt_sum( input, weight )

    return prediction

num_toes = [ 8.5, 9.5, 9.9 , 9.0 ]
wlrec = [ 0.65, 0.8, 0.8, 0.9 ] 
nfans = [ 1.2, 1.3, 0.5, 1.0 ]

print( 'inputs := [number of toes, win/loss record and number of fans]' )

for i,toes in enumerate ( num_toes ):
    input = [ num_toes[ i ], wlrec[ i ], nfans[ i ] ]
    predic = neural_network ( input, weight )
    print ('inputs: ', input, " Prediction: ", predic)