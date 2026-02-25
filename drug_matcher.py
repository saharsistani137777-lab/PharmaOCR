python
import pandas as pd
from fuzzywuzzy import fuzz, process
from config import Config

class DrugMatcher:
    def init(self):
        self.drugs_fa = pd.read_csv(Config.DRUGS_FA_PATH)
        self.drugs_en = pd.read_csv(Config.DRUGS_EN_PATH)
        self.drug_names = list(self.drugs_fa['name_fa']) + list(self.drugs_fa['name_en'])
        self.drug_names = list(set([str(n).lower() for n in self.drug_names]))
    
    def match_drugs(self, text):
        text_lower = text.lower()
        words = text_lower.split()
        found_drugs = []
        
        for word in words:
            match, score = process.extractOne(
                word, 
                self.drug_names,
                scorer=fuzz.ratio
            )
            
            if score > Config.MATCH_THRESHOLD:
                drug_info = self.get_drug_info(match)
                if drug_info:
                    found_drugs.append({
                        'matched': match,
                        'score': score,
                        'info': drug_info
                    })
        
        return found_drugs
    
    def get_drug_info(self, drug_name):
        drug_name_lower = drug_name.lower()
        row_fa = self.drugs_fa[
            self.drugs_fa['name_fa'].str.lower() == drug_name_lower
        ]
        if not row_fa.empty:
            return row_fa.iloc[0].to_dict()
        
        row_en = self.drugs_en[
            self.drugs_en['name'].str.lower() == drug_name_lower
        ]
        if not row_en.empty:
            return row_en.iloc[0].to_dict()
        
        return None
