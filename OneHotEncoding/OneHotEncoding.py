import numpy as np

class OneHotEncoder:
    def OneHotEncoder1D(self, data):
        '''
        Takes inpue a 1d numpy array and outputs the oneHotEncoding of it
        '''
        #find number of levels
        levels = np.unique(data)
        no_level = len(levels)
        no_rows = len(data)
        print no_rows
        out = np.zeros((no_rows, no_level))

        level_mapping = dict()
        i = 0
        k = 0
        while(i < no_rows):
            if(data[i] in level_mapping):
                out[i][level_mapping[data[i]]] = 1
            else:
                level_mapping[data[i]] = k
                out[i][k] = 1
                k += 1
            i += 1
        return out

    def encode(self, data):
        '''
        Expects a numpy ndarray
        '''
        num_of_features = data.shape[1]
        out = np.zeros((data.shape[0],1))
        i = 0
        while(i < num_of_features):
            out = np.hstack( (out, self.OneHotEncoder1D(data[:,i])) )
            i += 1

        return out[:, 1:]
