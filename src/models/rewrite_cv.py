from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from schemas.prompts import REWRITE_TEMPLATE
from config.config import JSON_SAVE_FILE_LOCATION
from utils.helper import load_json_file



class ReWrite:
    
    def __init__(self, model):
        self.llm = model
    
    
    
    def re_write_cv(self, score : int, job_des : str):
        # load data
        
        parsed_cv_data = load_json_file(JSON_SAVE_FILE_LOCATION)
        
        
        if score > 50:
            return {"Score" : score}
        else:
            
            re_write_prompt = PromptTemplate(
                template=REWRITE_TEMPLATE,
                input_variables=["resume", "job_description"]
            )
            
            parser = JsonOutputParser()
            
            chain = re_write_prompt | self.llm | parser
            
            output_result = chain.invoke({
                "resume" : parsed_cv_data,
                "job_description" : job_des
            })
            
            return output_result
        