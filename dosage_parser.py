python
import re

class DosageParser:
    def init(self):
        self.patterns = {
            'q8h': 'every 8 hours',
            'q12h': 'every 12 hours',
            'qd': 'once daily',
            'bid': 'twice daily',
            'tid': 'three times daily',
            'qid': 'four times daily',
            'hs': 'at bedtime',
            'prn': 'as needed'
        }
    
    def parse(self, text):
        text_lower = text.lower()
        dosage_info = {
            'frequency': None,
            'amount': 1,
            'unit': 'tablet',
            'parsed_text': text
        }
        
        for code, meaning in self.patterns.items():
            if code in text_lower:
                dosage_info['frequency'] = meaning
                dosage_info['parsed_text'] = text.replace(code, meaning)
        
        amount_match = re.search(r'(\d+)\s*(?:tab|cap|pill)', text_lower)
        if amount_match:
            dosage_info['amount'] = int(amount_match.group(1))
        
        return dosage_info
