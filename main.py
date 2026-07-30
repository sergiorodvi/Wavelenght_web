import pygame
import math
import random
import os
import sys
import asyncio

# --- BASE DE DATOS DE CATEGORÍAS ---
CATEGORIAS = [
    ("Mala ciudad para vivir de España", "Buena ciudad para vivir de España"),
    ("Mala película", "Buena película"),
    ("Comida asquerosa", "Comida deliciosa"),
    ("Frío", "Calor"),
    ("Trabajo estresante", "Trabajo relajante"),
    ("Poco ético", "Muy ético"),
    ("Grosería", "Amabilidad"),
    ("Inútil", "Útil"),
    ("Canción triste", "Canción alegre"),
    ("Introvertido", "Extrovertido"),
    ("Habilidad inútil", "Superpoder"),
    ("Animal feo", "Animal adorable"),
    ("Deporte aburrido", "Deporte divertido"),
    ("Mal olor", "Buen olor"),
    ("Tema de conversación tabú", "Tema de conversación común"),
    ("Blando", "Duro"),
    ("Sucio", "Impecable"),
    ("Ilegal", "Obligatorio"),
    ("Mala música para una boda", "Buena música para una boda"),
    ("Pequeño", "Gigantesco"),
    ("Para niños", "Para adultos"),
    ("Barato", "Caro"),
    ("Lento", "Veloz"),
    ("Débil", "Fuerte"),
    ("Terrorífico", "No da miedo"),
    ("Comida basura", "Comida sana"),
    ("Peligroso", "Inofensivo"),
    ("Mala persona", "Buena persona"),
    ("Aburrido", "Divertido"),
    ("Invención inútil", "Gran avance de la humanidad"),
    ("Ruidoso", "Silencioso"),
    ("Cosas de pobres", "Cosas de ricos"),
    ("Poco fiable", "Totalmente confiable"),
    ("Poco higiénico", "Muy limpio"),
    ("Hobby barato", "Hobby caro"),
    ("Mal regalo", "Buen regalo"),
    ("Inculto", "Culto"),
    ("Lugar ruidoso", "Lugar de tranquilidad"),
    ("Habilidad entrenada", "Talento natural"),
    ("Mala suerte", "Buena suerte"),
    ("Destino de viaje sobrevalorado", "Destino de viaje infravalorado"),
    ("Mal destino de viaje", "Buen destino de viaje"),
    ("Nombre feo", "Nombre bonito"),
    ("Poco importante para vivir", "Vital para la vida"),
    ("Fruta mala", "Fruta exquisita"),
    ("Malo para la salud", "Bueno para la salud"),
    ("Divertido en grupo", "Divertido a solas"),
    ("Mala altura para chico", "Buena altura para chico"),
    ("Mala altura para chica", "Buena altura para chica"),
    ("Mala fecha de cumpleaños", "Buena fecha de cumpleaños"),
    ("No cuernos", "Cuernos"),
    ("Mala comida al volver de fiesta", "Buena comida al volver de fiesta"),
    ("Gitano", "Payo"),
    ("Canción para llorar", "Canción de fiesta"),
    ("Deporte nada practicado", "Deporte muy practicado"),
    ("Homosexual", "Heterosexual"),
    ("Sólo famoso", "Realmente guapo"),
    ("Menos famoso", "Más famoso"),
    ("Mal momento para un ataque de risa", "Buen momento para un ataque de risa"),
    ("Número sin aura", "Número con aura"),
    ("Mal bocadillo", "Buen bocadillo"),
    ("Mal ingrediente para una pizza", "Buen ingrediente para una pizza"),
    ("Mal trabajo", "Buen trabajo"),
    ("Asignatura fácil", "Asignatura difícil"),
    ("Mala provincia", "Buena provincia"),
    ("Mal villancico de navidad", "Buen villancico de navidad"),
    ("Mal regalo de navidad", "Buen regalo de navidad"),
    ("Hace mal su trabajo", "Hace bien su trabajo"),
    ("Fama local", "Fama mundial"),
    ("Famoso feo", "Famoso guapo"),
    ("Tierra trágame", "Ojalá me ocurriese"),
    ("Sólo lo deseas", "Realmente lo necesitas"),
    ("Deportista que cae mal", "Deportista que cae bien"),
    ("Sobrado", "Humilde"),
    ("Buen disfraz de carnaval", "Mal disfraz de carnaval"),
    ("Buen disfraz de Halloween", "Mal disfraz de Halloween"),
    ("Mal momento de ANHQV/LQSA", "Buen momento de ANHQV/LQSA"),
    ("Mala edad para ser padre", "Buena edad para ser padre"),
    ("Mala edad para ser madre", "Buena edad para ser madre"),
    ("Fácil", "Difícil"),
    ("Mal objeto para defenderte de zombies", "Buen objeto para defenderte de zombies"),
    ("Mal objeto para defenderte de un león", "Buen objeto para defenderte de un león"),
    ("Mal objeto para defenderte de un atracador", "Buen objeto para defenderte de un atracador"),
    ("Mala liga de fútbol", "Buena liga de fútbol"),
    ("Mal sabor de helado", "Buen sabor de helado"),
    ("Mala selección de fútbol", "Buena selección de fútbol"),
    ("Buen pokemon inicial", "Mal pokemon inicial"),
    ("Plan de invierno", "Plan de verano"),
    ("Bebida mala", "Bebida rica"),
    ("Mala razón para hacerte famoso", "Buena razón para hacerte famoso"),
    ("Mal número de personas para salir de fiesta", "Buen número de personas para salir de fiesta"),
    ("Mal animal de reencarnación", "Buen animal de reencarnación"),
    ("Mal personaje de los simpson", "Buen personaje de los simpson"),
    ("Aburrido", "Divertido"),
    ("Secreto inofensivo", "Secreto devastador"),
    ("Tema de conversación incómodo", "Tema de conversación genial"),
    ("Comportamiento inmaduro", "Madurez absoluta"),
    ("Socialmente inaceptable", "Norma social"),
    ("Mal lugar para proponer matrimonio", "Lugar idílico para proponer matrimonio"),
    ("Da miedo pero no debería", "Parece seguro pero es peligroso"),
    ("Mala razón para romper una relación", "Buena razón para romper una relación"),
    ("Tacaño", "Generoso"),
    ("Mala excusa por llegar tarde", "Buena excusa por llegar tarde"),
    ("Peor cosa para decir antes de morir", "Últimas palabras legendarias"),
    ("Mala diferencia de edad", "Buena diferencia de edad"),
    ("Mal país para vivir", "Buen país para vivir"),
    ("Aburrido", "Divertido"),
]

WIDTH, HEIGHT = 1440, 950
CENTER_X, CENTER_Y = 720, 750
RADIUS = 520

# --- Rutas de assets: relativas al proyecto, compatibles con PC y con el
# empaquetado web de pygbag (que ejecuta con el directorio del proyecto como
# working directory, tanto en local como dentro del navegador). ---
FONT_BOLD_PATH = os.path.join("assets", "Roboto-Bold.ttf")
FONT_REG_PATH = os.path.join("assets", "Roboto-Regular.ttf")

MAX_EQUIPOS = 8
MIN_EQUIPOS = 2
MAX_RONDAS = 20
MIN_RONDAS = 1


class Boton:
    """Botón táctil simple: rectángulo + texto, sabe si ha sido pulsado."""
    def __init__(self, rect, texto, font, color=(52, 143, 235), color_texto=(255, 255, 255)):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.font = font
        self.color = color
        self.color_texto = color_texto

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=14)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=14)
        txt = self.font.render(self.texto, True, self.color_texto)
        surface.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                            self.rect.centery - txt.get_height() // 2))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class CampoTexto:
    """Caja de texto táctil. Al tocarla se activa y se puede escribir con el teclado
    (en Android, tocar un campo activo hace aparecer el teclado en pantalla)."""
    def __init__(self, rect, texto_inicial, font, placeholder=""):
        self.rect = pygame.Rect(rect)
        self.texto = texto_inicial
        self.font = font
        self.placeholder = placeholder
        self.activo = False

    def draw(self, surface):
        color_borde = (235, 143, 52) if self.activo else (120, 120, 130)
        pygame.draw.rect(surface, (45, 45, 55), self.rect, border_radius=10)
        pygame.draw.rect(surface, color_borde, self.rect, 3, border_radius=10)
        mostrar = self.texto if self.texto else self.placeholder
        color_txt = (240, 240, 240) if self.texto else (140, 140, 150)
        txt = self.font.render(mostrar, True, color_txt)
        surface.blit(txt, (self.rect.x + 15, self.rect.centery - txt.get_height() // 2))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        if not self.activo:
            return
        if event.type == pygame.TEXTINPUT:
            if len(self.texto) < 18:
                self.texto += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]


class JuegoWavelength:
    def __init__(self):
        pygame.init()

        # En pantallas HiDPI/Retina (típico en móviles, devicePixelRatio 2 o 3)
        # el lienzo se ve borroso si lo dibujamos a la misma resolución "CSS"
        # que ocupa en pantalla: el navegador lo estira para rellenar los
        # píxeles físicos reales. Pedimos más resolución interna en esos casos
        # para que se vea nítido (el tamaño en pantalla no cambia, solo la
        # nitidez). En PC (devicePixelRatio normalmente 1) no afecta.
        dpr = 1.0
        if sys.platform in ("emscripten", "wasi"):
            try:
                from platform import window
                dpr = float(window.devicePixelRatio) or 1.0
            except Exception:
                dpr = 1.0
        dpr = min(dpr, 2.0)  # tope en 2x para no disparar el coste de renderizado

        base_w, base_h = 1280, 844
        # En navegador no existe el concepto de "resolución de escritorio",
        # así que fijamos un tamaño de ventana concreto (misma proporción que
        # el tablero, 1440x950) en vez de pedir pantalla completa con (0, 0).
        self.screen = pygame.display.set_mode(
            (int(base_w * dpr), int(base_h * dpr)), pygame.RESIZABLE
        )
        pygame.display.set_caption("Wavelength")
        self.base_surface = pygame.Surface((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.font_title = self._load_font(64, bold=True)
        self.font_cat = self._load_font(38, bold=True)
        self.font_med = self._load_font(36)
        self.font_small = self._load_font(24)
        self.font_numbers = self._load_font(30, bold=True)
        self.font_button = self._load_font(32, bold=True)

        self.fase = 'SETUP'
        self.num_equipos = 2
        self.num_rondas = 5
        self.campos_nombres = []
        self._construir_setup()

    def _load_font(self, size, bold=False):
        path = FONT_BOLD_PATH if bold else FONT_REG_PATH
        try:
            return pygame.font.Font(path, size)
        except Exception:
            # Si por lo que sea no encuentra la fuente embebida, recurre a la
            # fuente por defecto de pygame (funciona en cualquier plataforma).
            return pygame.font.Font(None, size)

    # ---------------------- PANTALLA DE CONFIGURACIÓN ----------------------

    def _construir_setup(self):
        """(Re)genera los botones y campos de texto de la pantalla de configuración
        según el número de equipos elegido."""
        self.btn_menos_equipos = Boton((WIDTH//2 - 260, 160, 60, 60), "-", self.font_button)
        self.btn_mas_equipos = Boton((WIDTH//2 + 200, 160, 60, 60), "+", self.font_button)

        self.btn_menos_rondas = Boton((WIDTH//2 - 260, 260, 60, 60), "-", self.font_button)
        self.btn_mas_rondas = Boton((WIDTH//2 + 200, 260, 60, 60), "+", self.font_button)

        nombres_previos = [c.texto for c in self.campos_nombres]
        self.campos_nombres = []
        y0 = 370
        for i in range(self.num_equipos):
            texto = nombres_previos[i] if i < len(nombres_previos) else ""
            campo = CampoTexto((WIDTH//2 - 250, y0 + i*80, 500, 60), texto,
                                self.font_med, placeholder=f"Equipo {i+1}")
            self.campos_nombres.append(campo)

        self.btn_empezar = Boton((WIDTH//2 - 150, 850, 300, 80), "EMPEZAR", self.font_button,
                                  color=(52, 183, 143))

    def draw_setup(self):
        self.base_surface.fill((30, 30, 40))
        self.render_text_centered("Configuración de la partida", self.font_title, (240, 240, 240), 40)

        self.render_text_centered(f"Nº de equipos: {self.num_equipos}", self.font_med, (240, 240, 240), 175)
        self.btn_menos_equipos.draw(self.base_surface)
        self.btn_mas_equipos.draw(self.base_surface)

        self.render_text_centered(f"Nº de rondas: {self.num_rondas}", self.font_med, (240, 240, 240), 275)
        self.btn_menos_rondas.draw(self.base_surface)
        self.btn_mas_rondas.draw(self.base_surface)

        for campo in self.campos_nombres:
            campo.draw(self.base_surface)

        self.btn_empezar.draw(self.base_surface)

        self._blit_a_pantalla()

    def handle_setup_event(self, event, pos_img):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn_menos_equipos.clicked(pos_img) and self.num_equipos > MIN_EQUIPOS:
                self.num_equipos -= 1
                self._construir_setup()
            elif self.btn_mas_equipos.clicked(pos_img) and self.num_equipos < MAX_EQUIPOS:
                self.num_equipos += 1
                self._construir_setup()
            elif self.btn_menos_rondas.clicked(pos_img) and self.num_rondas > MIN_RONDAS:
                self.num_rondas -= 1
            elif self.btn_mas_rondas.clicked(pos_img) and self.num_rondas < MAX_RONDAS:
                self.num_rondas += 1
            elif self.btn_empezar.clicked(pos_img):
                self._empezar_partida()
                return
            else:
                # Activa el campo de texto tocado y desactiva el resto
                for campo in self.campos_nombres:
                    campo.activo = campo.clicked(pos_img)
                if any(c.activo for c in self.campos_nombres):
                    pygame.key.start_text_input()
                else:
                    pygame.key.stop_text_input()

        for campo in self.campos_nombres:
            campo.handle_event(event)

    def _empezar_partida(self):
        nombres = []
        for i, campo in enumerate(self.campos_nombres):
            nombres.append(campo.texto.strip() or f"Equipo {i+1}")
        pygame.key.stop_text_input()
        self.equipos = {nombre: 0 for nombre in nombres}
        self.nombres_equipos = list(self.equipos.keys())
        self.max_rondas = self.num_rondas
        self.ronda_actual = 1
        self.turno_idx = 0
        self.iniciar_ronda()

    # ---------------------- LÓGICA DE JUEGO (igual que antes) ----------------------

    def iniciar_ronda(self):
        if self.ronda_actual > self.max_rondas:
            self.fase = 'FIN'
            self.btn_reiniciar = Boton((WIDTH//2 - 150, HEIGHT//2 + 60, 300, 80),
                                        "NUEVA PARTIDA", self.font_button, color=(52, 183, 143))
            return
        self.tema_izq, self.tema_der = random.choice(CATEGORIAS)
        self.target_angle = random.uniform(1, 179)
        self.needle_angle = 90
        self.fase = 'AVISO_PROPOSITOR'
        self.btn_continuar = Boton((WIDTH//2 - 160, HEIGHT - 100, 320, 80), "CONTINUAR", self.font_button)

    def dibujar_texto_ajustado(self, surface, text, rect, font):
        words = text.split(' ')
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if font.size(' '.join(current_line))[0] > rect.width:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))
        y = rect.y
        for line in lines:
            line_surf = font.render(line, True, (240, 240, 240))
            surface.blit(line_surf, (rect.x + (rect.width//2 - line_surf.get_width()//2), y))
            y += font.get_linesize()

    def draw_sector(self, surface, color, start_angle, end_angle, label=None):
        vs, ve = max(0.0, min(180.0, start_angle)), max(0.0, min(180.0, end_angle))
        if vs >= ve:
            return
        pts = [(CENTER_X, CENTER_Y)]
        r = RADIUS - 5
        for a in range(int(vs*10), int(ve*10)+1):
            rad = math.radians(a/10.0)
            pts.append((CENTER_X - r*math.cos(rad), CENTER_Y - r*math.sin(rad)))
        pygame.draw.polygon(surface, color, pts)

        if label:
            mid = math.radians((vs+ve)/2)
            tx, ty = CENTER_X - (RADIUS-40)*math.cos(mid), CENTER_Y - (RADIUS-40)*math.sin(mid)
            lbl = self.font_numbers.render(label, True, (30, 30, 30))
            surface.blit(lbl, (tx-lbl.get_width()//2, ty-lbl.get_height()//2))

    def draw_needle(self, surface, angle):
        rad = math.radians(angle)
        perp = rad + math.pi/2
        b1 = (CENTER_X - 18*math.cos(perp), CENTER_Y - 18*math.sin(perp))
        b2 = (CENTER_X + 18*math.cos(perp), CENTER_Y + 18*math.sin(perp))
        tip = (CENTER_X - (RADIUS-10)*math.cos(rad), CENTER_Y - (RADIUS-10)*math.sin(rad))
        pygame.draw.polygon(surface, (220, 50, 50), [b1, b2, tip])
        pygame.draw.circle(surface, (220, 50, 50), (CENTER_X, CENTER_Y), 15)
        pygame.draw.circle(surface, (240, 240, 240), (CENTER_X, CENTER_Y), 18, 3)

    def draw_ui(self):
        self.base_surface.fill((30, 30, 40))

        px = WIDTH - 350
        pygame.draw.rect(self.base_surface, (45, 45, 55), (px, 20, 330, 120+len(self.equipos)*50), border_radius=15)
        self.base_surface.blit(self.font_small.render(f"Ronda {self.ronda_actual}/{self.max_rondas}", True, (200, 200, 200)), (px+20, 35))
        for i, n in enumerate(self.nombres_equipos):
            col = (255, 255, 100) if i == self.turno_idx and self.fase != 'FIN' else (240, 240, 240)
            txt = self.font_med.render(f"{n}: {self.equipos[n]}", True, col)
            self.base_surface.blit(txt, (px+20, 90+i*50))

        if self.fase == 'FIN':
            self.render_text_centered("¡FIN DE PARTIDA!", self.font_title, (52, 235, 143), HEIGHT//2 - 60)
            ganador = max(self.equipos, key=self.equipos.get)
            self.render_text_centered(f"Gana {ganador} con {self.equipos[ganador]} puntos", self.font_med, (240, 240, 240), HEIGHT//2 + 10)
            self.btn_reiniciar.draw(self.base_surface)
        elif self.fase == 'AVISO_PROPOSITOR':
            self.render_text_centered(f"Turno de: {self.nombres_equipos[self.turno_idx]}", self.font_title, (240, 240, 240), HEIGHT//2-60)
            self.btn_continuar.texto = "VER OBJETIVO"
            self.btn_continuar.draw(self.base_surface)
        else:
            self.draw_sector(self.base_surface, (50, 50, 60), 0, 180)
            if self.fase in ['PROPOSITOR', 'RESULTADO']:
                t = self.target_angle
                self.draw_sector(self.base_surface, (235, 143, 52), t-22.5, t-13.5, "2")
                self.draw_sector(self.base_surface, (52, 183, 235), t-13.5, t-4.5, "3")
                self.draw_sector(self.base_surface, (52, 235, 143), t-4.5, t+4.5, "4")
                self.draw_sector(self.base_surface, (52, 183, 235), t+4.5, t+13.5, "3")
                self.draw_sector(self.base_surface, (235, 143, 52), t+13.5, t+22.5, "2")

            pygame.draw.arc(self.base_surface, (240, 240, 240), (CENTER_X-RADIUS, CENTER_Y-RADIUS, RADIUS*2, RADIUS*2), 0, math.pi, 6)
            pygame.draw.line(self.base_surface, (240, 240, 240), (CENTER_X-RADIUS, CENTER_Y), (CENTER_X+RADIUS, CENTER_Y), 6)

            self.dibujar_texto_ajustado(self.base_surface, self.tema_izq, pygame.Rect(50, CENTER_Y+50, 500, 250), self.font_cat)
            self.dibujar_texto_ajustado(self.base_surface, self.tema_der, pygame.Rect(WIDTH-550, CENTER_Y+50, 500, 250), self.font_cat)

            self.draw_needle(self.base_surface, self.needle_angle)

            if self.fase == 'PROPOSITOR':
                self.btn_continuar.texto = "LISTOS PARA ADIVINAR"
            elif self.fase == 'ADIVINAR':
                self.btn_continuar.texto = "CONFIRMAR RESPUESTA"
            elif self.fase == 'RESULTADO':
                self.btn_continuar.texto = "SIGUIENTE EQUIPO"
            self.btn_continuar.draw(self.base_surface)

        self._blit_a_pantalla()

    def _calcular_escala(self):
        """Calcula el factor de escala y el desplazamiento (offset) para dibujar
        la superficie base (WIDTH x HEIGHT) centrada dentro de la ventana real,
        SIN deformar la proporción (letterboxing: añade barras si hace falta)."""
        ww, wh = self.screen.get_size()
        escala = min(ww / WIDTH, wh / HEIGHT)
        nuevo_w, nuevo_h = int(WIDTH * escala), int(HEIGHT * escala)
        off_x = (ww - nuevo_w) // 2
        off_y = (wh - nuevo_h) // 2
        return escala, nuevo_w, nuevo_h, off_x, off_y

    def _blit_a_pantalla(self):
        """Escala la superficie base manteniendo proporción y la centra en la
        ventana, rellenando el resto con negro (evita el estiramiento)."""
        escala, nuevo_w, nuevo_h, off_x, off_y = self._calcular_escala()
        scaled = pygame.transform.smoothscale(self.base_surface, (nuevo_w, nuevo_h))
        self.screen.fill((0, 0, 0))
        self.screen.blit(scaled, (off_x, off_y))
        pygame.display.flip()

    def render_text_centered(self, text, font, color, y):
        r = font.render(text, True, color)
        self.base_surface.blit(r, (WIDTH//2 - r.get_width()//2, y))

    def _avanzar_fase(self):
        if self.fase == 'AVISO_PROPOSITOR':
            self.fase = 'PROPOSITOR'
        elif self.fase == 'PROPOSITOR':
            self.fase = 'ADIVINAR'
        elif self.fase == 'ADIVINAR':
            self.fase = 'RESULTADO'
            diff = abs(self.needle_angle - self.target_angle)
            pts = 4 if diff <= 4.5 else 3 if diff <= 13.5 else 2 if diff <= 22.5 else 0
            self.equipos[self.nombres_equipos[self.turno_idx]] += pts
        elif self.fase == 'RESULTADO':
            self.turno_idx = (self.turno_idx + 1) % len(self.nombres_equipos)
            if self.turno_idx == 0:
                self.ronda_actual += 1
            self.iniciar_ronda()

    def _pos_a_coords_imagen(self, pos):
        """Convierte una posición de pantalla (mouse/touch) a coordenadas de la
        superficie base (WIDTH x HEIGHT), teniendo en cuenta el letterboxing
        (offset) y el factor de escala real."""
        mx, my = pos
        escala, _, _, off_x, off_y = self._calcular_escala()
        imx = (mx - off_x) / escala
        imy = (my - off_y) / escala
        return imx, imy

    async def run(self):
        dragging = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                    pos_img = self._pos_a_coords_imagen(event.pos)
                else:
                    pos_img = None

                if self.fase == 'SETUP':
                    self.handle_setup_event(event, pos_img)
                    continue

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.fase == 'FIN':
                        if self.btn_reiniciar.clicked(pos_img):
                            self.fase = 'SETUP'
                            self._construir_setup()
                    elif self.btn_continuar.clicked(pos_img):
                        self._avanzar_fase()
                    else:
                        dragging = True
                if event.type == pygame.MOUSEBUTTONUP:
                    dragging = False

            if self.fase == 'ADIVINAR' and dragging:
                mx, my = pygame.mouse.get_pos()
                imx, imy = self._pos_a_coords_imagen((mx, my))
                dx, dy = CENTER_X - imx, CENTER_Y - imy
                if dy > 0:
                    self.needle_angle = max(0, min(180, math.degrees(math.atan2(dy, dx))))

            if self.fase == 'SETUP':
                self.draw_setup()
            else:
                self.draw_ui()
            self.clock.tick(60)
            # Cede el control al navegador en cada frame; imprescindible para
            # que la pestaña no se congele al ejecutarse como WebAssembly.
            await asyncio.sleep(0)


async def main():
    await JuegoWavelength().run()


if __name__ == "__main__":
    asyncio.run(main())
