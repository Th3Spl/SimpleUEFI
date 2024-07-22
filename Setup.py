#
# Libraries
#
import os
import shutil
import ctypes


#
# Getting the DOCUMENTS path
#
def get_documents_path( ) -> str:
    
    #
    # For Windows 7 and later
    #
    CSIDL_PERSONAL = 5
    
    #
    # Get the path using Windows API
    #
    buf = ctypes.create_unicode_buffer( 260 )
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, 0, buf)
    
    return buf.value


#
# Get VS installation
#
def get_templates_path( documents_path ) -> str:
    
    if os.path.exists( f"{ documents_path }\\Visual Studio 2015" ):
        return f"{ documents_path }\\Visual Studio 2015"
    
    if os.path.exists( f"{ documents_path }\\Visual Studio 2019" ):
        return f"{ documents_path }\\Visual Studio 2019"
    
    if os.path.exists( f"{ documents_path }\\Visual Studio 2022" ):
        return f"{ documents_path }\\Visual Studio 2022"
    
    return None


#
# Copy folder & Content
#
def copy_folder( source_dir, destination_dir ) -> bool :
    
    #
    # Status
    #
    status = True
    
    
    #
    # Checking the source directory & the destination directory 
    #
    if not os.path.exists( source_dir ):
        print(" [ ERROR ] Could not find the source path!")
        return
        
    if not os.path.exists( destination_dir ):
        os.makedirs( destination_dir )
    
    
    #
    # Copying the files
    #
    for item in os.listdir( source_dir ):
        source_item = os.path.join( source_dir, item )
        destination_item = os.path.join( destination_dir, item )
        
        try:
            if os.path.isdir( source_item ):
                shutil.copytree( source_item, destination_item )
            else:
                shutil.copy2( source_item, destination_item )
            print( f" [ SETUP ] Copied '{ source_item }' to '{ destination_item }'" )
        except shutil.Error as e:
            print( f" [ ERROR ] Could not copy '{ source_item }': { e }" )
            status = False
        except OSError as e:
            print( f" [ ERROR ] OS error occurred while copying '{ source_item }': { e }" ) 
            status = False
    
    return status


#
# Main function
#
def main( ) -> None:
    
    #
    # Changing the console color
    #
    os.system( "color a" )
    
    
    #
    # Credits
    #
    print( "\n------------------------------------------------------------------" )
    print( " Simple MSVC_UEFI By: Th3Spl\n" )
    print( " Credits:")
    print( " - VisualUEFI: https://github.com/ionescu007/VisualUefi" )   
    print( " - EDK2:       https://github.com/tianocore/edk2" ) 
    print( "------------------------------------------------------------------\n" )
    print( " [ SETUP ] Initializing the setup..." )
    
    
    #
    # Notifying
    #
    print( " [ SETUP ] Environment variables successfully found" )
    
    
    #
    # Copying the components within a universal path
    #
    if copy_folder( ".\\MSVC_UEFI", "C:\\Program Files\\MSVC_UEFI" ):
        print( " [ SETUP ] All files copied successfully!" )
    else:
        print( " [ ERROR ] Could not copy all the needed files!" )
    
    
    #
    # Making the user compile VisualUefi
    #
    print( " [ SETUP ] Opening the folder\n" )
    print( " [ SETUP ] Please open 'EDK-II.sln' and build the entier solution.\n" )
    os.system( f"explorer \"C:\\Program Files\\MSVC_UEFI\\VisualUefi\\EDK-II\"" )
    print( " Presss any key once you compiled VisualUefi...\n" )
    os.system( "pause>nul" )
    
    
    #
    # Findig out which VisualStudio installation the user has
    #
    templates_path = get_templates_path( get_documents_path() )
    if templates_path != None:
        print( " [ SETUP ] Templates path found successfully" )
    else:
        print( " [ ERROR ] Could not find a VS templates path!" )
        return
    
    
    #
    # Once the user has compield VisualUefi
    # 
    if copy_folder( ".\\Templates", f"{ templates_path }\\Templates\\ProjectTemplates" ):
        print( " [ SETUP ] All templates copied successfully!" )
    else:
        print( " [ SETUP ] Could not copy all the templates!" )
    
    
    return
    

#
# Starting the main routine
#
if __name__ == "__main__":
    main( )