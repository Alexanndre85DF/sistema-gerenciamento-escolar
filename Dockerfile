# Usa uma imagem oficial do Python
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o conteúdo do projeto para dentro do container
COPY . .

# Instala as dependências (garanta que existe requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Define variáveis para rodar o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta usada pelo Render
EXPOSE 10000

# Inicia a aplicação com Gunicorn (altere se necessário)
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
