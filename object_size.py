from openai import OpenAI

import base64



client = OpenAI(api_key="")


response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image": "https://images.unsplash.com/photo-1622838321711-4c6b3f1f6d5b",
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])