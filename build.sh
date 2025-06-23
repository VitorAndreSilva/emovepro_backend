#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o pip
pip install --upgrade pip

# Instala o pdm
pip install pdm

# Instala as dependências
#pip install -r requirements.txt
pdm install

# Coleta os arquivos estáticos
pdm run python manage.py collectstatic --no-input

# Aplica as migrações
pdm run python manage.py migrate