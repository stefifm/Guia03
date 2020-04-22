print("Fecha por día, mes y año")

#datos

# dia = int(input("Día: "))
# mes = int(input("Mes: "))
# año = int(input("Año: "))

fecha =input("Ingrese fecha en formato aa/aa/aaaa: " )

#proceso

dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
año = fecha[6] + fecha[7] + fecha[8] + fecha[9]

#resultado
print("Día:", dia, "- Mes:", mes, "- Año:", año)

