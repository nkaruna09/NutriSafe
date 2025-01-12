FROM streamlit/streamlit:latest

COPY install_zbar.sh /install_zbar.sh
RUN chmod +x /install_zbar.sh
RUN /install_zbar.sh

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
