import json
from together import Together

# Inicializar cliente con la API Key
client = Together(api_key="tu_api_key")

# Función para chatear con el modelo y extraer JSON
def chat_with_model_and_extract_json(user_input):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=[{"role": "user", "content": user_input}]
    )

    assistant_reply = response.choices[0].message.content

    # Intentar extraer el JSON de la respuesta
    try:
        json_start = assistant_reply.find("{")  # Encuentra el inicio del JSON
        json_end = assistant_reply.rfind("}") + 1  # Encuentra el final del JSON
        json_str = assistant_reply[json_start:json_end]  # Extrae solo el JSON
        json_data = json.loads(json_str)  # Convierte la cadena JSON en un diccionario
        return json_data
    except (json.JSONDecodeError, ValueError, IndexError):
        print("No se pudo extraer un JSON válido de la respuesta de la IA.")
        return None

# Solicitar la rutina en formato JSON
user_prompt = (
    "Eres un entrenador de gimnasio experto. Genera un plan de entrenamiento en formato JSON "
    "para la siguiente persona:\n\n"
    "- Nombre: Juan Pérez\n"
    "- Peso: 75 kg\n"
    "- Altura: 1.75 m\n"
    "- Sexo: Masculino\n"
    "- Condiciones médicas: Ninguna\n"
    "- Meta del entrenamiento: Aumentar masa muscular\n\n"
    "El JSON debe seguir esta estructura:\n\n"
    f"{json.dumps(json_template, indent=2)}"
)

# Llamar a la IA y extraer el JSON
rutina_json = chat_with_model_and_extract_json(user_prompt)

# Imprimir la rutina extraída
if rutina_json:
    print("Rutina extraída correctamente:")
    print(json.dumps(rutina_json, indent=2))
else:
    print("No se obtuvo un JSON válido.")