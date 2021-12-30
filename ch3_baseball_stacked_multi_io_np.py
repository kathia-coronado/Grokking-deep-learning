#Grokking Deep Learning 
'''
Multiple input and output stacked neural network (NN). In this 
NN, there are two set of weights: 
ih_wgt := weights that map the inputs to the hidden layer
hp_wgt := weights that map the hidden layer to the prediction or
          output layer 

Stacking networks allows for the output of one network to be fed 
as the input to another network. 

'''
import numpy as np 

def w_sum (inp, wt):
    '''    
    function computes the weighted sum or dot product  of the 
    inputs with the weights.
    
    inpura : wt := list of the weights of the system 
             inp := list of the inputs of the system 
    '''
    assert ( len ( inp ) == len ( wt ) )

    output = 0 

    for i in range ( len ( inp) ):
        output += wt[ i ] * inp[ i ]

    return output

def vector_matrix_mult (vec, matrix ):
    
    assert ( len( vec ) == len( matrix ) )

    output = [ None ] * len( vec )

    for i in range ( len( vec ) ):
        output[ i ] = w_sum ( vec, matrix[ i ] )

    return output

def  neural_network ( input, weights ):
    '''
    Neural network first makes one prediction at the hidden layer using 
    one set of weights and then feeds this prediction as the input to 
    another prediction operation using a second set of weights. 

    Inputs: input := datainputs describing one of the baseball games
            weights := system weights that map the inputs to the outputs
    '''
    hid = input.dot( weights[ 0 ] )
    pred = hid.dot( weights[ 1] )
    return hid

# weights tht map the inputs to hidden later  
ih_wgt = np.array([ [0.1, 0.2, -0.1],
           [-0.1, 0.1, 0.9],
           [0.1, 0.4, 0.1]])

# weights that map the hidder later to the predictions
hp_wgt = np.array([ [0.3, 1.1, -0.3 ],
           [0.1, 0.2, 0.0 ],
           [0.0, 1.3, 0.1 ]])

weights = [ih_wgt, hp_wgt]

toes  = np.array([ 8.5,  9.5, 9.9, 9.0 ])
wlrec = np.array([ 0.65, 0.8, 0.8, 0.9 ])
nfans = np.array([ 1.2,  1.3, 0.5, 1.0 ])

for i in range ( len (toes) ):
    inputs = np.array([toes[ i ], wlrec[ i ], nfans[ i ]])
    pred = neural_network(inputs, weights)
    print( 'Inputs: ', inputs, " Predictions: ", pred)