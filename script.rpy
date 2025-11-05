image blackout = Solid("#000")  # Pantalla negra


 # Personajes con sus imagenes
default puntos_pytu = 0
define nrr = Character("Narrador", color = "#ffffcc")
define a = Character("Arandu", color = "#f82b10")
define t = Character("Tupa", color = "#1ad1ff")
define p = Character("Pytu",color = "#33ffbb")
define g = Character("Guara", color = "#66ffff")

image arandu = "Arandu_normal.png"
image tupa = "tupa_pensativo.png"
image pytu = "pytu_enojado.png"
image guara = "guara_alegre.png"


default menuset = set()


label start:
    scene blackout
    with fade
    play music "musica_intro.mp3"
    scene start
    $ nombre_jugador = renpy.input("Escribe tu nombre")

    if nombre_jugador == " ":
        $ nombre_jugador = "Jugador"

        "Mucho gusto [nombre_jugador]."

    nrr "Dejenme ponerte en contexto [nombre_jugador] vale?"
    nrr "En el principio no hubo luz ni sombra, ni palabra ni eco. Solo un vacío inmenso, tan silencioso que parecía contener todos los sonidos posibles."
    nrr "De esa nada primordial surgió el primer suspiro del universo, y con él, los cuatro pilares que lo sostendrían por toda la eternidad... "
    
    #--- Mostramos uno a uno los dioses
    show arandu at left with moveinleft:
        zoom 0.5
    nrr "Arandú, la sabiduría que da forma al pensamiento"
    show tupa at right with moveinright:
        zoom 0.5
    nrr "Tupã, el orden que gobierna el equilibrio"
    transform slide_in:
        xpos -0.5      # start off-screen left
        ypos 0       # vertical center
        linear 0.5 xpos 0.25   # move to target horizontal position

    show pytu at slide_in
    nrr "Pytû, el caos que engendra movimiento"
    
    transform slide_in_r:
        xpos 1.5      # start off-screen left
        ypos 0       # vertical center
        linear 0.5 xpos 0.55  # move to target horizontal position

    show guara at slide_in_r:  # middle-right
        zoom 1.2
    nrr "y Guará, el destino que entrelaza todo lo que fue y será."
    #---

    nrr "Así comenzó la historia del cosmos, cuando el silencio decidió hablar."
    nrr "Que esperara a nuestro protagonista en este mundo tan particular?"
    stop music
    jump capitulo1


label capitulo1:
    scene blackout
    play music "univero_intro.mp3" noloop
    centered "=== CAPÍTULO 1 — ARANDU, DIOS DEL SABIDURIA ==="
    stop music
    scene espacio
    show blackout onlayer screens
    $ renpy.with_statement(None)

    #--- Efecto de parpadeo cuando el jugador despierta
    show blackout onlayer screens:
        alpha 1.0
        linear 0.4 alpha 0.0    
        linear 0.6 alpha 1.0    
        linear 3.0 alpha 0.0   
    with None
    #---
    nrr "Lentamente abres los ojos..."
    "[nombre_jugador]" "Ugh... Que hora es? Donde estoy?"

    #--- Efecto de rayo 
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    #---
            
    show arandu at center:
        zoom 0.5
    with dissolve
    with Fade(2.0, 0.0, 0.0)
    "[nombre_jugador]" "Que es eso?!"

    a "No temas. No estoy aquí para dominarte. Estoy aquí para abrir tus ojos"
    a "Voy a hacerte unas preguntas y las respuestas que des determinaran tu destino"
    "[nombre_jugador]" "No entiendo bien la situacion pero supongo que no tengo opcion"


    jump cap1pre1

#--- Preguntas del primer capitulo
menu cap1pre1:
    set menuset  
    a "Si un algoritmo tarda 2 segundos en procesar 1 dato y 6 segundos en procesar 3 datos, su complejidad es:"
    "Lineal":
        a "Incorrecto. No puedes asumir la complejidad sin conocer más sobre el algoritmo."
        jump cap1pre1
    "Exponencial":
        a "Incorrecto. No puedes asumir la complejidad sin conocer más sobre el algoritmo."
        jump cap1pre1
    "Depende de la magnitud y operaciones internas":
        a "CORRECTO, has comprendido que no se puede determinar la complejidad solo con esos datos."
        jump cap1pre2

menu cap1pre2:
    set menuset
    a "Si un error aparece justo antes de entregar el proyecto, ¿qué haces?"
    "Busco culpables":
        "Incorrecto, eso solo trae mas problemas"
        jump cap1pre2
    "Ignoro y entrego igual":
        "Incorrecto, eso solo trae mas problemas"
        jump cap1pre2
    "Analizo el impacto y propongo una solucion rapida":
        a "CORRECTO, es la respuesta mas responsable"
        jump capitulo2
#---

label capitulo2:
    play music "univero_intro.mp3" noloop
    scene blackout
    centered "=== CAPÍTULO 2 — TUPÃ, DIOS DEL ORDEN ==="
    stop music
    scene espacio
    with fade

    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)



            
    show tupa at center:
        zoom 0.5
    with dissolve


    t "El orden protege. Sin reglas, todo se destruye."
    t "¿Qué es indispensable en un equipo de programación?"
    jump cap2pre1

#--- Preguntas del segundo capitulo
menu cap2pre1:
    set menuset
    "Cada quien trabaja por su cuenta":
        t "Incorrecto: El caos sin guía destruye incluso al más fuerte."
        jump cap2pre1
    "Comunicación clara y roles definidos":
        t "Correcto: Sin comunicación, no hay código que funcione."
        jump cap2pre2
    "Que nadie cuestione al líder":
        t "Incorrecto: El caos sin guía destruye incluso al más fuerte."
        jump cap2pre1


menu cap2pre2:
    t "Encuentras un fallo que te beneficia pero afecta al proyecto. ¿Qué haces?"
    set menuset
    "Lo uso":
        t "El orden se pierde cuando la ética se rompe."
        jump cap2pre2
    "Lo reporto":
        t "Correcto: Has ganado el poder del CONTROL."    
        t "El orden siempre recompensa al justo."
        t "Puedes avanzar."
        jump capitulo3
    "Lo ignoro":
        t "Incorrecto: El orden se pierde cuando la ética se rompe."
        jump cap2pre2
#---


label capitulo3:
    play music "univero_intro.mp3" noloop
    scene blackout
    centered "=== CAPÍTULO 3 — PYTU, DIOS DEL CAOS ==="
    stop music
    scene espacio
    with fade

    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)
    show expression Solid("#FFFFFF") as flash
    with Pause(0.1)
    hide flash
    with Pause(0.1)


            
    show pytu at center:
        zoom 1.1
    with dissolve
    p "Buenas caballero, que te trae por aqui?"
    "Tenia mucho miedo, no me podia mover..."
    p "Que pasa? Tanto miedo doy? No importa, sabes para que estas aqui no?"
    "Asiento temeroso"
    p "Es un placer oir eso, ahora, en que te guias para tomar decisiones?"

#--- Preguntas del tercer capitulo
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
#---

label capitulo4:
    play music "univero_intro.mp3" noloop
    scene blackout
    with fade
    centered "=== CAPÍTULO 4 — GUARÁ, DIOS DEL DESTINO ===" 
    scene espacio
    stop music
    show guara
    with dissolve
    show guara at right 
    with moveinright
    g "Todo está escrito. Incluso tú."


label antes_p1:
    show guara at right
    with dissolve

#--- Preguntas del cuarto capitulo
menu p1: 
    set menuset
    g "Una mujer busca venganza por la muerte de su hijo. Mata al asesino y deja huérfano a otro niño. ¿Qué ha logrado?"
    "Justicia":
        jump p1_fail_1
    "Equilibrio":
        jump p1_fail_2
    "Continuar con el ciclo que la llevo a esta situación":
        jump p1_ok

label p1_fail_1:
    hide guara
    show guara at right 
    with dissolve
    g "¿Justicia? Hm... así lo creen los mortales, cuando el dolor los ciega."
    g "¿Puede llamarse justo un acto que engendra el mismo llanto que intenta apagar?"
    jump antes_p1

label p1_fail_2:
    hide guara
    show guara at right 
    with dissolve
    g "Equilibrio... una palabra noble, pero mal comprendida.
    Lo que ella hizo no fue balancear el mundo, sino repetirlo."
    g "El orden verdadero no surge del reflejo del dolor, sino de su ruptura."
    jump antes_p1
    
label p1_ok:
    hide guara at right
    show guara at center
    with move
    g "Ah... ves más allá del velo."
    g "El hilo que una vez la ató al dolor, ella misma lo tejió de nuevo."
    g "Así nacen los bucles eternos: de corazones que confunden justicia con redención"
    g "Solo cuando el odio se extingue, el destino encuentra un nuevo patrón."
    hide guara at center
    show guara at right
    with move
    jump p2


menu p2:
    
    set menuset
    g "¿El futuro está decidido?"

    "Sí.":
        jump p2_fail_1

    "No, lo decido yo.":
        jump p2_ok

    "¿Que es el futuro?":
        jump p2_fail_2

label p2_fail_1:
    g "“Faber est suae quisque fortunae.” Appius Claudius Caecus. III A.C."
    g "Significa que cada quien es el propio arquitecto de su futuro..."
    "Tiene sentido."
    g "Vuelve a intentarlo."

    jump p2
label p2_fail_2:
    g "El futuro… es una de las más sutiles ilusiones que la mente humana ha inventado."
    g "No existe como un lugar al que vayamos, ni como un tiempo que esté aguardándonos..."
    g "... el futuro es apenas una proyección de la conciencia, un intento de darle forma a lo que todavía no es."
    "Fua... Me dejo pensando"
    hide guara
    show guara at right
    with dissolve
    g "Vuelve a intentarlo."
    jump p2

label p2_ok:
    hide guara at right
    show guara at center
    with move

    g "Es correcto"
    hide guara 
    show guara at right
    with dissolve
    g "Bueno..."
    g "Creo que haz llegado al final de tu viaje"
    g "Te queda una ultima decisión por tomar, y será una para definir el destino no solo tuyo sino..."
    show guara at right
    with dissolve
    hide guara with dissolve
    show guara at center:
        zoom 1.5
    g "del MUNDO."
    jump final
#---



label final:
    scene blackout
    nrr "Tu sabiduria te ha llevado a este punto, has pasado por mucho y ahora tienes que tomar una ultima decision"
    centered "Para restaurar el equilibrio debes..."
    menu:
        "DESTRUIR TODO":
            "Wow, en serio?"
            $ renpy.movie_cutscene("images/VID_20251105_134206.webm")
            scene blackout
            with fade
            "Felicidades..."
            return
            
        "RECONSTRUIR EL UNIVERSO":
            "Un mundo nuevo... una nueva oportunidad..."
            $ renpy.movie_cutscene("images/1762216753932.webm")
            scene blackout
            with fade
            centered "FELICIDADES, GRACIAS POR JUGAR"
            return 

# label secreto:
#     $ renpy.movie_cutscene("images/shookai-umamusume.webm")