"""this program changes new lines to spaces and gives variable"""
textForChange = input("please enter name of your text file or relative path to it: ")

def NewLineChanger(textFile):
    boringText = ""
    
    
    try:
        with open(textFile,"r") as f:
            boringText = f.read().replace('\n',' ')
            return boringText

    except FileNotFoundError:
        print("such file or directory is not found")
        return

print(NewLineChanger(textForChange))
