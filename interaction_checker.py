python
import json
from config import Config
class InteractionChecker:
    def init(self):
        with open(Config.INTERACTIONS_PATH, 'r') as f:
            data = json.load(f)
            self.interactions = data['interactions']
    
    def check(self, medications):
        warnings = []
        drug_names = [m['info']['name_en'] if 'name_en' in m['info'] 
                     else m['info']['name'] for m in medications]
        
        for i in range(len(drug_names)):
            for j in range(i+1, len(drug_names)):
                for interaction in self.interactions:
                    if (interaction['drug1'].lower() == drug_names[i].lower() and 
                        interaction['drug2'].lower() == drug_names[j].lower()) or \
                       (interaction['drug1'].lower() == drug_names[j].lower() and 
                        interaction['drug2'].lower() == drug_names[i].lower()):
                        warnings.append({
                            'drugs': [drug_names[i], drug_names[j]],
                            'severity': interaction['severity'],
                            'description': interaction['description']
                        })
        
        return warnings
