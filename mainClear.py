import os

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def moves(foldername,files):
    for file in files:
        os.replace(file, f"foldername/{file}")

if __name__ == '__main__':

    files=os.listdir()
    files.remove("mainClear.py")

    createIfNotExists('Images')
    createIfNotExists('Media')
    createIfNotExists('Docs')
    imgExts = [".png",".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt",".docx",".doc",".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4",".mp3"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        exts = os.path.splitext(file)[1].lower()
        if (exts not in imgExts) and (exts not in docExts ) and (exts not in mediaExts) and os.path.isfile(file):
            others.append(file)

    moves("Image",images)
    moves("Docs",docs)
    moves("Media",medias)
    moves("Others",others)
