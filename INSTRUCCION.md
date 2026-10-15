# Instrucciones de despliegue (entorno local)

API REST de estudiantes construida con **Django 6.1** y **Django REST Framework**, con base de datos SQLite.

## Requisitos previos

- **Python 3.12 o superior** (el proyecto se desarrolló con Python 3.14).
- **Git**.

Verifica tu versión:

| Sistema | Comando |
|---------|---------|
| macOS / Linux | `python3 --version` |
| Windows | `python --version` (o `py --version`) |

## 1. Clonar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd DjangoApiEva
```

## 2. Crear el entorno virtual

El entorno virtual (`venv/`) **no se sube a Git**; cada persona crea el suyo.

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (CMD)**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

> Si PowerShell muestra un error de "execution policy", ejecuta una vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Sabrás que está activo cuando veas `(venv)` al inicio de la línea de comandos.

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Crear la base de datos

La base de datos `db.sqlite3` **no se sube a Git**. Se crea localmente aplicando las migraciones:

```bash
python manage.py migrate
```

(Opcional) Crear un usuario administrador para entrar a `/admin/`:

```bash
python manage.py createsuperuser
```

## 5. Levantar el servidor

```bash
python manage.py runserver
```

Si el puerto 8000 está ocupado, usa otro: `python manage.py runserver 8001`.

> En macOS/Linux, si `python` no existe usa `python3`. Con el entorno virtual activo, `python` funciona en todos los sistemas.

## 6. Probar la API

| Recurso | URL |
|---------|-----|
| Panel de administración | http://127.0.0.1:8000/admin/ |
| Raíz de la API | http://127.0.0.1:8000/api/ |
| Estudiantes | http://127.0.0.1:8000/api/estudiantes/ |

Desde el navegador, Django REST Framework ofrece una interfaz para listar, crear, editar y eliminar estudiantes. También puedes usar `curl`, Postman o Insomnia.

## Solución de problemas

| Problema | Solución |
|----------|----------|
| `pip install` falla por la versión de Python | Instala Python 3.12 o superior. |
| `python` no se reconoce (Windows) | Prueba con `py`, o reinstala Python marcando "Add Python to PATH". |
| `No module named django` | El entorno virtual no está activo o no se instalaron las dependencias (pasos 2 y 3). |
| `no such table: estudiantes_estudiantes` | Falta ejecutar `python manage.py migrate`. |
| Git muestra archivos modificados sin cambios reales | Diferencias de saltos de línea; el archivo `.gitattributes` del proyecto lo evita. |

## Archivos que no se versionan

Definidos en `.gitignore`: `venv/`, `__pycache__/`, `db.sqlite3`, `.env`, `media/`, `staticfiles/` y archivos de editor/sistema.

## Actualizar dependencias (para quien agregue paquetes nuevos)

```bash
pip freeze > requirements.txt
```
