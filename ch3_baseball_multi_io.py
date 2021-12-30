#Grokking Deep Learning 

'''
Multi input and output neural network, used to make predictions
based on baseball team data.

'''



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

def neural_network( input, weights ):

    pred = vector_matrix_mult (input, weights)

    return pred 


weights = ( [ 0.1, 0.1, -0.3 ],  
            [ 0.1, 0.2, 0.0 ],   
            [ 0.0, 1.3, 0.1 ] )  

toes  = [ 8.5,  9.5, 9.9, 9.0 ]
wlrec = [ 0.65, 0.8, 0.8, 0.9 ]
nfans = [ 1.2,  1.3, 0.5, 1.0 ]

for i in range ( len(toes) ):
    input = [ toes[ i ], wlrec[ i ], nfans[ i ] ]
    pred = neural_network( input, weights )
    print ( 'input: ', input, ' Prediction: ', pred )
