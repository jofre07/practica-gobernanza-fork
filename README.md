# Repositorio de Práctica - Semana 3

**MDW101 - Controlador de Versiones**  
Maestría en Diseño Web y Desarrollo de Apps  
ESPAM MFL

---

## Propósito

Este repositorio es para practicar el flujo de colaboración con Git:

1. **Fork** - Crear tu copia personal
2. **Clone** - Descargar a tu máquina
3. **Upstream** - Conectar con el original
4. **Branch** - Crear rama feature
5. **Commit** - Guardar cambios
6. **Push** - Subir a tu fork
7. **Pull Request** - Solicitar integración

---

## Instrucciones

### Paso 1: Fork
Haz clic en el botón **Fork** (esquina superior derecha) para crear una copia en tu cuenta.

### Paso 2: Clone
```bash
git clone git@github.com:TU-USUARIO/practica-gobernanza.git
cd practica-s3
```

### Paso 3: Agregar Upstream
```bash
git remote add upstream git@github.com:mdw101/practica-gobernanza.git
git remote -v
```

### Paso 4: Crear Rama Feature
```bash
git checkout -b feature/tu-nombre
```

### Paso 5: Hacer Cambios
Agrega tu nombre al archivo `CONTRIBUCIONES.md`:
```bash
echo "- Tu Nombre - Fecha" >> CONTRIBUCIONES.md
```

### Paso 6: Commit
```bash
git add CONTRIBUCIONES.md
git commit -m "docs: agregar mi nombre a contribuciones"
```

### Paso 7: Push
```bash
git push -u origin feature/tu-nombre
```

### Paso 8: Pull Request
Ve a GitHub y crea un Pull Request desde tu rama hacia `main`.

---

## Estructura del Repositorio

```
practica-governanza/
├── README.md           # Este archivo
├── CONTRIBUCIONES.md   # Lista de contribuidores
├── .gitignore          # Archivos ignorados
└── src/
    └── calculadora.py  # Código de ejemplo
```

---

## Actividades de la Semana 3

| Día | Actividad |
|-----|-----------|
| Viernes | Fork + Clone + Upstream (asincrónico) |
| Sábado | Taller de conflictos en parejas |
| Domingo | GitFlow avanzado |

---

## Contacto

**Docente:** Mg. John Cevallos Macías  
**Email:** john.cevallos@espam.edu.ec

---

*Repositorio creado para fines educativos - MDW101 Semana 3*
test
test
