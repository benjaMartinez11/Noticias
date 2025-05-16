from newspaper import Article

# URL del artículo
url = "https://www.clarin.com/sociedad/primer-paro-gremio-docente-grande-gobierno-axel-kicillof-provincia_0_Ay49JOV85e.html"
article = Article(url)

# Descargar y procesar el artículo
article.download()
article.parse()

# Obtener información
titulo = article.title
autores = ", ".join(article.authors)
fecha = article.publish_date.strftime("%Y-%m-%d") if article.publish_date else "Fecha no disponible"
contenido = article.text

# Mostrar resultados
print(f"Título: {titulo}")
print(f"Autor(es): {autores}")
print(f"Fecha de publicación: {fecha}")
print(f"Contenido:\n{contenido}")
