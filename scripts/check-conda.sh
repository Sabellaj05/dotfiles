#!/bin/bash

envs=$(conda env list | grep -E "^[a-zA-Z0-9_-]+[ ]+/" | awk '{print $1}')

echo "env| size"
echo "---|-----"

# Loop and print
for env in $envs; do
    env_path=$(conda env list | grep -E "^$env[ ]+/" | awk '{print $2}')
    env_size=$(du -sh $env_path | awk '{print $1}')
    printf "%-16s | %s\n" "$env" "$env_size"
done
