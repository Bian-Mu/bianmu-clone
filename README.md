# bianmu-clone

- **Description**:一个用于替代本人水群的QQbot，献给亲爱的群友

## 功能

1. LLM：用本人群发言训练过的，基于ChatGLM-6B-4bit，训练语料约为2800条发言做成的1400组左右的个人对话，部分文件ignore了（想来也没有人用这个，后续有需要的话可以写一个大致教程）;  
2. Randomly_Speak：随机发言（LLM+群友旧言）、复读、回答（LLM）
3. Stalk_You：翻译为“视奸”，考虑记录特定群友的发言内容与习惯
4. Life_sucks：翻译为”生草的生活“，考虑完成日常功能

## 部署

主要采用Lagrange.Core+Melobot实现，由于LLM推理需要占用一定显存，故被迫先在本地使用，待到荷包充足考虑上服务器（老实说电脑晚上关机之后QQbot正好不发言了，更像个真人吧）

## todolist

1. 添加图片相关功能
2. Life_Sucks加一些功能
3. Randomly_Speak完善随机的逻辑