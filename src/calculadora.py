"""
Calculadora Simple - Repositorio de Práctica MDW101

Este archivo es para practicar:
- Crear conflictos de merge (modificar la misma función)
- Resolución de conflictos
- Code review en Pull Requests

Autor: MDW101 - Control de Versiones
Fecha: Enero 2026
"""


def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Resta el segundo número del primero."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números."""
        resultado = a * b 
    return resultado


def dividir(a: float, b: float) -> float:
    """
    Divide el primer número entre el segundo.
    
    Raises:
        ValueError: Si el divisor es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# ============================================================
# EJERCICIO PARA EL TALLER DEL SÁBADO
# ============================================================
# 
# Durante el taller, ambos miembros de la pareja modificarán
# la misma función para generar un conflicto de merge.
#
# Persona A: Modificar la función 'potencia' de una forma
# Persona B: Modificar la función 'potencia' de otra forma
#
# Luego resolverán el conflicto juntos.
# ============================================================

def potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.
    
    EJERCICIO: Esta función será modificada por ambos
    miembros de la pareja para practicar conflictos.
    """
    return base ** exponente


def raiz_cuadrada(numero: float) -> float:
    """
    Calcula la raíz cuadrada de un número.
    
    Raises:
        ValueError: Si el número es negativo.
    """
    if numero < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return numero ** 0.5


# ============================================================
# MAIN - Para pruebas rápidas
# ============================================================

if __name__ == "__main__":
    print("=== Calculadora MDW101 ===")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 * 7 = {multiplicar(6, 7)}")
    print(f"20 / 4 = {dividir(20, 4)}")
    print(f"2 ^ 8 = {potencia(2, 8)}")
    print(f"√16 = {raiz_cuadrada(16)}")
