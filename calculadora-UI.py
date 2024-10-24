import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")

# Variable que almacenará las operaciones
operacion = ""

# Función que actualiza la pantalla cuando se presionan los botones
def presionar_boton(valor):
    global operacion
    operacion += str(valor)
    pantalla_var.set(operacion)

# Función para evaluar la operación matemática
def calcular():
    global operacion
    try:
        resultado = str(eval(operacion))  # evalúa la operación
        pantalla_var.set(resultado)
        operacion = resultado  # se puede seguir operando con el resultado
    except:
        pantalla_var.set("Error")
        operacion = ""

# Función para borrar la pantalla
def limpiar():
    global operacion
    operacion = ""
    pantalla_var.set("")

# Crear una variable para la pantalla
pantalla_var = tk.StringVar()

# Crear la pantalla de la calculadora
pantalla = tk.Entry(ventana, textvariable=pantalla_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

# Crear botones de la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila = 1
columna = 0

# Crear los botones y agregarlos a la ventana
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=calcular).grid(row=fila, column=columna, columnspan=2)
        columna += 1
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=lambda b=boton: presionar_boton(b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Crear botón para limpiar la pantalla
tk.Button(ventana, text="C", padx=20, pady=20, font=("Arial", 18), command=limpiar).grid(row=fila, column=0, columnspan=4)

# Ejecutar la ventana
ventana.mainloop()
