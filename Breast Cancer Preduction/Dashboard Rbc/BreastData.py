import pandas as pd



class dataset:
    def __init__(self) -> None:
         self.data = pd.read_csv("data.csv")

    
    @property
    def remove_id_unnamed(self):  
        columns = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 
        'smoothness_mean', 'compactness_mean', 'concavity_mean','concave points_mean', 'symmetry_mean',
        'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se','fractal_dimension_se', 
        'radius_worst', 'texture_worst','perimeter_worst', 'area_worst', 'smoothness_worst','compactness_worst', 
        'concavity_worst', 'concave points_worst','symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
        self.data = self.data[['diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean','concave points_mean', 'symmetry_mean', 'radius_se', 
        'perimeter_se', 'area_se','compactness_se', 'concavity_se', 'concave points_se', 
         'radius_worst', 'texture_worst','perimeter_worst', 'area_worst', 
        'smoothness_worst','compactness_worst', 'concavity_worst', 'concave points_worst','symmetry_worst',
         'fractal_dimension_worst']]

        return self.data.head()


    @property
    def Target(self):
        Target = self.data['diagnosis'].value_counts()
        Count_Target = self.data['diagnosis'].value_counts
        return Target,Count_Target 

    @property
    def Corr_graph(self): 
        corr = self.data.corr () 
        corr.style.background_gradient(cmap='coolwarm') 
        return corr

       