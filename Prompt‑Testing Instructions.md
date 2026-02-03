# Prompt‑Testing Instructions for Simulated Testing

## 1. Download the Required Files
Download the entire `tools/` folder from GitHub.

**GitHub Folder:**  
<[complete folder with input files](https://github.com/Sasishivaran/LLM_ENG_Project5/tree/main/tools)>

Click **Code → Download ZIP**, or download only the `tools/` folder if your platform supports it.

You should end up with these files:
- prompt_testing_sandbox.py
- prompt_sample_library.csv
- prompt_sample_library.md
- eval_rubric.csv
- eval_test_cases.csv
- value_stream_map_template.md
- prompt_testing_instructions.md

All files must be placed in the **same directory** inside your Jupyter environment.

## 2. Upload the Files into Your Jupyter Notebook Environment
Inside Jupyter:
1. Navigate to your working directory  
2. Click **Upload**  
3. Upload all files from the `tools/` folder  
4. Confirm they appear side‑by‑side like this:



No subfolders needed.

## 3. Run the Prompt‑Testing Sandbox
Open a new Jupyter cell and run:

```python
!python prompt_testing_sandbox.py
```
If everything is correct, you’ll see:

```python
Experiment results saved to prompt_experiment_results.csv
```

This means the script executed successfully.

## 4. Verify the Output File
After running the script, a new file will appear:


Open it in Jupyter:

```python
import pandas as pd
df = pd.read_csv("prompt_experiment_results.csv")
df.head()
```
You should see columns like:
- timestamp
- prompt_id
- prompt_text
- response_text
- latency_sec
- token_usage
