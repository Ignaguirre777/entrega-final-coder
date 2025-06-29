# Playground Blog Project

Este es el proyecto final para el curso de Django en Coderhouse.  
Incluye un sistema de blog, gestión de páginas, perfiles de usuario y mensajería interna.

---

---

## 🚀 ¿Qué incluye este proyecto?

- **Blog:** Publica, edita, elimina y visualiza posts.
- **Pages:** Crea y administra páginas informativas.
- **Mensajería:** Envía y recibe mensajes entre usuarios registrados.
- **Perfiles:** Cada usuario puede editar su perfil y ver información personal.
- **Administrador:** Acceso al panel de Django para CRUD completo.
- **Autenticación:** Registro, login y logout de usuarios.
- **Página About:** Información sobre el creador del proyecto.

---

## 🗂️ Estructura principal

- **blog/**  
  Posts y páginas (modelos, vistas, templates).
- **accounts/**  
  Registro, login, perfil de usuario.
- **messenger/**  
  Envío y recepción de mensajes privados.
- **templates/**  
  Base, home, about, y todos los templates de la app.
- **static/**  
  Archivos CSS para el estilo minimalista y moderno.

---

## 🛠️ Instalación y uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicia el servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Accede a la app:**  
   Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.

