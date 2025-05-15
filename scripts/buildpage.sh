#!/bin/bash
function buildpage {
    TITLE=$(head -n 1 "${1}")
    DATE=$(date "+%d %m %y")
   
    cat layout/before.html |  sed "s/href=\"${FILE}\"/& class=\"current\"/" layout/before.html | sed "s/{{TITLE}}/${TITLE}/"
    tail -n +2 ${1}
    
    cat layout/after.html | sed "s/{{DATE}}/${DATE}/"
}

if [[ "${1}" = "" ]]; then # premier argument obligatoire : le nom de la page
    echo "Usage: ${0} PAGE" >&2
    exit 1

elif test ! -f "${1}"; then # et doit correspondre à une page existante
    echo "${0}: error: ${1}: no such file" >&2
    exit 1
    
else # si tout va bien on construit la page dans public/
    FILE="${1#pages/}" 
    buildpage "${1}" > "public/${FILE}"
fi