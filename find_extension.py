import streamlit as st

definition_extensions = {
  "doc": "Document Word: DESCRIPTION \n Un fichier créé par Microsoft Word, couramment utilisé pour rédiger et formater des textes, des rapports, des lettres et des articles.",
  "exe": "Fichier Exécutable: DESCRIPTION \n Un fichier contenant un programme informatique exécutable sous Windows, souvent utilisé pour installer ou lancer des logiciels.",
  "txt": "Document Texte: DESCRIPTION \n Un fichier de texte brut sans mise en forme, utilisé pour stocker des informations en texte simple.",
  "jpeg": "Image JPEG: DESCRIPTION \n Un format de fichier d'image compressé couramment utilisé pour stocker des photographies et des images avec une bonne qualité et une taille de fichier réduite.",
  "jpg": "Image JPEG: DESCRIPTION \n Un format de fichier d'image compressé couramment utilisé pour stocker des photographies et des images avec une bonne qualité et une taille de fichier réduite.",
  "png": "Image PNG: DESCRIPTION \n Un format de fichier d'image sans perte de qualité, souvent utilisé pour les graphiques avec des zones transparentes.",
  "pdf": "Document PDF: DESCRIPTION \n Un format de fichier universel créé par Adobe, utilisé pour présenter des documents de manière cohérente indépendamment du logiciel, du matériel ou du système d'exploitation.",
  "zip": "Archive ZIP: DESCRIPTION \n Un fichier compressé qui peut contenir plusieurs fichiers ou dossiers, utilisé pour réduire la taille de stockage et faciliter le transfert.",
  "dat": "Fichier de Données: DESCRIPTION \n Un fichier utilisé pour stocker des données génériques pouvant être utilisées par diverses applications et programmes.",
  "json": "Fichier JSON: DESCRIPTION \n Un format de fichier utilisé pour stocker et échanger des données structurées, principalement utilisé dans le développement web pour les échanges de données entre un serveur et un client.",
  "xls": "Fichier Excel: DESCRIPTION \n Un fichier de feuille de calcul créé par Microsoft Excel, utilisé pour organiser, analyser et stocker des données sous forme de tableaux.",
  "xlsx": "Fichier Excel: DESCRIPTION \n Un fichier de feuille de calcul au format XML créé par Microsoft Excel, offrant des fonctionnalités avancées de gestion de données.",
  "py": "Fichier Python: DESCRIPTION \n Un fichier script contenant du code écrit en langage de programmation Python, utilisé pour automatiser des tâches, analyser des données ou développer des applications.",
  "ipynb": "Jupyter Notebook: DESCRIPTION \n Un fichier contenant du code Python exécutable, des visualisations, et du texte formaté, utilisé pour le développement interactif, l'analyse de données et le partage de recherches.",
  "jar": "Fichier Java: DESCRIPTION \n Un fichier archive Java contenant des classes Java compilées et des métadonnées nécessaires à l'exécution d'applications développées en Java.",
  "css": "Fichier CSS: DESCRIPTION \n Un fichier de feuille de style en cascade utilisé pour définir l'apparence et la mise en page des pages web, en contrôlant les couleurs, les polices, les espacements, et d'autres aspects visuels.",
  "html": "Fichier HTML: DESCRIPTION \n Un fichier de langage de balisage hypertexte utilisé pour créer la structure et le contenu des pages web, en définissant les éléments tels que les titres, les paragraphes, les liens, et les images.",
  "ppt": "Fichier PowerPoint: DESCRIPTION \n Un fichier de présentation créé par Microsoft PowerPoint, utilisé pour créer des diaporamas contenant des textes, images, vidéos, animations et graphiques.",
  "pptx": "Fichier PowerPoint: DESCRIPTION \n Un fichier de présentation au format XML créé par Microsoft PowerPoint, offrant des fonctionnalités avancées de création de diaporamas.",
  "rtf": "Fichier RTF: DESCRIPTION \n Un fichier de texte enrichi pouvant inclure différentes polices, couleurs et formats, compatible avec de nombreux traitements de texte.",
  "csv": "Fichier CSV: DESCRIPTION \n Un fichier de valeurs séparées par des virgules utilisé pour stocker des données tabulaires, souvent importé et exporté par les feuilles de calcul.",
  "xml": "Fichier XML: DESCRIPTION \n Un fichier de langage de balisage extensible utilisé pour structurer et stocker des données de manière hiérarchique, souvent utilisé dans les échanges de données entre applications.",
  "svg": "Fichier SVG: DESCRIPTION \n Un fichier de graphique vectoriel évolutif utilisé pour définir des images vectorielles bidimensionnelles, souvent utilisé pour les logos et les icônes sur les sites web.",
  "mp3": "Fichier MP3: DESCRIPTION \n Un fichier audio compressé utilisant la norme de compression MPEG-1 Audio Layer III, couramment utilisé pour stocker et diffuser de la musique.",
  "wav": "Fichier WAV: DESCRIPTION \n Un fichier audio non compressé de haute qualité utilisé pour stocker des enregistrements sonores.",
  "mp4": "Fichier MP4: DESCRIPTION \n Un fichier multimédia utilisé pour stocker des vidéos, des images et de l'audio, couramment utilisé pour le streaming vidéo et les téléchargements.",
  "avi": "Fichier AVI: DESCRIPTION \n Un fichier vidéo non compressé ou peu compressé utilisé pour stocker des vidéos avec une haute qualité, souvent utilisé pour l'édition vidéo.",
  "mkv": "Fichier MKV: DESCRIPTION \n Un fichier conteneur multimédia utilisé pour stocker des vidéos, de l'audio et des sous-titres dans un seul fichier, souvent utilisé pour les vidéos haute définition.",
  "flv": "Fichier FLV: DESCRIPTION \n Un fichier vidéo Flash utilisé pour diffuser des vidéos en ligne, souvent utilisé par les sites de partage de vidéos.",
  "mov": "Fichier MOV: DESCRIPTION \n Un fichier vidéo développé par Apple utilisé pour stocker des vidéos, de l'audio et des effets, couramment utilisé dans le montage vidéo professionnel.",
  "epub": "Fichier EPUB: DESCRIPTION \n Un fichier de livre électronique utilisé pour stocker des livres numériques, souvent utilisé par les liseuses électroniques.",
  "mobi": "Fichier MOBI: DESCRIPTION \n Un format de fichier de livre électronique utilisé par Amazon Kindle et d'autres liseuses électroniques.",
  "tar": "Archive TAR: DESCRIPTION \n Un fichier archive utilisé pour regrouper plusieurs fichiers dans un seul fichier pour une distribution ou une sauvegarde, souvent utilisé en combinaison avec la compression gzip.",
  "gz": "Fichier GZ: DESCRIPTION \n Un fichier compressé utilisant la compression gzip, souvent utilisé pour réduire la taille des fichiers TAR.",
  "rar": "Archive RAR: DESCRIPTION \n Un fichier archive compressé utilisant la compression RAR, souvent utilisé pour la distribution de logiciels et de fichiers volumineux.",
  "7z": "Archive 7z: DESCRIPTION \n Un fichier archive compressé utilisant la compression 7z, offrant une haute compression et supportant plusieurs formats de données."
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
