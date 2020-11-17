import pandas as pd
import numpy as np

# --------------------------------TRAINED NEURAL NET DATA-------------------------------------

trained_activations = [np.array([[-0.364402, -1.86106,  0.644491, -0.070859,  1.,  0.,
                                  1.,  0.,  0.]]),
                       np.array([[0.9875525, 0.88008342, 0.02839811, 0.99564306, 0.99592818,
                                  0.21442287, 0.9937713, 0.98781454, 0.50631533]]),
                       np.array([[1.56023348e-04, 3.81342998e-03, 9.96371288e-01]])]

trained_weights = [np.array([[-3.37971049, -0.61816954, -0.16241541,  4.76223218,  4.63981161,
                              -3.19517451,  4.32307045, -0.10763092,  0.83961083],
                             [0.63560599,  0.2648269,  1.94940882, -2.619836, -2.70713842,
                              1.80218476, -2.36600391, -1.88822734,  0.40891955],
                             [0.45793873,  0.23139682, -1.6495256,  0.48928713,  0.40057207,
                              0.34982515,  0.58040054,  1.84866072, -0.14027218],
                             [2.04246248,  0.90160015, -1.62194568, -0.02228814,  0.07912638,
                              0.36727169, -0.15364671,  1.73044273,  0.20291316],
                             [1.19338278,  0.99679496,  0.77220602,  1.61168965,  1.32894253,
                              -0.27248938,  1.08537906, -0.5553534,  0.79148492],
                             [1.69760456,  0.70086895,  0.90418925, -0.26934511, -0.26322964,
                              0.19349631, -0.5485062, -0.8835138,  0.42654247],
                             [2.98124441,  1.17877522,  0.21212751,  0.36270433,  0.57069393,
                              0.96423212,  0.77407126,  0.32845229,  0.40553981],
                             [-0.57321083,  0.14239956,  1.07546772,  1.37482568,  1.58041382,
                              -0.52783021,  1.64797556, -1.48997094,  1.14889076],
                             [1.32225693,  0.80724207,  1.17617055, -0.79240847, -0.41698983,
                              0.66076064, -0.11697339,  0.31778831,  0.68631277]]),
                   np.array([[3.20800405, -5.94732906,  0.78753571],
                             [0.47555428, -2.49113834, -0.41179534],
                             [2.5003609,  1.81313074, -5.21773288],
                             [-4.05916794,  3.17866956,  0.20001304],
                             [-4.22035513,  2.86735828,  0.44374326],
                             [3.19268485, -2.65035136, -1.20377782],
                             [-3.30499473,  2.95508469,  0.80575194],
                             [-1.40617493, -5.59718104,  4.88702026],
                             [-0.37414805, -0.81193384, -1.30959131]])]

def sigmoid(x):
    y = 1.0 / (1 + np.exp(-x))
    return y

def sigmoid_derivative(x):
    return x * (1.0 - x)

def forward_propagate_input(X_input):
    activations = X_input
    trained_activations[0] = activations

    # iterate through the network layers
    for i, w in enumerate(trained_weights):
        net_inputs = np.dot(activations, w)

        activations = sigmoid(net_inputs)
        # i+1: because activation = input of next neuron
        trained_activations[i + 1] = activations

    return activations


# ---------------------------------PRE-PROCESS INPUT------------------------------------

# Convert to dictionary with labels so it can be sent to dataframe
def first_process(input_list):
    # input_list = ['Biscoe','42','13.5','210','4150','femenino']  # -> Es un Gento -> [0, 0, 1]
    labels = ['island', 'bill_length_mm', 'bill_depth_mm',
              'flipper_length_mm', 'body_mass_g', 'sex']
    dict_data = dict()
    for i, _ in enumerate(zip(input_list, labels)):
        dict_data[labels[i]] = input_list[i]

    return dict_data


# Convert to dataframe from dictionary and rollback to original english labels
def second_process(dict_data):
    pd_data_oriented = pd.DataFrame.from_dict(dict_data, orient='index')
    pd_data = pd_data_oriented.transpose()
    pd_data['sex'].replace(['Femenino', 'Masculino'], [
                           'female', 'male'], inplace=True)

    return pd_data


# Encode one hot
def third_process(pd_data):
    df_input = pd_data.copy()
    encode = ['sex', 'island']

    for col in encode:
        dummy = pd.get_dummies(df_input[col], prefix=col)
        df_input = pd.concat([df_input, dummy], axis=1)
        del df_input[col]

    return df_input


# Add missing columns and fill with 0s
def add_extra_cols(df):
    labels = ['sex_female', 'sex_male', 'island_Biscoe',
              'island_Dream', 'island_Torgersen']
    dict_data = dict()
    for label in labels:
        if label not in df.columns:
            dict_data[label] = 0
            mock_df = pd.DataFrame.from_dict(
                dict_data, orient='index').transpose()
            new_df = pd.concat([df, mock_df], axis=1)

    return new_df


# Rearrange columns y normalize
def rearrange_normalize(df_final):    
    df_numbers = df_final.filter(['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
    df_genders = df_final.filter(['sex_female', 'sex_male'])
    df_islands = df_final.filter(['island_Biscoe', 'island_Dream', 'island_Torgersen'])

    # Normalize number data with mean and std from original dataset
    means = [43.992793, 17.164865, 200.966967, 4207.057057]
    stds = [5.468668, 1.969235, 14.015765, 805.215802]

    # Manually normalize each value in row
    for i, col in enumerate(list(df_numbers.columns)):
        normal_data = float(df_numbers.at[0, col])
        # normalize and round
        normal_data = round((normal_data - means[i]) / stds[i], 6)
        df_numbers.at[0, col] = str(normal_data)

    # Rejoin separated columns to the right side in proper order (same as training input format)
    formatted_df = pd.concat([df_numbers, df_genders], axis=1)
    formatted_df = pd.concat([formatted_df, df_islands], axis=1)

    return formatted_df


# -------------------------------Process all input--------------------------------------
def process_all_input(input_list):
    first = first_process(input_list)    
    second = second_process(first)    
    third = third_process(second)    
    df_final = add_extra_cols(third)
    
    arranged_df = rearrange_normalize(df_final)
    
    # Define test input in numpy array
    X_input = arranged_df.to_numpy(dtype='float', copy=True)
    
    # Ask for the NN prediction
    predicted_output = forward_propagate_input(X_input)
    
    # Aplicando redondeo a resultados de predicción:
    rounded_predicted_output = np.around(predicted_output, 1).copy()
        
    # print(rounded_predicted_output)
    print("Output is:")
    print("Adelie = [1, 0, 0]", '||',
          "Chinstrap = [0, 1, 0]", '||', "Gento = [0, 0, 1]")
    
    lst = rounded_predicted_output.tolist()
    
    for elem in lst:
        if elem == [1.0, 0.0, 0.0]:
            return 1
        elif elem == [0.0, 1.0, 0.0]:
            return 2
        elif elem == [0.0, 0.0, 1.0]:
            return 3
        else:
            return -1