from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


from src.core.logging import logger
from src.utils.helper import load_json_file
from src.config.config import JSON_SAVE_FILE_LOCATION
from src.schemas.prompts import SCORE_TEMPLATE

logger = logger(__name__)

class GenerateScore:
    
    
    def __init__(self, model):
        self.llm = model
    
    
    def score(self, job_des : str):
        # load data
        logger.info("Loading Json File........")
        
        parsed_cv_data = load_json_file(JSON_SAVE_FILE_LOCATION)
        
        
        score_prompt = PromptTemplate(
            template=SCORE_TEMPLATE,
            input_variables=["job_description", "resume"]
        )
        
        parser = JsonOutputParser()
        
        chain = score_prompt | self.llm | parser
        
        output = chain.invoke({
            "resume" : parsed_cv_data,
            "job_description" : job_des
        })
        
        score = int(output["score"].replace('%',''))
        
        logger.info("Score Generated Successfully")
        
        return score