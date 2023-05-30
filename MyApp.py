
import streamlit as st
import openai

openai.api_key = "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"

def generar_resumen(texto_largo):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=texto_largo,
        max_tokens=100,
        temperature=0.3,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None,
        n=1,
        echo=False
    )
    if response.choices and len(response.choices) > 0:
        resumen = response.choices[0].text.strip()
        return resumen
    else:
        return "No se pudo generar el resumen"

def generar_prompt(texto_largo,prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt+texto_largo,
        max_tokens=100,
        temperature=0.3,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None,
        n=1,
        echo=False
    )
    if response.choices and len(response.choices) > 0:
        resumen = response.choices[0].text.strip()
        return resumen
    else:
        return "No se pudo generar el resumen"




# Configurar la interfaz de la aplicación con Streamlit
st.title("Generador de Resúmenes de Texto")
texto_largo = st.text_area("Ingrese el texto largo que desea resumir")

if st.button("Generar Resumen", key="generar_resumen_btn"):
    if texto_largo :
        resumen = generar_resumen(texto_largo)
        st.subheader("Resumen:")
        st.write(resumen)
        
    else:
        st.write("Por favor, ingrese al menos un texto para generar el resumen")
prompt = st.text_area("Ingrese otro texto")   
if st.button("Generar Resumen con Prompt Adicional", key="generar_resumen_prompt_btn"):
    if prompt:
        prompt = generar_prompt(texto_largo,prompt)
        st.subheader("prompt:")
        st.write(prompt)
    else:
        st.write("Por favor, ingrese el prompt adicional para generar el resumen")
