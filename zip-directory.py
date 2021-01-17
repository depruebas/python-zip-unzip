import os
import sys
import zipfile

# ZIP a directory
def zip_directory(path_zip, filename):
    
    zipf = zipfile.ZipFile( filename, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path_zip):
        for file in files:
            zipf.write(os.path.join(root, file))

    zipf.close()

# UnZip in the path_unzip a zip file
def unzip_directory( path_unzip, filename):

    with zipfile.ZipFile( filename, 'r') as zip_ref:
       zip_ref.extractall( path_unzip)

# View content of zip file
def zip_view( filename):

     with zipfile.ZipFile( filename) as file:
        file.printdir()


# Help to usage script
def help():
    print(""" Wrong parameter:
    
    Usage:
        python zip-directory.py Zip path filename       # To zip directory recursively
        python zip-directory.py UnZip path filename     # To un Zip
        python zip-directory.py View filename           # To view files in zip archive

    """)


if __name__ == '__main__':      

    if len(sys.argv) > 1:
        
        if ( sys.argv[1] == 'Zip'):
            filename =  sys.argv[3]
            path =  sys.argv[2]

            print( sys.argv[1] + ": directory: " + path + " into file: " + filename)

            zip_directory( path, filename)

        elif( sys.argv[1] == 'UnZip'):
            filename =  sys.argv[3]
            path =  sys.argv[2]

            print( sys.argv[1] + ": file: " + filename + " directory: " + path)

            unzip_directory( path, filename)
        
        elif( sys.argv[1] == 'View'):
            filename =  sys.argv[2]

            print( sys.argv[1] + ": file: " + filename )

            zip_view( filename)

        else:
            print( sys.argv[1] + ": unknown command")
            help()
            
    else:
        print( "Unknown command")
        help()


    sys.exit()

    
