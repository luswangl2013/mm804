This is the instruction on how to run the code.
by Shang Lu

Python version 2.7.
VTK version 7.1.1
Tkinter is a standard package of Python. Make sure it is still in the environment.

--------------------------
Files in the folder:
1. "ReadMe.txt" -- this instruction file.
2. "vtk_crop.py" -- source code of this project.
3. "mm804_project_report_ShangLu.pdf" -- project report.
--------------------------
How to run the code:
1. Unzip first. Run the "vtk_crop.py" file in python environment. Then a user interface panel named "Start" is displayed. 

2. In the blank on the panel, input the directory path of the folder which contains the CT data. ATTENTION: (1)if the data are located in a totally different directory from the source code, the input must contain the full directory, from the basic disk to the last level folder containing the DCM files. (2)If the data folder is under the same root of the source code, the input can skip the high level directory, starting from the folder containing source code to the last level folder containing DCM files.
 
FOR EXAMPLE, (A)if the DCM files are in a folder named "CTDATA", and this folder is at the same root with the source code, the input should be "CTDATA". (B)If the folder "CTDATA" is in the folder "DATA" and "DATA" folder is at the same root with the source code, the input should be "DATA\CTDATA". (C)If the source code is somewhere in C: disk, while the data are located at D:\DATA\CTDATA, the input should be "D:\DATA\CTDATA".

WARNING: make sure input is full and correct. Wrong input generates nothing in the window.

3. After input the path of data folder, click "Choose" button. Then the "Start" panel will disappear, and a VTK window will be displayed. In the center of the window, the CT data are shown. The data can be rotated, moved or zoomed as normal.

4. The cropping area is set very large at the beginning, with scale 500 on each axis. So large amount of data are displayed. To select an area of interest, just right-click the location of interest in the data. Then a superquadric function will crop the data.

5. At the moment of selection, the superquadric function is set with scale 100 on each axis, and value 0 on both PhiRoundness and ThetaRoundness. So the cropping area is cubic at this time. Move the sliders on the left side to adjust these parameters. "N/S Roundness" and "E/W Roundness" sliders control PhiRoundness and ThetaRoundness correspondingly. Move them from 0 to 1 will shape the area from cube to sphere. "Radius ~" sliders control the scale on corresponding axis. Move them will change the size of cropping area.

6. Left-click the "Reset" text at the top-right corner will change all the parameters of superquadric function back to initial values. So the cropping area will change back to large size with cubic shape and original location. Thus the data are ready to be cropped again.

7. After cropping, close the window to quit the source code.