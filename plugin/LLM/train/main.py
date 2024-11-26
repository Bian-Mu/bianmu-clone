from ChatModel import ChatModel

model_path = "./base_model"
checkpoint_path = "../output/checkpoint-500"

LLM=ChatModel(model_path=model_path,checkpoint_path=checkpoint_path)

Flag=True

while Flag:
    text=input("You:")
    if text!="exit":
        response=LLM.func_chat(text)
        print("LLM:",response)
    else:
        Flag=False