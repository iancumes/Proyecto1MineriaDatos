# Reporte EDA - Divorcios en Guatemala

- Fecha de ejecucion: 2026-02-09 21:33:37
- Archivo analizado: `datos_unificadosF.csv`

## 1) Descripcion general del conjunto de datos
- Observaciones (filas): **69,944**
- Variables originales: **45**
- Variables canonicas (tras unificacion): **26**
- Cobertura temporal por anio de registro: **2010 - 2023**
- Archivos de origen detectados: **12**

## 2) Significado y tipo de cada variable
Se genero el archivo `diccionario_variables.csv` con descripcion, tipo sugerido, completitud y columnas de origen utilizadas para cada variable.

| Variable | Tipo | Descripcion |
|---|---|---|
| `depreg` | categorica | Departamento donde se registro el divorcio (codigo INE). |
| `mupreg` | categorica | Municipio donde se registro el divorcio (codigo INE). |
| `mesreg` | numerica_discreta | Mes de registro del divorcio. |
| `anoreg` | numerica_discreta | Anio de registro del divorcio. |
| `diaocu` | numerica_discreta | Dia de ocurrencia del divorcio. |
| `mesocu` | numerica_discreta | Mes de ocurrencia del divorcio. |
| `anoocu` | numerica_discreta | Anio de ocurrencia del divorcio. |
| `depocu` | categorica | Departamento de ocurrencia del divorcio (codigo INE). |
| `mupocu` | categorica | Municipio de ocurrencia del divorcio (codigo INE). |
| `edadhom` | numerica_discreta | Edad del hombre al momento del divorcio. |
| `edadmuj` | numerica_discreta | Edad de la mujer al momento del divorcio. |
| `gethom` | categorica | Codigo de grupo etnico del hombre (catalogo INE). |
| `getmuj` | categorica | Codigo de grupo etnico de la mujer (catalogo INE). |
| `nachom` | categorica | Codigo de nacionalidad del hombre (catalogo INE). |
| `nacmuj` | categorica | Codigo de nacionalidad de la mujer (catalogo INE). |
| `eschom` | categorica | Codigo de escolaridad del hombre (catalogo INE). |
| `escmuj` | categorica | Codigo de escolaridad de la mujer (catalogo INE). |
| `ocuhom` | categorica | Codigo de ocupacion del hombre (catalogo INE / CIUO). |
| `ocumuj` | categorica | Codigo de ocupacion de la mujer (catalogo INE / CIUO). |
| `puehom` | categorica | Codigo de pueblo o pertenencia del hombre (catalogo INE). |
| `puemuj` | categorica | Codigo de pueblo o pertenencia de la mujer (catalogo INE). |
| `ciuohom` | categorica | Codigo CIUO resumido para ocupacion del hombre. |
| `ciuomuj` | categorica | Codigo CIUO resumido para ocupacion de la mujer. |
| `pperhom` | categorica | Codigo adicional de pertenencia del hombre (catalogo INE). |
| `ppermuj` | categorica | Codigo adicional de pertenencia de la mujer (catalogo INE). |
| `origen_archivo` | texto | Archivo .sav de origen desde donde se tomo el registro. |

## 3) Cantidad de variables y observaciones
- Total de observaciones: **69,944**
- Total de variables para analisis: **26**
- Nota: se consolidaron columnas repetidas por cambios historicos de nomenclatura.

## 4) Exploracion de variables numericas
El archivo `resumen_numericas.csv` incluye medidas de tendencia central (media, mediana, moda), dispersion (varianza, desviacion estandar, rango, IQR), orden (Q1, Q3, percentiles) y forma (asimetria, curtosis).

| Variable | n validos | Media | Mediana | Moda | Min | Q1 | Q3 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `mesreg` | 69944 | 6.58 | 7 | 10 | 1 | 4 | 10 | 12 |
| `anoreg` | 69944 | 2016.52 | 2017 | 2022 | 2010 | 2013 | 2019 | 2023 |
| `diaocu` | 69944 | 15.72 | 16 | 18 | 1 | 8 | 23 | 31 |
| `mesocu` | 69944 | 6.33 | 6 | 10 | 1 | 3 | 9 | 12 |
| `anoocu` | 53670 | 2017.30 | 2018 | 2022 | 2010 | 2015 | 2020 | 2022 |
| `edadhom` | 32830 | 35.85 | 34 | 31 | 15 | 29 | 41 | 96 |
| `edadmuj` | 32968 | 32.58 | 31 | 27 | 14 | 26 | 38 | 80 |

## 5) Exploracion de variables categoricas
Se generaron tablas de frecuencia en `tablas_frecuencia/` para cada variable categorica (frecuencia absoluta y porcentaje).

### Departamentos con mas divorcios registrados (depreg)
| Codigo | Departamento | Frecuencia | Porcentaje |
|---:|---|---:|---:|
| 1 | Guatemala | 27308 | 39.04% |
| 9 | Quetzaltenango | 5343 | 7.64% |
| 5 | Escuintla | 3201 | 4.58% |
| 22 | Jutiapa | 2722 | 3.89% |
| 12 | San Marcos | 2654 | 3.79% |
| 10 | Suchitepequez | 2368 | 3.39% |
| 13 | Huehuetenango | 2229 | 3.19% |
| 18 | Izabal | 2208 | 3.16% |

### Escolaridad (codigos) mas frecuentes
Hombre (`eschom`):
- codigo 9: 36079 (51.58%)
- codigo 4: 11120 (15.90%)
- codigo 1: 8533 (12.20%)
- codigo 2: 5850 (8.36%)
- codigo 3: 4600 (6.58%)
- codigo 5: 3230 (4.62%)
Mujer (`escmuj`):
- codigo 9: 35655 (50.98%)
- codigo 4: 11559 (16.53%)
- codigo 1: 8963 (12.81%)
- codigo 2: 5578 (7.97%)
- codigo 3: 4644 (6.64%)
- codigo 5: 2964 (4.24%)

## 6) Relaciones entre variables
Se crearon tablas de relacion en `tablas_relaciones/` con:
- divorcios por anio
- divorcios por departamento
- edades promedio por anio
- correlaciones (Pearson y Spearman)
- tabla cruzada escolaridad hombre vs mujer
- tabla cruzada grupo etnico hombre vs mujer

- Anio con mas divorcios registrados: **2022** con **8,446** casos.
- Brecha media de edad (hombre - mujer): **3.20** anios (n pares: 30,222).

## 7) Graficas generadas
- No se generaron graficas (matplotlib no disponible en el entorno).

## Nota metodologica
Los codigos de catalogos INE (por ejemplo etnia, escolaridad, nacionalidad, ocupacion y pertenencia) se reportan como codigos. Para traducir cada codigo a su etiqueta textual oficial se recomienda anexar el diccionario/codigo oficial del INE.
