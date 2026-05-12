#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Melany Nikol Plata Amado"
edad = 14
estatura = 1.60
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("dnd._mel", "mel_nik_0")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "The Abbys", "artista": "The Weeknd", "duracion": "4:43"},
{"titulo": "No Pole", "artista": "Don Toliver", "duracion": "3:08"},
{"titulo": "they don't know 'bout us", "artista": "BTS", "duracion": "2:45"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
