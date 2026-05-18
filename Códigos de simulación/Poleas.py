# Importa pandas para organizar los datos en tablas tipo DataFrame.
import pandas as pd

# Importa numpy para cálculos numéricos, promedios, desviaciones y arreglos.
import numpy as np

# Importa el módulo stats de scipy para aplicar pruebas estadísticas como t-Student.
from scipy import stats

# Importa matplotlib para generar las gráficas.
import matplotlib.pyplot as plt


# 1. DATOS EXPERIMENTALES

# Se crea una lista con los datos experimentales obtenidos en Tracker.
datos = [
    # ID, montaje, cuerda, n, poleas móviles, tuercas motriz, masa motriz, masa carga, masa efectiva, aceleración teórica, toma 1, toma 2, toma 3, toma 4, toma 5.
    [1, "Una polea", "Ideal", 1, 0, 2, 70, 40, 40, 2.6673, 2.5863, 2.5179, 2.4582, 2.5410, 2.5576],
    # Datos para una polea, cuerda ideal, tres tuercas.
    [2, "Una polea", "Ideal", 1, 0, 3, 100, 40, 40, 4.1914, 4.0723, 4.0401, 4.0957, 4.1889, 4.0294],
    # Datos para una polea, cuerda ideal, cuatro tuercas.
    [3, "Una polea", "Ideal", 1, 0, 4, 130, 40, 40, 5.1776, 4.7947, 4.9354, 4.9495, 4.8683, 4.9566],

    # Datos para doble polea, cuerda ideal, dos tuercas.
    [4, "Doble polea", "Ideal", 2, 1, 2, 70, 40, 82, 1.5670, 1.5056, 1.3537, 1.4923, 1.3810, 1.4135],
    # Datos para doble polea, cuerda ideal, tres tuercas.
    [5, "Doble polea", "Ideal", 2, 1, 3, 100, 40, 82, 2.3943, 2.2243, 2.0128, 2.2013, 2.0892, 2.2646],
    # Datos para doble polea, cuerda ideal, cuatro tuercas.
    [6, "Doble polea", "Ideal", 2, 1, 4, 130, 40, 82, 2.8918, 2.6497, 2.5800, 2.7113, 2.7246, 2.7225],

    # Datos para tres poleas, cuerda ideal, dos tuercas.
    [7, "Tres poleas", "Ideal", 3, 2, 2, 70, 40, 124, 1.1155, 0.9548, 0.9758, 0.9411, 0.8522, 0.9288],
    # Datos para tres poleas, cuerda ideal, tres tuercas.
    [8, "Tres poleas", "Ideal", 3, 2, 3, 100, 40, 124, 1.6809, 1.4463, 1.4816, 1.4522, 1.3026, 1.4151],
    # Datos para tres poleas, cuerda ideal, cuatro tuercas.
    [9, "Tres poleas", "Ideal", 3, 2, 4, 130, 40, 124, 2.0104, 1.6151, 1.7768, 1.7005, 1.7141, 1.8847],

    # Datos para una polea, cuerda con masa, dos tuercas.
    [10, "Una polea", "Con masa", 1, 0, 2, 70, 40, 40, 2.6673, 2.4278, 2.4131, 2.2386, 2.2714, 2.3017],
    # Datos para una polea, cuerda con masa, tres tuercas.
    [11, "Una polea", "Con masa", 1, 0, 3, 100, 40, 40, 4.1914, 3.9252, 3.7183, 3.7753, 3.6059, 3.6000],
    # Datos para una polea, cuerda con masa, cuatro tuercas.
    [12, "Una polea", "Con masa", 1, 0, 4, 130, 40, 40, 5.1776, 4.5192, 4.2463, 4.3962, 4.5390, 4.5704],

    # Datos para doble polea, cuerda con masa, dos tuercas.
    [13, "Doble polea", "Con masa", 2, 1, 2, 70, 40, 82, 1.5670, 1.2858, 1.2379, 1.2886, 1.2597, 1.1787],
    # Datos para doble polea, cuerda con masa, tres tuercas.
    [14, "Doble polea", "Con masa", 2, 1, 3, 100, 40, 82, 2.3943, 1.8892, 1.7143, 1.8679, 1.9187, 1.8730],
    # Datos para doble polea, cuerda con masa, cuatro tuercas.
    [15, "Doble polea", "Con masa", 2, 1, 4, 130, 40, 82, 2.8918, 2.4525, 2.3530, 2.0413, 2.3255, 2.1887],

    # Datos para tres poleas, cuerda con masa, cuatro tuercas.
    [16, "Tres poleas", "Con masa", 3, 2, 4, 130, 40, 124, 2.0104, 1.1145, 1.1336, 1.1344, 1.1610, 1.2266],
]

# Se definen los nombres de las columnas de la tabla principal.
columnas = [
    # Identificador de cada condición experimental.
    "ID",
    # Tipo de montaje usado.
    "Montaje",
    # Tipo de cuerda utilizada.
    "Cuerda",
    # Número de tramos de cuerda que sostienen la carga.
    "n",
    # Número de poleas móviles.
    "Poleas_moviles",
    # Número de tuercas en el vaso motriz.
    "Tuercas_motriz",
    # Masa motriz total en gramos.
    "m_motriz_g",
    # Masa de la carga en gramos.
    "M_carga_g",
    # Masa efectiva de la carga en gramos.
    "M_ef_g",
    # Aceleración teórica ideal en m/s².
    "a_teo_ideal",
    # Primera toma experimental.
    "Toma_1",
    # Segunda toma experimental.
    "Toma_2",
    # Tercera toma experimental.
    "Toma_3",
    # Cuarta toma experimental.
    "Toma_4",
    # Quinta toma experimental.
    "Toma_5"
]

# Se convierte la lista de datos en un DataFrame de pandas.
df = pd.DataFrame(datos, columns=columnas)

# Se define una lista con los nombres de las columnas que contienen las tomas experimentales.
tomas = ["Toma_1", "Toma_2", "Toma_3", "Toma_4", "Toma_5"]


# 2. CÁLCULOS ESTADÍSTICOS

# Se define una función para analizar estadísticamente cada fila del DataFrame.
def analizar_fila(row):
    # Se extraen las cinco tomas experimentales de la fila actual.
    valores = row[tomas].astype(float).to_numpy()

    # Se extrae la aceleración teórica ideal de la fila actual.
    a_teo = row["a_teo_ideal"]

    # Se calcula la aceleración experimental promedio.
    promedio = np.mean(valores)

    # Se calcula la desviación estándar muestral de las cinco tomas.
    desviacion = np.std(valores, ddof=1)

    # Se calcula la incertidumbre de la media.
    incertidumbre = desviacion / np.sqrt(len(valores))

    # Se calcula el error relativo porcentual respecto al modelo ideal.
    error_relativo = abs((promedio - a_teo) / a_teo) * 100

    # Se aplica una prueba t-Student de una muestra contra el valor teórico ideal.
    t_stat, p_valor = stats.ttest_1samp(valores, popmean=a_teo)

    # Se determina si se rechaza la hipótesis nula con un nivel de significancia de 0.05.
    rechaza_H0 = p_valor < 0.05

    # Se devuelven los resultados calculados como una Serie de pandas.
    return pd.Series({
        # Aceleración experimental promedio.
        "a_exp_promedio": promedio,
        # Desviación estándar de las tomas.
        "desviacion_estandar": desviacion,
        # Incertidumbre de la media.
        "incertidumbre_media": incertidumbre,
        # Error relativo porcentual.
        "error_relativo_%": error_relativo,
        # Estadístico t calculado.
        "t_stat": t_stat,
        # Valor p de la prueba t-Student.
        "p_valor": p_valor,
        # Resultado lógico de la prueba.
        "rechaza_H0": rechaza_H0
    })

# Se aplica la función de análisis a cada fila de la tabla.
resultados_estadisticos = df.apply(analizar_fila, axis=1)

# Se une la tabla original con los resultados estadísticos.
resumen = pd.concat([df, resultados_estadisticos], axis=1)


# 3. COMPARACIÓN ENTRE CUERDA IDEAL Y CUERDA CON MASA

# Se crea una lista vacía donde se guardarán las comparaciones.
comparaciones = []

# Se recorren los diferentes tipos de montaje.
for montaje in resumen["Montaje"].unique():
    # Se recorren los diferentes números de tuercas motrices.
    for tuercas in resumen["Tuercas_motriz"].unique():

        # Se filtra la condición con cuerda ideal para el montaje y número de tuercas actual.
        ideal = resumen[
            (resumen["Montaje"] == montaje) &
            (resumen["Cuerda"] == "Ideal") &
            (resumen["Tuercas_motriz"] == tuercas)
        ]

        # Se filtra la condición con cuerda con masa para el montaje y número de tuercas actual.
        con_masa = resumen[
            (resumen["Montaje"] == montaje) &
            (resumen["Cuerda"] == "Con masa") &
            (resumen["Tuercas_motriz"] == tuercas)
        ]

        # Se verifica que existan ambas condiciones para poder compararlas.
        if len(ideal) == 1 and len(con_masa) == 1:

            # Se extraen las cinco tomas de la condición con cuerda ideal.
            valores_ideal = ideal.iloc[0][tomas].astype(float).to_numpy()

            # Se extraen las cinco tomas de la condición con cuerda con masa.
            valores_masa = con_masa.iloc[0][tomas].astype(float).to_numpy()

            # Se calcula el promedio de aceleración con cuerda ideal.
            prom_ideal = valores_ideal.mean()

            # Se calcula el promedio de aceleración con cuerda con masa.
            prom_masa = valores_masa.mean()

            # Se calcula la reducción porcentual de aceleración al usar cuerda con masa.
            reduccion = ((prom_ideal - prom_masa) / prom_ideal) * 100

            # Se aplica una prueba t de Welch para comparar las dos condiciones.
            t_welch, p_welch = stats.ttest_ind(valores_ideal, valores_masa, equal_var=False)

            # Se determina si la diferencia entre cuerdas es estadísticamente significativa.
            diferencia_significativa = p_welch < 0.05

            # Se agrega el resultado de la comparación a la lista.
            comparaciones.append({
                # Tipo de montaje comparado.
                "Montaje": montaje,
                # Número de tuercas motrices usadas.
                "Tuercas_motriz": tuercas,
                # Promedio con cuerda ideal.
                "a_ideal_prom": prom_ideal,
                # Promedio con cuerda con masa.
                "a_con_masa_prom": prom_masa,
                # Reducción porcentual.
                "reduccion_%": reduccion,
                # Estadístico t de Welch.
                "t_welch": t_welch,
                # Valor p de Welch.
                "p_welch": p_welch,
                # Resultado lógico de la comparación.
                "diferencia_significativa": diferencia_significativa
            })

# Se convierte la lista de comparaciones en un DataFrame.
comparacion_cuerdas = pd.DataFrame(comparaciones)


# 4. MOSTRAR TABLAS EN CONSOLA

# Se configura pandas para mostrar más columnas en consola.
pd.set_option("display.max_columns", None)

# Se configura pandas para mostrar más ancho de tabla en consola.
pd.set_option("display.width", 200)

# Se imprime un título para la tabla de resumen estadístico.
print("\nRESUMEN ESTADÍSTICO POR CONDICIÓN\n")

# Se imprime una versión resumida de los resultados principales.
print(
    resumen[
        [
            "ID",
            "Montaje",
            "Cuerda",
            "Tuercas_motriz",
            "a_teo_ideal",
            "a_exp_promedio",
            "desviacion_estandar",
            "incertidumbre_media",
            "error_relativo_%",
            "p_valor",
            "rechaza_H0"
        ]
    ].round(5)
)

# Se imprime un título para la tabla de comparación entre cuerdas.
print("\nCOMPARACIÓN ENTRE CUERDA IDEAL Y CUERDA CON MASA\n")

# Se imprime la tabla de comparación entre cuerda ideal y cuerda con masa.
print(comparacion_cuerdas.round(5))


# 5. GRAFICAR RESULTADOS

# Se crea una figura para comparar aceleración experimental vs masa motriz con cuerda ideal.
plt.figure(figsize=(9, 6))

# Se recorren los montajes disponibles.
for montaje in resumen["Montaje"].unique():

    # Se filtran los datos del montaje actual con cuerda ideal.
    sub = resumen[(resumen["Montaje"] == montaje) & (resumen["Cuerda"] == "Ideal")]

    # Se grafican los puntos experimentales con barras de error.
    plt.errorbar(
        sub["m_motriz_g"],
        sub["a_exp_promedio"],
        yerr=sub["incertidumbre_media"],
        marker="o",
        capsize=5,
        label=f"{montaje}"
    )

# Se etiqueta el eje horizontal.
plt.xlabel("Masa motriz (g)")

# Se etiqueta el eje vertical.
plt.ylabel("Aceleración experimental promedio (m/s²)")

# Se agrega el título de la gráfica.
plt.title("Aceleración experimental con cuerda ideal")

# Se agrega una leyenda para identificar cada montaje.
plt.legend(title="Montaje")

# Se activa la cuadrícula para facilitar la lectura.
plt.grid(True)

# Se ajusta el diseño para evitar superposición de etiquetas.
plt.tight_layout()

# Se muestra la gráfica en pantalla.
plt.show()


# Se crea una figura para comparar aceleración experimental vs masa motriz con cuerda con masa.
plt.figure(figsize=(9, 6))

# Se recorren los montajes disponibles.
for montaje in resumen["Montaje"].unique():

    # Se filtran los datos del montaje actual con cuerda con masa.
    sub = resumen[(resumen["Montaje"] == montaje) & (resumen["Cuerda"] == "Con masa")]

    # Se grafican los puntos experimentales con barras de error.
    plt.errorbar(
        sub["m_motriz_g"],
        sub["a_exp_promedio"],
        yerr=sub["incertidumbre_media"],
        marker="o",
        capsize=5,
        label=f"{montaje}"
    )

# Se etiqueta el eje horizontal.
plt.xlabel("Masa motriz (g)")

# Se etiqueta el eje vertical.
plt.ylabel("Aceleración experimental promedio (m/s²)")

# Se agrega el título de la gráfica.
plt.title("Aceleración experimental con cuerda con masa")

# Se agrega una leyenda para identificar cada montaje.
plt.legend(title="Montaje")

# Se activa la cuadrícula para facilitar la lectura.
plt.grid(True)

# Se ajusta el diseño para evitar superposición de etiquetas.
plt.tight_layout()

# Se muestra la gráfica en pantalla.
plt.show()


# Se crea una figura para comparar aceleración teórica ideal contra aceleración experimental.
plt.figure(figsize=(9, 6))

# Se recorren los tipos de cuerda disponibles.
for cuerda in resumen["Cuerda"].unique():

    # Se filtran los datos del tipo de cuerda actual.
    sub = resumen[resumen["Cuerda"] == cuerda]

    # Se grafican los puntos de aceleración teórica vs aceleración experimental.
    plt.scatter(
        sub["a_teo_ideal"],
        sub["a_exp_promedio"],
        label=cuerda
    )

# Se calcula el valor máximo para construir la línea de referencia ideal.
max_val = max(resumen["a_teo_ideal"].max(), resumen["a_exp_promedio"].max())

# Se dibuja la línea de referencia donde a experimental sería igual a a teórica.
plt.plot([0, max_val], [0, max_val], linestyle="--", label="Referencia: $a_{exp}=a_{teo}$")

# Se etiqueta el eje horizontal.
plt.xlabel("Aceleración teórica ideal (m/s²)")

# Se etiqueta el eje vertical.
plt.ylabel("Aceleración experimental promedio (m/s²)")

# Se agrega el título de la gráfica.
plt.title("Comparación entre modelo ideal y datos experimentales")

# Se agrega una leyenda para identificar cuerda ideal y cuerda con masa.
plt.legend(title="Tipo de cuerda")

# Se activa la cuadrícula para facilitar la lectura.
plt.grid(True)

# Se ajusta el diseño para evitar superposición de etiquetas.
plt.tight_layout()

# Se muestra la gráfica en pantalla.
plt.show()


# Se crea una figura para mostrar la reducción porcentual al usar cuerda con masa.
plt.figure(figsize=(11, 6))

# Se construyen etiquetas combinando montaje y número de tuercas.
etiquetas = (
    comparacion_cuerdas["Montaje"]
    + " - "
    + comparacion_cuerdas["Tuercas_motriz"].astype(str)
    + " tuercas"
)

# Se grafica la reducción porcentual como barras.
plt.bar(etiquetas, comparacion_cuerdas["reduccion_%"])

# Se rota el texto del eje x para que no se superponga.
plt.xticks(rotation=75, ha="right")

# Se etiqueta el eje horizontal.
plt.xlabel("Configuración experimental")

# Se etiqueta el eje vertical.
plt.ylabel("Reducción de aceleración (%)")

# Se agrega el título de la gráfica.
plt.title("Reducción de aceleración al usar cuerda con masa")

# Se activa la cuadrícula solo en el eje y.
plt.grid(axis="y")

# Se ajusta el diseño para evitar superposición de etiquetas.
plt.tight_layout()

# Se muestra la gráfica en pantalla.
plt.show()


# Se crea una figura para mostrar el error relativo por configuración.
plt.figure(figsize=(11, 6))

# Se construyen etiquetas para cada condición experimental.
etiquetas_error = (
    resumen["Montaje"]
    + " - "
    + resumen["Cuerda"]
    + " - "
    + resumen["Tuercas_motriz"].astype(str)
    + " tuercas"
)

# Se grafica el error relativo porcentual.
plt.bar(etiquetas_error, resumen["error_relativo_%"])

# Se rota el texto del eje x para que sea legible.
plt.xticks(rotation=80, ha="right")

# Se etiqueta el eje horizontal.
plt.xlabel("Configuración experimental")

# Se etiqueta el eje vertical.
plt.ylabel("Error relativo (%)")

# Se agrega el título de la gráfica.
plt.title("Error relativo respecto al modelo ideal")

# Se activa la cuadrícula solo en el eje y.
plt.grid(axis="y")

# Se ajusta el diseño para evitar superposición de etiquetas.
plt.tight_layout()

# Se muestra la gráfica en pantalla.
plt.show()


# 6. INTERPRETACIÓN AUTOMÁTICA BÁSICA

# Se imprime un encabezado para la interpretación.
print("\nINTERPRETACIÓN GENERAL\n")

# Se verifica si todas las condiciones rechazan la hipótesis nula.
if resumen["rechaza_H0"].all():

    # Se imprime la conclusión si todas rechazan el modelo ideal.
    print("En todas las condiciones se rechaza H0: la aceleración experimental difiere significativamente del modelo ideal.")

# Si no todas las condiciones rechazan la hipótesis nula.
else:

    # Se imprime la conclusión si algunas condiciones no rechazan el modelo ideal.
    print("Algunas condiciones no rechazan H0: en esos casos el modelo ideal puede considerarse compatible con los datos.")

# Se verifica si todas las comparaciones entre cuerdas son significativas.
if comparacion_cuerdas["diferencia_significativa"].all():

    # Se imprime la conclusión si la cuerda con masa cambia significativamente la aceleración.
    print("La comparación entre cuerda ideal y cuerda con masa muestra diferencias significativas en todas las configuraciones comparables.")

# Si no todas las comparaciones entre cuerdas son significativas.
else:

    # Se imprime la conclusión si alguna comparación no es significativa.
    print("No todas las comparaciones entre cuerda ideal y cuerda con masa resultaron estadísticamente significativas.")