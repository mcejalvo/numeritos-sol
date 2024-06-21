import streamlit as st
import numpy as np

# Título del dashboard
st.title('Los numeritos de Sol')

# Entradas del usuario
s = st.number_input('Suma total', min_value=1, value=10)
v_m = st.number_input('Valor mínimo', min_value=1, value=1)
v_M = st.number_input('Valor máximo', min_value=1, value=10)
n = st.number_input('Número total de sumandos', min_value=2, value=3)
max_intentos = st.number_input('Número máximo de intentos (subir si no se encuentra solución)', value=10000)


# Validación de entrada
if v_m > v_M:
    st.error('El valor mínimo no puede ser mayor que el valor máximo')
else:
    encontrado = False
    intentos = 0

    while not encontrado and intentos < max_intentos:
        # Generar n-1 números aleatorios
        numeros_aleatorios = np.random.randint(v_m, v_M+1, n-1)
        
        # Calcular el último número
        suma_parcial = np.sum(numeros_aleatorios)
        ultimo_numero = s - suma_parcial

        if v_m <= ultimo_numero <= v_M:
            encontrado = True
            numeros_aleatorios = np.append(numeros_aleatorios, ultimo_numero)
        intentos += 1

    if encontrado:
        # Mostrar los números generados
        st.write('Números generados:')
        st.write(numeros_aleatorios)

        # Verificar la suma
        st.write('Suma de los números generados:')
        st.write(np.sum(numeros_aleatorios))
    else:
        st.error('No se pudo generar una secuencia válida dentro del número máximo de intentos.')
