from together import Together

# Inicializar cliente con clave de API
client = Together(api_key="c93d7fed154e79ad0c180cd64526997024329864250d0e2de676aa1d1b0f29ce")

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    messages=[{"role": "user", "content": "What are some fun things to do in New York?"}],
)

# Corregir error en la impresión
print(response.choices[0].message.content)
