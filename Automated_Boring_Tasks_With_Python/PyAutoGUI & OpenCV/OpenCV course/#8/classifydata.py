import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def generate_negative_description_text_file():
    with open("neg.txt", "w") as f:
        for filename in os.listdir("neg"):
            f.write("neg/" + filename + "\n")

generate_negative_description_text_file()