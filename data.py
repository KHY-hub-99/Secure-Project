import json

def load_test_cases(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        test_cases = json.load(f)
    return test_cases

def extract_test_cases(test_data, category=None):
    if category:
        return [case for case in test_data if case['category'] == category]
    return test_data

data = load_test_cases('colla_v1.json')
filtered_data = extract_test_cases(data, category='LLM06')

print("\n======= LLM06 Test data =======\n")
for case in filtered_data:
    print(f"\n{case['prompt_text']}\n")
    print("=" * 50)