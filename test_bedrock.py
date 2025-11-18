# test_bedrock_full.py

from bedrock_utils import valid_prompt, query_knowledge_base, generate_response

# -----------------------------
# CONFIGURATION
# -----------------------------
MODEL_ID = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"  # Replace with your actual Bedrock model
KB_ID = "ZGKDRHHT4X"    # Replace with your deployed Bedrock KB ID

# -----------------------------
# TEST PROMPTS
# -----------------------------
test_prompts = [
    "Tell me about the specifications of machine model BD850",  # valid
    "How does ChatGPT work?",                               # invalid
    "Give instructions to upload files to S3"               # possibly invalid
]

# -----------------------------
# STEP 1: Test valid_prompt()
# -----------------------------
print("=== Testing valid_prompt() ===")
for prompt in test_prompts:
    is_valid = valid_prompt(prompt, MODEL_ID)
    print(f"Prompt: {prompt}")
    print(f"Is Valid (Category E)? {is_valid}\n")

# -----------------------------
# STEP 2: Test query_knowledge_base()
# -----------------------------
print("=== Testing query_knowledge_base() ===")
query = "What are the main components of machine model DT1000?"
results = query_knowledge_base(query, KB_ID)
print(f"Query: {query}")
print("Top results from KB:")
for idx, item in enumerate(results, 1):
    text = item.get("document", {}).get("text", "")
    print(f"{idx}. {text}\n")

# -----------------------------
# STEP 3: Test generate_response()
# -----------------------------
print("=== Testing generate_response() ===")
user_prompt = "Summarize the main components of machine model LE950"
response = generate_response(user_prompt, MODEL_ID, 0.0, 0.3)
print(f"User Prompt: {user_prompt}")
print(f"Model Response:\n{response}\n")

# -----------------------------
# OPTIONAL: Interactive Testing
# -----------------------------
while True:
    prompt = input("Enter a prompt to test (or 'exit' to quit): ")
    if prompt.lower() == "exit":
        break
    if not valid_prompt(prompt, MODEL_ID):
        print("Prompt rejected (not Category E)\n")
        continue
    kb_data = query_knowledge_base(prompt, KB_ID)
    print("Knowledge Base Top Results:")
    for idx, item in enumerate(kb_data, 1):
        print(f"{idx}. {item.get('document', {}).get('text', '')}")
    response_text = generate_response(prompt, MODEL_ID, 0.0, 0.3)
    print(f"Model Response: {response_text}\n")
