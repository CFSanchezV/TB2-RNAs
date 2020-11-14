import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

#Entradas 
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
#Salidas reales
expected_output =np.array([[0],[1],[1],[0]])

#epocas
epochs=10000

#factor de aprendizaje
lr=0.25

#Neuronas de capa entrada a coger // capa oculta //Capa salida
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons=2,2,1

#Pesos aleatorios para la capa oculta
hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))

#Pesos aleatorios para umbral bias de la capa oculta
#(una entrada mas que se le considera a la neurona en la capa oculta)
hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))

#Pesos para la capa salida
output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))

#Pesos aleatorios para umbral bias de la capa salida
output_bias = np.random.uniform(size=(1,outputLayerNeurons))

for _ in range(epochs):
	#Forward Propagation
	hidden_layer_activation = np.dot(inputs,hidden_weights)
	hidden_layer_activation += hidden_bias
	hidden_layer_output = sigmoid(hidden_layer_activation)

	output_layer_activation = np.dot(hidden_layer_output,output_weights)
	output_layer_activation += output_bias
	predicted_output = sigmoid(output_layer_activation)

	#Backpropagation
	error = expected_output - predicted_output
	d_predicted_output = error * sigmoid_derivative(predicted_output)
	
	error_hidden_layer = d_predicted_output.dot(output_weights.T)
	d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

	#Updating Weights and Biases
	output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
	output_bias += np.sum(d_predicted_output) * lr
	hidden_weights += inputs.T.dot(d_hidden_layer) * lr
	hidden_bias += np.sum(d_hidden_layer) * lr

    
print("Pesos finales: ")
print(hidden_weights)
print("bias finales: ")
print(hidden_bias)
print("Pesos finales capa de salida: ")
print(output_weights)
print("bias finales capa de salida: ")
print(output_bias)

print("\n Predicción : ")
print(predicted_output)