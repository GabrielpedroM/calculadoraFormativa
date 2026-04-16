FROM python:3.12-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia tudo da sua pasta atual para dentro do container
COPY . .

# Comando para executar o script
CMD ["python", "calculadora.py"]