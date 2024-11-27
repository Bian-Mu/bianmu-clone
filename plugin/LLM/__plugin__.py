from train.ChatModel import ChatModel

model_path = "./base_model"
checkpoint_path = "../output/checkpoint-500"

LLM=ChatModel(model_path=model_path,checkpoint_path=checkpoint_path)

