from huggingface_hub import InferenceClient
import os

def query_model(prompt):
    try:
        hf_token = os.getenv("HF_TOKEN")

        if not hf_token:
            return "Error: Hugging Face token not found. Please configure HF_TOKEN."

        client = InferenceClient(
            model="Qwen/Qwen2.5-7B-Instruct",
            token=hf_token
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional certified fitness trainer who strictly follows formatting instructions."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=800,
            temperature=0.5,
            top_p=0.9
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating workout plan: {str(e)}"
