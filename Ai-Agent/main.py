from llama_index.llms.ollama import Ollama


print("What is your question")
x = input()
llm = Ollama(model="mistral", request_timeout=45.0)
response = llm.complete(x)
print(response)