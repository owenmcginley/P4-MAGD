#!/usr/bin/bash
# Script modificado que permite generar y almacenar los ficheros json con un directorio para cada ciudad
# Ejemplo de estructura de directorios:
# json/
# ├── malaga
# ├── mallorca
# │   └── reviews.json
# └── menorca
#     └── reviews.json
# Uso: 
# 1. Hacer el fichero ejecutable:
# chmod u+x db_load_city_files.sh
# 2. Ejecutarlo con el nombre del directorio donde estén los json como argumento, por ej.
# ./db_load_city_files.sh json
#
# Esto cargará todos los ficheros json en los directorios json/mallorca/ json/menorca/... etc
# en colecciones con el mismo nombre que los ficheros (pero sin su extensión)
#
# Con la estructura de arriba, cargará mallorca/reviews.json y menorca/reviews.json 
# en la colección reviews
# Si hay más ficheros json en esos directorios, los cargará igualmente en las colecciones 
# correspondientes

if [ $# -eq 1 ] 
then dir="$1"
    echo Changing dir to "$1"
    saved_dir=`pwd`
else dir=json
fi

cd "$dir"


CITIES=(menorca mallorca malaga)

for city in ${CITIES[@]};
    do cd $city
    echo Processing json for $city 
    files=*.json
    
    for f in $files;
        do coll="${f%.json}"
        echo loading "$f" into collection "$coll"
        mongoimport -d airbnb --collection="$coll" --jsonArray mongodb://localhost:27017/ "$f"
    done

    cd ..
done

if [[ -v saved_dir ]]; then cd "$saved_dir"; fi
