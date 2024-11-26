# export HF_ENDPOINT=https://hf-mirror.com

from transformers import AutoModel, AutoTokenizer

# 指定模型名称
model_name = "THUDM/chatglm-6b-int4"
model_save_path = "./train/base_model"  # 指定保存模型的位置

# 下载模型和分词器，并保存到指定路径
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, quantization_bit=4)

# 将模型和分词器保存到指定路径
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(model_save_path)
