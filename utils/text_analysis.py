from typing import List

import pickle as pkl

class text_token:
    def __init__(self, start_time:int = None, end_time:int = None, text:str = "", answer:str = None) -> None:
        self.start_time = start_time
        self.end_time = end_time
        
        self.text = text
        self.answer = answer

class text_content:
    
    def __init__(self, original_text:List[text_token] = None,
                complete_text:List[text_token] = None) -> None:
        self.original_text = original_text
        self.complete_text = complete_text
        
    @staticmethod
    def load_text_from_file(self, path):
        caption_pkl = pkl.load(open(path, "rb"))