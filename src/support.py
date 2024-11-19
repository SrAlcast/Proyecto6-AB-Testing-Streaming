import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, mannwhitneyu, shapiro, levene

def realizar_ab_test(data, columna_grupo, columna_variable, valor_grupo1, valor_grupo2, alpha=0.05):
    """
    Realiza un A/B test entre dos grupos en una variable específica, seleccionando automáticamente el test adecuado
    en función de la normalidad y homocedasticidad de los datos. Genera visualizaciones para los grupos.

    Parámetros:
    - data (pd.DataFrame): DataFrame que contiene los datos a analizar.
    - columna_grupo (str): Nombre de la columna que contiene los grupos a comparar.
    - columna_variable (str): Nombre de la variable en la cual se realizará el A/B test.
    - valor_grupo1 (str): Valor que identifica al primer grupo en columna_grupo.
    - valor_grupo2 (str): Valor que identifica al segundo grupo en columna_grupo.
    - alpha (float): Nivel de significancia para las pruebas estadísticas. Default es 0.05.

    Procedimiento:
    1. Filtra los datos para los grupos específicos.
    2. Verifica la normalidad de ambas muestras usando el test de Shapiro-Wilk.
    3. Verifica la homocedasticidad entre las muestras usando el test de Levene.
    4. Selecciona y realiza el test adecuado:
        - Si ambas muestras son normales y homocedásticas, realiza un test t de dos muestras (independientes).
        - Si alguna de las condiciones no se cumple, realiza el test no paramétrico de Mann-Whitney U.
    5. Imprime el resultado, indicando el test aplicado, el estadístico de prueba y si hay diferencia significativa.
    6. Genera visualizaciones de la distribución de los datos para cada grupo.

    """
    # Filtrar datos para cada grupo
    grupo1 = data[data[columna_grupo] == valor_grupo1][columna_variable].dropna()
    grupo2 = data[data[columna_grupo] == valor_grupo2][columna_variable].dropna()

    # Verificar normalidad con Shapiro-Wilk
    normal1 = shapiro(grupo1)[1] > alpha
    normal2 = shapiro(grupo2)[1] > alpha
    if normal1 and normal2:
        print("Son distribuciones normales")
    else:
        print("Son distribuciones no normales")        

    # Verificar homocedasticidad con Levene
    homocedastico = levene(grupo1, grupo2)[1] > alpha
    if homocedastico:
        print("Son distribuciones homocedasticas")
    else:
        print("Son distribuciones no homocedasticas")   
    # Decidir y aplicar el test correcto
    if normal1 and normal2 and homocedastico:
        # Test t si ambas distribuciones son normales y homocedásticas
        estadistico_prueba, p_valor = ttest_ind(grupo1, grupo2)
        tipo_test = 'test t'
    else:
        # Test de Mann-Whitney si no cumple normalidad o homocedasticidad
        estadistico_prueba, p_valor = mannwhitneyu(grupo1, grupo2)
        tipo_test = 'test Mann-Whitney U'

    # Imprimir resultados
    print(f"Variable: {columna_variable}")
    print(f"Test aplicado: {tipo_test}")
    print(f"Estadístico de prueba: {estadistico_prueba:.2f} | P-valor: {p_valor:.4f}")
    if p_valor < alpha:
        print(f"--> Diferencia significativa en '{columna_variable}' entre {valor_grupo1} y {valor_grupo2}.\n")
    else:
        print(f"--> No hay diferencia significativa en '{columna_variable}' entre {valor_grupo1} y {valor_grupo2}.\n")

    # Visualización de los datos
    print("---------------------------------------")
    print(f"Visualizaciones de variables:")
    plt.figure(figsize=(12, 6))

    # Gráfico de caja
    plt.subplot(1, 2, 1)
    sns.boxplot(x=columna_grupo, y=columna_variable, data=data)
    plt.title(f'Distribución de {columna_variable} por grupo (Boxplot)')

    # Gráfico de violín
    plt.subplot(1, 2, 2)
    sns.violinplot(x=columna_grupo, y=columna_variable, data=data)
    plt.title(f'Distribución de {columna_variable} por grupo (Violin Plot)')

    plt.tight_layout()
    plt.show()

    grupos = data[columna_grupo].nunique()
    # Calcular el número de filas y columnas para los subplots
    filas = (grupos // 2) + (grupos % 2)
    columnas = 2
    
    # Crear subplots de acuerdo al tamaño de los grupos
    fig, axes = plt.subplots(filas, columnas, figsize=(10, 5))
    axes = axes.flatten()

    lista_grupos = list(data[columna_grupo].unique())

    # Crear histogramas para cada grupo
    for indice, grupo in enumerate(lista_grupos):
        sns.histplot(data[data[columna_grupo] == grupo], x=columna_variable, ax=axes[indice], kde=True)
        axes[indice].set_xlabel(f'Grupo {grupo}')

    # Eliminar subplots vacíos si hay un número impar de grupos
    if grupos % 2 != 0:
        fig.delaxes(axes[-1])
        
    plt.tight_layout() 
    plt.show()

