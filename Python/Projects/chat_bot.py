# from transformers import AutoModelForCausalLM, AutoTokenizer

# # Cargar el modelo preentrenado
# modelo = "dccuchile/gpt2-spanish"  # Puedes usar otros modelos disponibles en Hugging Face
# tokenizer = AutoTokenizer.from_pretrained(modelo)
# model = AutoModelForCausalLM.from_pretrained(modelo)

# def chatbot_responder(pregunta):
#     """
#     Función que genera una respuesta a partir de una pregunta usando GPT-2.

#     :param pregunta: String con la pregunta o mensaje del usuario.
#     :return: String con la respuesta generada.
#     """
#     # Convertir la entrada en tokens
#     input_ids = tokenizer.encode(pregunta, return_tensors="pt")
#     respuesta_ids = model.generate(
#         input_ids,
#         max_length=100,
#         num_return_sequences=1,
#         no_repeat_ngram_size=2,
#         temperature=0.7,
#         top_k=50
#     )
#     respuesta = tokenizer.decode(respuesta_ids[0], skip_special_tokens=True)
#     return respuesta
  
# def iniciar_chatbot():
#     print("¡Hola! Soy tu chatbot. Puedes preguntarme cosas como:")
#     print("- ¿Cómo está el clima?")
#     print("- ¿Qué es la inteligencia artificial?")
#     print("Escribe 'salir' para terminar la conversación.\n")
    
#     while True:
#         pregunta = input("Tú: ")
#         if pregunta.lower() == "salir":
#             print("Chatbot: ¡Adiós! Que tengas un buen día.")
#             break
#         respuesta = chatbot_responder(pregunta)
#         print(f"Chatbot: {respuesta}")

# # Iniciar el chatbot
# iniciar_chatbot()

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Cargar el modelo mBART preentrenado
modelo = "facebook/mbart-large-50"
tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSeq2SeqLM.from_pretrained(modelo)

def chatbot_mbart(pregunta):
    """
    Responde a preguntas en español usando el modelo mBART.
    """
    # Ajustar el tokenizer al idioma español
    tokenizer.src_lang = "es_XX"
    tokenizer.tgt_lang = "es_XX"

    # Tokenizar la entrada
    input_ids = tokenizer.encode(pregunta, return_tensors="pt")

    # Generar respuesta
    output_ids = model.generate(
        input_ids,
        max_length=100,
        num_beams=5,
        no_repeat_ngram_size=2,
        temperature=0.7
    )

    # Decodificar la respuesta
    respuesta = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return respuesta

# Ejemplo de uso
pregunta = "¿Qué es la inteligencia artificial?"
print(chatbot_mbart(pregunta))