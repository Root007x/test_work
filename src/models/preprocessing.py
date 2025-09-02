from typing import BinaryIO
from pdfminer.high_level import extract_text
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from core.logging import logger
from schemas.prompts import PARSING_TEMPLATE
from config.config import JSON_SAVE_FILE_LOCATION
from src.utils.helper import save_json_file


logger = logger(__name__)



class Preprocess:
    
    
    def __init__(self, pdf_file: BinaryIO, model):
        self.pdf_file = pdf_file
        self.llm = model
        
        
    def extract_pdf_data(self):
        cv_data = extract_text(self.pdf_file)
        logger.info("PDF data extraction completed!")
        
        extract_prompt = PromptTemplate(
            template=PARSING_TEMPLATE,
            input_variables=["resume_context"]
        )
        
        parser = JsonOutputParser()
        
        chain = extract_prompt | self.llm | parser
        
        extract_structure_output = chain.invoke({
            "resume_context" : cv_data
        })
        
        logger.info("Structure Data Extraction completed.")
        
        # save as json
        save_json_file(
            save_location=JSON_SAVE_FILE_LOCATION,
            data=extract_structure_output
        )
        
        logger.info("Json File Saved Successfully")
        
        
        
        
        
        
        
        
    
    