# FPY-1101 Evaluacion 2 - Forma A - Calidad: REGULAR
# Nota esperada: 3.5-5.5
# Criterios: IE 2.1.1, IE 2.1.2, IE 2.1.3, IE 2.2.1, IE 2.2.2, IE 2.3.1, IE 2.3.2
# Generado para testing de evaluacion LLM - Sistema DUOC UC

# Sistema de calculo de beneficios estudiantiles
# Codigo con errores parciales - sin ciclos ni excepciones

def main():
    # IE 2.1.1: Variables inicializadas parcialmente
    ARANCEL = 2200000
    # Falta inicializar MATRICULA

    # IE 2.1.3: Entrada de datos incompleta
    promedio = float(input("Promedio: "))
    quintil = int(input("Quintil: "))
    # Falta solicitar nombre

    # IE 2.3.1: Validacion con errores sintacticos menores
    if promedio < 1:
        print("Error promedio")
    # Falta validar limite superior y quintil

    # IE 2.2.1 y IE 2.3.2: Calculo con errores logicos
    descuento = 0

    if promedio > 6.0:
        descuento = 0.20  # Valor incorrecto, deberia ser 0.25 o 0.30
    elif promedio > 5.0:
        descuento = 0.10
    # Faltan condiciones para quintil - error logico

    # IE 2.1.2: Actualizacion incompleta
    arancel_final = ARANCEL * (1 - descuento)
    # Falta calcular matricula y total

    # IE 2.1.3: Salida parcial
    print(f"Arancel: {arancel_final}")
    # Falta mostrar matricula, total, ahorro

if __name__ == "__main__":
    main()
