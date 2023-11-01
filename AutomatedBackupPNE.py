# Author: Cameron Beebe
# Date: 8/11/23
# Purpose: Backup the default.pdb file that houses our Printnet database. 
# Comments: I did not include the funcionality to delete files after a certian number is reached because I did not want to erase anything we may need in the futuer. 



import shutil
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import subprocess

# Set the path of the specific file you want to backup
specific_file_path = "G:/HDW/Printronix/Printronix_PrintNet_Database/default.pdb"
# Set the path to the backup directory
backup_directory = "G:/HDW/Printronix/Printronix_PrintNet_Database"

# Function to create a backup of the specific file
def createFile():
    try:
        backup_date = datetime.now().strftime("%Y%m%d")
        backup_filename = f"backup_{backup_date}.pdb"
        destination_path = os.path.join(backup_directory, backup_filename)
        
        # Copy the specific file to the backup location
        shutil.copy(specific_file_path, destination_path)
        
        # Show message when completed
        messagebox.showinfo(title="", message=f"Your file has been successfully backed up. To {str(backup_directory)}")
    except Exception as e:
        # If an exception occurs, display an error message
        messagebox.showerror(title="Error", message=f"An error occurred: {str(e)}. Ensure you have your G: drive mapped to properly.")

# Call the function to create the backup
createFile()





