from bs4 import BeautifulSoup

# Cargar los archivos
followers_path = "C:\Users\usuario\Desktop\followers_1.html"
following_path = "C:\Users\usuario\Desktop\following.html"

# Leer contenido
with open(followers_path, "r", encoding="utf-8") as f:
    followers_html = f.read()

with open(following_path, "r", encoding="utf-8") as f:
    following_html = f.read()

# Parsear con BeautifulSoup
followers_soup = BeautifulSoup(followers_html, "html.parser")
following_soup = BeautifulSoup(following_html, "html.parser")

# Extraer nombres de usuario
followers = [a.text.strip() for a in followers_soup.find_all("a") if "instagram.com" in a.get("href", "")]
following = [h2.text.strip() for h2 in following_soup.find_all("h2")]

# Determinar a quién sigues pero no te sigue
no_te_siguen = sorted(set(following) - set(followers))

no_te_siguen[:30], len(no_te_siguen)
