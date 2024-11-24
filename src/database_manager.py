import json
import numpy as np

class Database:
    def __init__(self, path='config/face_database.json'):
        self.path = path
        self.data = self.load()
    
    def load(self):
        try:
            with open(self.path, 'r') as f:
                return json.load(f)
        except:
            return {'faces': []}
    
    def save(self, name, encoding):
        face = {
            'name': name,
            'encoding': encoding.tolist()
        }
        self.data['faces'].append(face)
        
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def get_all_faces(self):
        return [(np.array(f['encoding']), f['name']) 
                for f in self.data['faces']]