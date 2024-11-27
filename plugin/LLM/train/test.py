from ChatModel import ChatModel

model_path = "./base_model"
checkpoint_path = "../output/checkpoint-500"

LLM_v1=ChatModel(model_path=model_path,checkpoint_path=checkpoint_path)

print(LLM_v1.func_chat("你这？"))