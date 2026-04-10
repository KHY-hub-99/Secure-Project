from datasets import load_dataset
import json
import re
import torch
import transformers
from transformers import pipeline
import time

# 오직 에러 메시지만 출력 (경고 무시)
transformers.utils.logging.set_verbosity_error()

# LLM06 카테고리에 해당하는 취약점 데이터만 필터링해서 가져오기
dataset = load_dataset("scthornton/securecode-aiml")
dataset_gui = []
for item in dataset["train"]:
    if item["metadata"]["owasp_llm_2025"] == "LLM01" or item["metadata"]["owasp_llm_2025"] == "LLM02" or item["metadata"]["owasp_llm_2025"] == "LLM06" or item["metadata"]["owasp_llm_2025"] == "LLM07":
        dataset_gui.append(item)
print(len(dataset_gui))

print("\n######### 가이드라인 확인 #########\n")
for item in dataset_gui[:5]:
    print(f"\nID: {item['id']}\n")
    print(f"\nGuidance: {item['security_assertions']}\n")
    print(f"\nAttack Context: {item['context']['description']}\n")
    print("=" * 50)

# def extract_useful_data(raw_json):
#     return {
#         "vulnerability_id": raw_json["id"],
#         "owasp_category": raw_json["metadata"]["owasp_llm_2025"],
        
#         # Red Agent가 공격 시나리오를 짤 때 읽어볼 컨텍스트
#         "attack_context": raw_json["context"]["description"],
        
#         # 실제 테스트에 찔러볼 초기 공격/질문 프롬프트
#         "seed_prompt": raw_json["conversations"][0]["content"],
        
#         # Evaluate Agent가 채점할 때 사용할 보안 체크리스트
#         "evaluation_criteria": raw_json["security_assertions"]
#     }