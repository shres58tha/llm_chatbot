import pip   

def import_xyz(xyz): 
    try:
        __import__(xyz)
        print (xyz + " module tested")
    except ImportError:
        print (f"{xyz} module is needed")
        print (f"pip install {xyz} ")
        pip.main (['install' , xyz])