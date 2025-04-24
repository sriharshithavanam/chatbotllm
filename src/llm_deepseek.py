from openai import OpenAI

def DeepSeekLLM():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="apikey",
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
