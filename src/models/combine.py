from langchain_groq import ChatGroq

from src.config.config import GROQ_API_KEY, LLM_MODEL_NAME




# 1. Model Setup
# 2. Preprocessing
# 3. score
# 4. rewrite_cv

# LLM Model Setup
model = ChatGroq(
    model = LLM_MODEL_NAME
)


print(model.invoke("Hi"))



