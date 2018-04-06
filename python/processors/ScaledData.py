from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler

class Standardize(TransformerMixin):
  """Standardizing the Data"""
  
  
  def fit(self, X, y= None):
    return self
    
    
  def transform(self, X, y = None):
    scaler = StandardScaler()
    scaled_data = scaler.transform(X)
    return scaled_data
    
   
