import csv
import json


def csv_to_json(arch_csv_file, arch_json_file):

  # create a dictionary
  data_dict = []

  with open(arch_csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # ahora convierto cada registro en un diccionario
    for row in csv_reader:
      data_dict.append(row)  #  La lisddta de dicionarios por coma

  with open(arch_json_file, 'w') as jsonfile:
    jsonfile.write(json.dumps(data_dict, indent=4))


def json_to_csv(arch_json_file, arch_csv_file):
  # creamos funcion para leer json y convertir json en csv si no existe el archivo csv se crea
  with open(arch_json_file, mode='r') as jsonfile:
    data_dict = json.load(jsonfile)
  with open(arch_csv_file, 'w', newline='') as csvfile:
    fieldnames = data_dict[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dict)


def menu():
  print("1. Convertir CSV a JSON")
  print("2. Convertir JSON a CSV")
  print("3. Salir")
  opcion = input("Seleccione una opción: ")
  return opcion


# ahora creo un bucle para que se repita el menu
while True:
  opcion = menu()
  if opcion == "1":
    arch_csv_file = input('Ingrese la ruta del archivo csv:   ')
    arch_json_file = input('Ingrese ruta del archivo de salida json:  ')
    csv_to_json(arch_csv_file, arch_json_file)
  elif opcion == "2":
    arch_json_file = input('Ingrese ruta del archivo de salida json:  ')
    arch_csv_file = input('Ingrese la ruta del archivo csv:   ')
    json_to_csv(arch_json_file, arch_csv_file)
  elif opcion == "3":
    break
  else:
    print("Opción inválida. Por favor, seleccione una opción válida.")

