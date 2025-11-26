import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

intentos_iniciales = 3
intentos = intentos_iniciales
nivel = 1
puntos = 0
total_niveles = 4

preguntas_niveles = {
    1: {
        "pregunta": "¿Cuál es el resultado de una compuerta AND con entradas 1 y 1?",
        "respuesta": "1",
        "tipo": "binaria",
        "explicacion": "La compuerta AND solo devuelve 1 cuando ambas entradas son 1."
    },
    2: {
        "pregunta": "¿Cuál es la compuerta lógica que devuelve 1 si al menos una entrada es 1?",
        "respuesta": "OR",
        "tipo": "multiple",
        "explicacion": "La compuerta OR devuelve 1 si cualquiera de las entradas es 1."
    },
    3: {
        "pregunta": "¿Qué devuelve una compuerta NOT si la entrada es 0?",
        "respuesta": "1",
        "tipo": "binaria",
        "explicacion": "La compuerta NOT invierte la entrada: 0 se vuelve 1."
    },
    4: {
        "pregunta": "¿Qué compuerta lógica devuelve 1 solo si las entradas son diferentes?",
        "respuesta": "XOR",
        "tipo": "multiple",
        "explicacion": "La compuerta XOR devuelve 1 solo si una entrada es 1 y la otra es 0."
    },
}

ventana = tk.Tk()
ventana.title("Minijuego de Compuertas Lógicas")
ventana.geometry("570x450")

label_nivel = tk.Label(ventana, text=f"Nivel: {nivel}", font=("Arial", 14))
label_nivel.pack(pady=5)

label_pregunta = tk.Label(ventana, text="", font=("Arial", 12))
label_pregunta.pack(pady=10)

label_intentos = tk.Label(ventana, text=f"Intentos: {intentos}", font=("Arial", 12))
label_intentos.pack()

label_puntos = tk.Label(ventana, text=f"Puntos: {puntos}", font=("Arial", 12))
label_puntos.pack(pady=5)

progress_label = tk.Label(ventana, text="Progreso:", font=("Arial", 11))
progress_label.pack(pady=5)

progress_bar = ttk.Progressbar(ventana, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)

entrada_respuesta = tk.Entry(ventana, font=("Arial", 12))

opciones = ["AND", "OR", "XOR", "NOT"]
variable_opcion = tk.StringVar(value="")
frame_opciones = tk.Frame(ventana)
botones_opciones = [
    tk.Radiobutton(frame_opciones, text=opc, variable=variable_opcion, value=opc, font=("Arial", 11))
    for opc in opciones
]
for boton in botones_opciones:
    boton.pack(anchor="w")


def cargar_nivel():
    global nivel
    if nivel in preguntas_niveles:
        label_nivel.config(text=f"Nivel: {nivel}")
        label_pregunta.config(text=preguntas_niveles[nivel]["pregunta"])

        tipo = preguntas_niveles[nivel]["tipo"]
        if tipo == "binaria":
            frame_opciones.pack_forget()
            entrada_respuesta.pack(pady=10)
            entrada_respuesta.delete(0, tk.END)
        else:
            entrada_respuesta.pack_forget()
            frame_opciones.pack(pady=10)
            variable_opcion.set("")

        progreso = ((nivel - 1) / total_niveles) * 100
        progress_bar["value"] = progreso
    else:
        progress_bar["value"] = 100
        messagebox.showinfo("🎉 ¡Ganaste!", f"¡Has completado todos los niveles!\nPuntuación final: {puntos}")
        ventana.quit()


def reiniciar_juego():
    global nivel, puntos, intentos
    messagebox.showwarning("❌ Reinicio", "Te has quedado sin intentos. El juego se reinicia.")
    nivel = 1
    puntos = 0
    intentos = intentos_iniciales
    actualizar_pantalla()
    progress_bar["value"] = 0
    cargar_nivel()


def actualizar_pantalla():
    label_intentos.config(text=f"Intentos: {intentos}")
    label_puntos.config(text=f"Puntos: {puntos}")


def verificar_respuesta():
    global nivel, puntos, intentos
    tipo = preguntas_niveles[nivel]["tipo"]
    respuesta_correcta = preguntas_niveles[nivel]["respuesta"]
    explicacion = preguntas_niveles[nivel]["explicacion"]

    respuesta_usuario = entrada_respuesta.get() if tipo == "binaria" else variable_opcion.get()

    if respuesta_usuario == "":
        messagebox.showerror("⚠️ Error", "Debe seleccionar o escribir una respuesta.")
        return

    if respuesta_usuario == respuesta_correcta:
        puntos += 10
        nivel += 1
        messagebox.showinfo("✔️ Correcto", "¡Bien hecho! Avanzas al siguiente nivel.")
    else:
        intentos -= 1
        if intentos > 0:
            messagebox.showerror("❌ Incorrecto", f"Respuesta incorrecta.\n➡ Explicación: {explicacion}\nIntentos restantes: {intentos}")
        else:
            reiniciar_juego()
            return

    actualizar_pantalla()
    cargar_nivel()


boton_enviar = tk.Button(ventana, text="Enviar respuesta", font=("Arial", 12), command=verificar_respuesta)
boton_enviar.pack(pady=15)

cargar_nivel()
ventana.mainloop()
