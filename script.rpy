image blackout = Solid("#000")  # black screen

default puntos_pytu = 0

define nrr = Character("Narrador")
define a = Character(("Arandu"))
define t = Character("Tupa")
define p = Character("Pytu")
define g = Character("Guara")

default menuset = set()



label start:
    scene blackout

    nrr "Dejenme darles un contexto de la situacion vale?"
    nrr "En el principio no hubo luz ni sombra, ni palabra ni eco. Solo un vacío inmenso, tan silencioso que parecía contener todos los sonidos posibles."
    nrr "De esa nada primordial surgió el primer suspiro del universo, y con él, los cuatro pilares que lo sostendrían por toda la eternidad... "

    show a at left with moveinleft
    nrr "Arandú, la sabiduría que da forma al pensamiento"
    show t at right with moveinright
    nrr "Tupã, el orden que gobierna el equilibrio"
    transform slide_in:
        xpos -0.5      # start off-screen left
        ypos 0       # vertical center
        linear 0.5 xpos 0.25   # move to target horizontal position


    show p at slide_in
    nrr "Pytû, el caos que engendra movimiento"
    
    transform slide_in_r:
        xpos 1.5      # start off-screen left
        ypos 0       # vertical center
        linear 0.5 xpos 0.55  # move to target horizontal position

    show g at slide_in_r  # middle-right
    nrr "y Guará, el destino que entrelaza todo lo que fue y será."

    nrr "Así comenzó la historia del cosmos, cuando el silencio decidió hablar."
    nrr "Que esperara a nuestro protagonista en este mundo tan particular?"

    jump capitulo1

label capitulo1:

    # Start with a black screen
    scene bg wakeup
    show blackout onlayer screens
    $ renpy.with_statement(None)

    # Blinking effect
    show blackout onlayer screens:
        alpha 1.0
        linear 0.4 alpha 0.0    # quick open (first blink)
        linear 0.6 alpha 1.0    # blink shut again
        linear 3.0 alpha 0.0    # long slow fade — eyes fully open
    with None


    nrr "Lentamente abres los ojos..."
    "Ugh... Que hora es? Donde estoy?"

    # --- Lightning flash effect ---
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    # --------------------------
    # Lightning explanation:
    # 'Solid("#FFFFFF")' is a completely white screen.
    # We 'show' it briefly to simulate a flash.
    # 'with Pause(0.1)' controls how long the flash appears.
    # Hiding it and flashing again simulates a second lightning strike.
    # --------------------------


            
    show Arandu
    with dissolve
    with Fade(2.0, 0.0, 0.0)
    "Que isso?!"
    # --------------------------
    # 'show mysterious_object at center' puts your object/character sprite on screen.
    # 'with Fade(2.0, 0.0, 0.0)' gradually makes it appear over 2 seconds:
    #    - first parameter (2.0): duration of the fade-in
    #    - next two parameters: fade-out duration and alpha, not used here
    # --------------------------
    a "No temas. No estoy aquí para dominarte. Estoy aquí para abrir tus ojos"
    

    jump cap1pre1


menu cap1pre1:
    set menuset  
    a "Si un algoritmo tarda 2 segundos en procesar 1 dato y 6 segundos en procesar 3 datos, su complejidad es:"
    "Lineal":
        "PLACEHOLDER"
        jump cap1pre1
    "Exponencial":
        "PLACEHOLDER"
        jump cap1pre1
    "Depende de la magnitud y operaciones internas":
        "CORRECTO"
        a "Si un error aparece justo antes de entregar el proyecto, ¿qué haces?"
        jump cap1pre2

menu cap1pre2:
    set menuset
    "Busco culpables":
        "PLACEHOLDER"
        jump cap1pre2
    "Ignoro y entrego igual":
        "PLACEHOLDER"
        jump cap1pre2
    "Analizo el impacto y propongo una solucion rapida":
        jump capitulo2


label capitulo2:
    scene espacio
    with fade

    centered "=== CAPÍTULO 2 — TUPÃ, DIOS DEL ORDEN ==="
    
    show t at center
    t "El orden protege. Sin reglas, todo se destruye."
    # ---------------- PREGUNTA 1 ----------------
    "¿Qué es indispensable en un equipo de programación?"
    jump cap2pre1

menu cap2pre1:
    set menuset
    "Cada quien trabaja por su cuenta":
        ":x: Incorrecto: El caos sin guía destruye incluso al más fuerte."
        jump cap2pre1
    "Comunicación clara y roles definidos":
        ":white_check_mark: Correcto: Sin comunicación, no hay código que funcione."
        jump cap2pre2
    "Que nadie cuestione al líder":
        ":x: Incorrecto: El caos sin guía destruye incluso al más fuerte."
        jump cap2pre1


menu cap2pre2:
    # ---------------- PREGUNTA 2 ----------------
    "Encuentras un fallo que te beneficia pero afecta al proyecto. ¿Qué haces?"
    set menuset
    "Lo uso":
        ":x: Incorrecto: El orden se pierde cuando la ética se rompe."
        jump cap2pre2
    "Lo reporto":
        ":white_check_mark: Correcto: Has ganado el poder del CONTROL."    
        t "El orden siempre recompensa al justo."
        "Puedes avanzar."
        jump capitulo3
    "Lo ignoro":
        ":x: Incorrecto: El orden se pierde cuando la ética se rompe."
        jump cap2pre2



    


label capitulo3:
    p "Buenas caballero, que te trae por aqui?"
    "Tenia mucho miedo, no me podia mover..."
    p "Que pasa? Tanto miedo doy? No importa, sabes para que estas aqui no?"
    "Asiento temeroso"
    p "Es un placer oir eso, ahora, en que te guias para tomar decisiones?"

    menu:
        "En mis impulsos":
            p "PERFECTO justo lo que queria escuchar"
            $ puntos_pytu += 1
        "En la informacion que tengo":
            p "Hmmm... okay"
    p "Bueno ya no tengo preguntas sabes, yo no soy del tipo hablador"
    p "A ver, una ultima pregunta creatura"
    p "Estas en las ultimas, probaste todo lo que podias e igual fallaste, te resbalaste y lo perdiste todo, la gente se rie de ti, que harias"
    menu:
        "Reirme con ellos":
            p "Jajajaja, vaya sujeto eres"
            $ puntos_pytu += 1
        "Irme y cambiar mi enfoque":
            p "Que decepcionante"
    
    p "Las cosas buenas duran poco, vamos a ver tu destino..."
    if puntos_pytu > 1:
        p "FELICIDADES HUMANO puedes pasar jijiji"
        jump capitulo4
    else:
        p "Que pena, te vas a quedar encerrado conmigo"

    return

default puntos_guara = 0
label capitulo4:
    g "Holanda soy Guara"
    g "¿El futuro está decidido?"

menu cap4pre1:
        "Sí.":
            jump p1_fail_1

        "No, lo decido yo.":
            $ puntos_guara +=1
            g "Movimiento naranja el futuro esta en tus manos."
            jump final

        "¿Que es el futuro?":
            jump p1_fail_2

label p1_fail_1:
    g "“Faber est suae quisque fortunae.” Appius Claudius Caecus. III A.C."
    g "Significa que cada quien es el propio arquitecto de su futuro..."
    "Tiene sentido."
    g "Vuelve a intentarlo."

    jump cap4pre1

label p1_fail_2:
    g "El futuro… es una de las más sutiles ilusiones que la mente humana ha inventado."
    g "No existe como un lugar al que vayamos, ni como un tiempo que esté aguardándonos..."
    g "... el futuro es apenas una proyección de la conciencia, un intento de darle forma a lo que todavía no es."
    "Fua... Me dejo pensando"
    hide tupac normal
    show tupac pensativo
    g "Vuelve a intentarlo."
    jump cap4pre1

    


label final:
    "WAZAAAA"   
    g "Para restaurar el equilibrio debes..."
    menu:
        "FINAL 1":
            "xd"
        "final 2":
            "xderlis"
