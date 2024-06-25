import streamlit as st

definition_extensions = {
    "doc": "Document Word",
    "exe": "Executable",
    "txt": "Document Texte",
    "jpeg": "Image JPEG",
    "jpg": "Image JPEG",
    "png": "Image PNG",
    "pdf": "Document PDF",
    "zip": "Archive ZIP",
    "dat": "Fichier de données",
    "json": "Fichier JavaScript",
    "xls": "Fichier Excel",
    "xlsx": "Fichier Excel",
    "py": "Fichier Python",
    "ipynb": "Jupyter Notebook",
    "jar": "Fichier Java"
}


def recuperer_extension(fichier):
    fichier_split = fichier.rsplit(".", 1)
    if len(fichier_split) > 1:
        return fichier_split[-1].lower()
    return None


def definition_extension(extension, definition_ex):
    return definition_ex.get(extension, "Extension non connue")


def recuperer_extension_et_la_definition(my_fichiers):
    resultats = []
    for fichier in my_fichiers:
        ext = recuperer_extension(fichier)
        if ext:
            definition = definition_extension(ext, definition_extensions)
            resultats.append((fichier, definition))
        else:
            resultats.append((fichier, "Aucune extension"))
    return resultats


st.title("Détecteur des extensions de fichiers")
st.markdown("Ce programme détecte les extensions de fichiers et fournit leur description.")


uploaded_files = st.file_uploader("Téléchargez vos fichiers", accept_multiple_files=True)
if uploaded_files:
    user_fichiers = [uploaded_file.name for uploaded_file in uploaded_files]
    st.subheader("Fichiers téléchargés :")
    resultats = recuperer_extension_et_la_definition(user_fichiers)
    for fichier, definition in resultats:
        st.write(f"{fichier} : {definition}")


st.subheader("Ou entrez les noms complets de fichiers manuellement (séparés par des virgules)")
manual_files = st.text_area("Noms de fichiers")
if manual_files:
    user_fichiers = [f.strip() for f in manual_files.split(",")]
    st.subheader("Fichiers ajoutés manuellement :")
    resultats = recuperer_extension_et_la_definition(user_fichiers)
    for fichier, definition in resultats:
        st.write(f"{fichier} : {definition}")

# CSS pour l'apparence
st.markdown("""
    <style>
        .st-ba {
            background-color: #f0f0f0;
        }
        .st-br {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .st-bg {
            background-color: white;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .st-bt {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
            border: none;
        }
        .st-bt:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)


input()
