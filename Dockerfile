FROM python:3.12.5-alpine3.20
COPY ./ /src/
WORKDIR /src/
RUN pip install --upgrade pip
RUN pip install mkdocs
RUN pip install mkdocs-material
RUN apk update
RUN apk add git
RUN pip install -r requirements.txt
RUN pip install mkdocs-glightbox
RUN pip install $(mkdocs get-deps)
EXPOSE 8080
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8080"]