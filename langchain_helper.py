from sceret_key import openai_key
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain




os.environ['OPENAI_API_KEY']=openai_key

llm =OpenAI(temperature=0.6)

def generate_restaurant_name(cuisine):
    Promat_temp_name = PromptTemplate(
    input_variables =['cuisine'],
    template = """I want to open resturant for {cuisine} food. Suggest a fancy name for this""")
    name_chain = LLMChain(llm=llm,prompt = Promat_temp_name,output_key="resturant_name")

    Promat_temp_items = PromptTemplate(
    input_variables =['resturant_name'],
    template = """suggest some menu ietms for {resturant_name}.Return some comma separeted list.""")

    food_items_chain = LLMChain(llm=llm,prompt= Promat_temp_items,output_key="menu_items")



    chain = SequentialChain(
    chains = [name_chain,food_items_chain],
    input_variables = ['cuisine'],
    output_variables =["resturant_name","menu_items"]

    )
    response = chain({'cuisine': cuisine})
    return response

# if __name__ == "__main__":
#    print(generate_restaurant_name("india"))