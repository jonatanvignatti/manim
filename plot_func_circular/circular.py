import numpy as np

from manim import *


class TrigonometriaZill(Scene):
    def construct(self):
        # --- TÍTULO INICIAL ---
        titulo = Text("Trigonometría: Secciones 9.2 y 9.3", color=BLUE)
        subtitulo = Text("Zill & Dewar ", font_size=24).next_to(titulo, DOWN)
        self.play(Write(titulo), FadeIn(subtitulo))
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(subtitulo))

        # --- SECCIÓN 9.2: SENO Y COSENO ---
        sec92 = Title("9.2 Gráficas de Seno y Coseno")
        axes = (
            Axes(
                x_range=[-0.5, 2 * PI + 0.5, PI / 2],
                y_range=[-1.5, 1.5, 1],
                axis_config={"include_tip": True},
            )
            .scale(0.8)
            .shift(DOWN * 0.5)
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Etiquetas de pi en el eje x
        x_labels = VGroup(
            MathTex(r"\pi/2").next_to(axes.c2p(PI / 2, 0), DOWN),
            MathTex(r"\pi").next_to(axes.c2p(PI, 0), DOWN),
            MathTex(r"3\pi/2").next_to(axes.c2p(3 * PI / 2, 0), DOWN),
            MathTex(r"2\pi").next_to(axes.c2p(2 * PI, 0), DOWN),
        )

        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        sin_label = MathTex("y = \\sin(x)", color=YELLOW).to_corner(UR)

        cos_graph = axes.plot(lambda x: np.cos(x), color=WHITE)
        cos_label = MathTex("y = \\cos(x)", color=WHITE).to_corner(UR)

        self.play(Write(sec92))
        self.play(Create(axes), Write(labels), Write(x_labels))

        # Animación del Seno
        self.play(Create(sin_graph), Write(sin_label), run_time=2)
        self.wait(1)

        # Transformación al Coseno
        self.play(
            ReplacementTransform(sin_graph, cos_graph),
            ReplacementTransform(sin_label, cos_label),
        )
        self.wait(2)
        self.play(
            FadeOut(axes),
            FadeOut(cos_graph),
            FadeOut(cos_label),
            FadeOut(x_labels),
            FadeOut(sec92),
        )

        # --- SECCIÓN 9.3: TANGENTE Y ASÍNTOTAS ---
        sec93 = Title("9.3 Gráficas de otras funciones")
        axes_tan = Axes(x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=7, y_length=5)

        # La tangente tiene discontinuidades, graficamos por intervalos
        tan_graph = VGroup()
        for i in range(-1, 1):
            start = -PI / 2 + 0.1 + i * PI
            end = PI / 2 - 0.1 + i * PI
            part = axes_tan.plot(lambda x: np.tan(x), x_range=[start, end], color=GREEN)
            tan_graph.add(part)

        # Asíntotas
        asintotas = VGroup(
            *[
                DashedLine(axes_tan.c2p(x, -4), axes_tan.c2p(x, 4), color=RED)
                for x in [-PI / 2, PI / 2]
            ]
        )

        tan_label = MathTex("y = \\tan(x)", color=GREEN).to_corner(UR)

        # Lista de descripción (Reemplazo de BulletList para evitar NameError)
        desc_tan = (
            VGroup(
                MathTex(r"\bullet \text{ Periodo: } \pi"),
                MathTex(r"\bullet \text{ Asíntotas en } x = \pm \pi/2"),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_corner(DL)
        )

        self.play(Write(sec93))
        self.play(Create(axes_tan))
        self.play(Create(asintotas))
        self.play(Create(tan_graph), Write(tan_label), run_time=3)
        self.play(Write(desc_tan))
        self.wait(3)

        # Limpieza de la sección 9.3
        self.play(
            FadeOut(tan_graph),
            FadeOut(asintotas),
            FadeOut(tan_label),
            FadeOut(desc_tan),
            FadeOut(axes_tan),
            FadeOut(sec93),
        )

        # --- MOSTRAR SCREENSHOT ---
        try:
            # El archivo debe estar en la misma carpeta que el script
            foto_libro = ImageMobject("Screenshot 2026-04-07 at 22.38.08.png")
            foto_libro.scale(1.5)
            caption = Text("Referencia: Zill & Dewar, pág. 493", font_size=20).next_to(
                foto_libro, DOWN
            )

            self.play(FadeIn(foto_libro), Write(caption))
            self.wait(4)
            self.play(FadeOut(foto_libro), FadeOut(caption))
        except:
            print("Imagen no encontrada, saltando al agradecimiento.")

        # --- FINAL ---
        thanks = Text("¡Gracias!", color=BLUE)
        self.play(Write(thanks))
        self.wait(2)
