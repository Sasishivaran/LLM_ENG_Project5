import time
import csv
from datetime import datetime

# Mock model call (replace with real API if desired)
def mock_model_call(prompt: str):
    # Simulate latency
    start = time.time()
    time.sleep(0.2)
    response = f'Mock response for: {prompt[:50]}...'
    latency = time.time() - start
    token_usage = len(prompt.split()) + len(response.split())
    return response, latency, token_usage

def run_prompt_experiment(prompts, output_csv="prompt_experiment_results.csv"):
    rows = [["timestamp", "prompt_id", "prompt_text", "response_text", "latency_sec", "token_usage"]]

    for p in prompts:
        prompt_id = p["prompt_id"]
        text = p["prompt_text"]
        response, latency, tokens = mock_model_call(text)

        rows.append([
            datetime.utcnow().isoformat() + "Z",
            prompt_id,
            text,
            response,
            round(latency, 3),
            tokens
        ])

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Experiment results saved to {output_csv}")

if __name__ == "__main__":
    sample_prompts = [
        {"prompt_id": "p001", "prompt_text": "Customer: I was charged twice. What should I do?"},
        {"prompt_id": "p002", "prompt_text": "Customer: The app crashes every time I open it."}
    ]
    run_prompt_experiment(sample_prompts)
