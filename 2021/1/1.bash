#/bin/bash

measurements=0
last_measurement=$(head -n 1 input.txt | xargs)

while read line; do
    if [[ "$line" -gt "$last_measurement" ]]; then
        ((measurements++))
    fi
    last_measurement=$line
done

echo "$measurements"
