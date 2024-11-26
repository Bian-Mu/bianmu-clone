import os
import torch
from transformers import AutoConfig, AutoModel, AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class ChatModel:
    def __init__(self, model_path, checkpoint_path, kernel_file="../quantization_kernels_parallel.so"):
        
        self.model_path = model_path
        self.checkpoint_path = checkpoint_path
        self.kernel_file = kernel_file

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        self.config = AutoConfig.from_pretrained(self.model_path, trust_remote_code=True, pre_seq_len=128)
        
        self.model = AutoModel.from_pretrained(self.model_path, kernel_file=self.kernel_file, config=self.config, trust_remote_code=True)

        # 加载prefix_encoder的权重
        prefix_state_dict = torch.load(os.path.join(self.checkpoint_path, "pytorch_model.bin"),map_location=device)
        new_prefix_state_dict = {}
        for k, v in prefix_state_dict.items():
            new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
        self.model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

        self.model = self.model.quantize(4, kernel_file=self.kernel_file)

        self.model = self.model.half().cuda()
        self.model.transformer.prefix_encoder.float()
        self.model.to(device)
        self.model = self.model.eval()

    def func_chat(self, input_text):
        response, history = self.model.chat(self.tokenizer, input_text, history=[])
        return response
    

# model_path = "./base_model"

# tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
# config = AutoConfig.from_pretrained(model_path, trust_remote_code=True, pre_seq_len=128)
# model = AutoModel.from_pretrained(model_path, kernel_file="../quantization_kernels_parallel.so",config=config, trust_remote_code=True)

# prefix_state_dict = torch.load(os.path.join("../output/checkpoint-500", "pytorch_model.bin"))
# new_prefix_state_dict = {}
# for k, v in prefix_state_dict.items():
#     new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
# model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)


# model = model.quantize(4,kernel_file="../quantization_kernels_parallel.so")
# model = model.half().cuda()
# model.transformer.prefix_encoder.float()
# model = model.eval()

# response, history = model.chat(tokenizer, "明天要开会吗", history=[])
# print(response)