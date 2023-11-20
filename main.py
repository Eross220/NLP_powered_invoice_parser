import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from outputpaser import invoice_extract_parser

def extract_data(data:str)->str:
     extract_template="""
        given the invoice information {information} from I want you to create:
        1.Bill To
        2.Invoice Number
        3.Invoice Date
        4.Unit Pirce
        5:Total Amount
        6.Work Description
        7:Payment Instructions:
        \n\{format_instruction}
     """

     extract_prompt=PromptTemplate(
          input_variables=["information"], 
          template=extract_template,
          partial_variables={"format_instruction":invoice_extract_parser.get_format_instructions()}
          
     )

    
     llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

     chain = LLMChain(llm=llm, prompt=extract_prompt)
     result= chain.run(information=data)

     return result

if __name__=='__main__':
     pdf_path="10-04 invoice.pdf"
     loader= PyPDFLoader(file_path=pdf_path)
     documents=loader.load()

     invoice_data=documents[0].page_content
     result=extract_data(data=invoice_data)

     print(result)



