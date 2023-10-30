import openai #importamos la libreria de openai

openai.api_key = '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' #asigamos nuestra clave api

response = openai.Completion.create( #llamamamos la api y le damos un promt y asignamos algunos parametros con los que queremos que funcione
  model="text-davinci-003",
  prompt="Decide si el sentimiento de un Tweet es positivo, neutral, o negativo. \
  \n\nTweet: \"#LoNuevoEnPlatzi es el Platzibot 🤖. Un asistente creado con Inteligencia Artificial para acompañarte en tu proceso de aprendizaje.\
  \"\nSentiment:",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)
response.choices[0].text #mostramos la respuesta de la solicitud anterior