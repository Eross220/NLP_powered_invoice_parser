from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
class paymentItem(BaseModel):
    bank_name: str= Field(description="the name of the Bank")
    account_name: str= Field(description="account name of the Bank")
    account_no: str= Field(description="the No of the bank")
    bank_address: str= Field(description="the address of bank")

class ExtractInvoice (BaseModel):
    bill_to: str= Field(description="the person of Bill to")
    invoice_number:int =Field(description="the number of the Invoice")
    invoice_date:str =Field(description="the Date of the Invoice")
    unit_price:int = Field(description="the price of the Unit")
    total_amount:float = Field(description="amount of the Total Amount")
    work_description: List[str]=Field(description="Work Description")
    payment_description: paymentItem = Field(description="Payment Instructions")

    
invoice_extract_parser:PydanticOutputParser = PydanticOutputParser(pydantic_object=ExtractInvoice)