import json

def prepare_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i + 1].strip() if i + 1 < len(lines) else ''
        
        data.append({
            "content": question,
            "summary": answer
        })
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


prepare_data('train_data.txt', 'formatted_data.json')
