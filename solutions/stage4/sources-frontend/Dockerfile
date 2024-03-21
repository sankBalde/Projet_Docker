FROM python:3.10-slim

WORKDIR Workspace/
COPY . .

RUN python -m pip install --no-cache-dir pip-tools
RUN cd sources-frontend/ && pip-compile --output-file=requirements.txt
RUN pip install --no-cache-dir -r sources-frontend/requirements.txt

RUN useradd -m appuser
RUN chown -R appuser /Workspace
USER appuser

EXPOSE 7860
ENTRYPOINT [ "python", "sources-frontend/main.py" ]