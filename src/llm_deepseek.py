from openai import OpenAI

def DeepSeekLLM():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    def call(prompt):
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    return call
