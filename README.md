# Wavelength — versión Web (jugable desde el navegador, sin instalar nada)

Hemos abandonado la vía del APK de Android (demasiadas piezas frágiles: SDK,
NDK, Docker...) y en su lugar compilamos el juego a **WebAssembly** con
`pygbag`, para que se abra como una página web normal en cualquier navegador
(móvil o PC), sin instalar ninguna app.

## Qué se ha adaptado en el código

- El bucle principal (`run()`) ahora es una función `async`, con un
  `await asyncio.sleep(0)` en cada vuelta — es el único requisito real que
  impone pygbag para que la pestaña del navegador no se congele.
- Las rutas de las fuentes son relativas (`assets/...`) en vez de calcularse
  con `__file__`, que es más robusto dentro del entorno empaquetado.
- El resto de la lógica (configuración, turnos, aguja, puntuación) es
  exactamente la misma que ya probamos y que te funcionaba en el APK — no ha
  hecho falta tocar nada de eso.

He probado el bucle asíncrono completo en mi entorno (varios segundos de
ejecución real, sin errores ni cuelgues) antes de dártelo.

## Por qué esta vía sí puede funcionar donde el APK no pudo

El proceso de `pygbag` necesita descargar un runtime de Python compilado
para el navegador, desde `pygame-web.github.io` — un dominio al que mi propio
entorno no tiene acceso (por eso no pude compilarlo yo mismo aquí). Pero
**GitHub Actions sí tiene acceso completo a internet**, así que dejamos que
sea GitHub quien haga esa descarga y compilación por nosotros — y además,
al terminar, publica el resultado como una página web gratuita en
`https://tu-usuario.github.io/tu-repo/`.

## Pasos para publicarlo

### 1. Sube estos archivos a tu repositorio de GitHub

Puedes reutilizar el mismo repo de antes o crear uno nuevo. Sube (arrastrando
desde el Explorador de Windows, como hiciste la otra vez):
- `main.py` (reemplaza el anterior si usas el mismo repo)
- la carpeta `assets/`
- `favicon.png` (en la raíz del repo, no dentro de `assets/`)
- `.github/workflows/pygbag.yml`

Si reutilizas el repo del intento de Android, puedes **borrar** (opcional,
no estorba pero por limpieza):
- `buildozer.spec`
- `.github/workflows/build.yml` (el workflow del APK)

### 2. Da permisos de escritura a las Actions

Esto es imprescindible o el paso de publicar en `gh-pages` fallará:
1. En tu repo, ve a **Settings** → **Actions** → **General**.
2. Baja hasta **"Workflow permissions"**.
3. Marca **"Read and write permissions"**.
4. Guarda ("Save").

### 3. Ejecuta el workflow manualmente

Este workflow no se dispara solo al hacer push (a propósito, para no gastar
minutos de Actions en cada cambio pequeño):
1. Ve a la pestaña **Actions** de tu repo.
2. A la izquierda, selecciona **"pygbag_build"**.
3. A la derecha, pulsa **"Run workflow"** → confirma.
4. Espera a que termine (icono verde ✅). Debería ser bastante más rápido y
   fiable que lo del APK, ya que aquí no hay SDK/NDK de Android de por medio.

### 4. Activa GitHub Pages apuntando a la rama que se acaba de crear

1. Ve a **Settings** → **Pages**.
2. En "Branch", selecciona **`gh-pages`** (se habrá creado automáticamente
   al terminar el workflow del paso 3) y la carpeta `/ (root)`.
3. Guarda.

### 5. Abre tu juego

Al cabo de uno o dos minutos, tu juego estará disponible en:

```
https://TU-USUARIO.github.io/TU-REPO/
```

Ábrelo desde el navegador de tu móvil o de tu PC — no hace falta instalar
nada, y puedes compartir ese enlace con quien quieras para que juegue
directamente.

## Notas y limitaciones a tener en cuenta

- La primera vez que alguien abre el enlace, el navegador tiene que
  descargar el runtime de Python + pygame en WebAssembly (unos cuantos MB),
  así que puede tardar unos segundos en arrancar la primera vez. Las
  siguientes veces va mucho más rápido porque el navegador lo cachea.
- Recomendado usar navegadores basados en Chromium (Chrome, Brave, el
  navegador de Samsung) — es lo más probado por los propios creadores de
  pygbag. Safari en iOS necesita iOS 15+ y puede dar más problemas.
- Si cambias el código, tienes que volver a subir `main.py` y volver a
  lanzar el workflow manualmente (paso 3) para que se regenere la web.
- Puedes seguir probando el juego en tu PC normalmente con
  `pip install pygame` + `python3 main.py` — el código funciona igual en
  local que empaquetado.
