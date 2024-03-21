FROM python:3.10-slim

WORKDIR Workspace/
COPY . .

RUN python -m pip install --no-cache-dir pip-tools
RUN cd sources/ && pip-compile --output-file=requirements.in
RUN pip install --no-cache-dir -r sources/requirements.in

RUN useradd -m appuser
RUN chown -R appuser /Workspace
USER appuser

EXPOSE 7860
ENTRYPOINT [ "python", "sources/main.py" ]