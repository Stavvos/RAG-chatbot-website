import html2text

print("Enter html filename")
html = input()

print("Enter name of the txt output file")
txt = input()

htmlFilePath = "./data/html/" + str(html)
txtFilePath = "./data/txt/" + str(txt)

with open(htmlFilePath, "r", encoding="utf-8") as file:
    htmlContent = file.read()

textContent = html2text.html2text(htmlContent)

outFile = open(txtFilePath, "w")
outFile.write(textContent)
outFile.close()

print("The output file was saved to ", txtFilePath)

