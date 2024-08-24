#!/bin/bash

for k in {1..30}
do
    echo "Running iteration $k..."
    python generate.py $1
done

echo "Removing duplicates..."
python remove_duplicates.py $1
