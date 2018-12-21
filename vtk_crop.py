# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 10:38:23 2018

@author: lin
"""

import Tkinter
import vtk
#from slider import *

##TK GUI
root = Tkinter.Tk()
theLabel = Tkinter.Label(root, text = "Enter your folder path")
theLabel.pack()
root.title('Start')
root.geometry('400x300')
folder = Tkinter.StringVar()
folder_name = Tkinter.Entry(root, textvariable = folder)
folder_name.pack()

## Callback for reset
def reset_data(obj,ev):
    global reader, functionToStencil, quadric, stencil
    #stencildata = stencil.GetStencil()
    quadric.SetCenter(reader.GetOutput().GetCenter())
    quadric.SetScale(500,500,500)
    #sliderRepPX.SetValue(0.5*(box.GetBounds()[0] + box.GetBounds()[1]))
    #sliderRepPY.SetValue(0.5*(box.GetBounds()[2] + box.GetBounds()[3]))
    #sliderRepPZ.SetValue(0.5*(box.GetBounds()[4] + box.GetBounds()[5]))
    sliderRepSX.SetValue(500)
    sliderRepSY.SetValue(500)
    sliderRepSZ.SetValue(500)
    quadric.SetPhiRoundness(0)
    quadric.SetThetaRoundness(0)
    sliderRepRPhi.SetValue(0)
    sliderRepRThe.SetValue(0)
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def getSliderObjects(sliderRep, sliderWidget, titleText, iren, initVal, minVal, maxVal, posXLeft, posY, callBackFunc): 
    sliderRep.SetMinimumValue(minVal)
    sliderRep.SetMaximumValue(maxVal)
    sliderRep.SetValue(initVal)
    sliderRep.SetTitleText(titleText)
    sliderRep.GetPoint1Coordinate().SetCoordinateSystemToDisplay()
    sliderRep.GetPoint1Coordinate().SetValue(posXLeft, posY, 0)
    sliderRep.GetPoint2Coordinate().SetCoordinateSystemToDisplay()
    sliderRep.GetPoint2Coordinate().SetValue(posXLeft+300, posY, 0)
    sliderRep.SetSliderLength(0.025)
    sliderRep.SetSliderWidth(0.025)
    sliderRep.SetEndCapLength(0.0125)

    sliderWidget.SetInteractor(iren)
    sliderWidget.SetRepresentation(sliderRep)
    sliderWidget.KeyPressActivationOff()
    sliderWidget.SetAnimationModeToJump()
    sliderWidget.SetEnabled(True)
    sliderWidget.AddObserver("InteractionEvent", callBackFunc)
    
## Slider Call backs:
def scaleXSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevScaleSet = quadric.GetScale()
    quadric.SetScale(val,prevScaleSet[1],prevScaleSet[2])
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def scaleYSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevScaleSet = quadric.GetScale()
    quadric.SetScale(prevScaleSet[0],val,prevScaleSet[2])
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def scaleZSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevScaleSet = quadric.GetScale()
    quadric.SetScale(prevScaleSet[0],prevScaleSet[0],val)
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def posXSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevCenterSet = quadric.GetCenter()
    quadric.SetCenter(val,prevCenterSet[1],prevCenterSet[2])
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def posYSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevCenterSet = quadric.GetCenter()
    quadric.SetCenter(prevCenterSet[0],val,prevCenterSet[2])
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def posZSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    prevCenterSet = quadric.GetCenter()
    quadric.SetCenter(prevCenterSet[0],prevCenterSet[1],val)
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def phiRSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    quadric.SetPhiRoundness(val)
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

def thetaRSliderCallback(obj, event):
    sliderRep = obj.GetRepresentation()
    
    val = sliderRep.GetValue()
    quadric.SetThetaRoundness(val)
    
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()

## Read data
reader = vtk.vtkDICOMImageReader()

def choose_folder():
    dir_ = folder.get()
    print (dir_)
    reader.SetDirectoryName(dir_)
    reader.Update()
    global root
    root.destroy()    

## TK GUI loop
submit_btn = Tkinter.Button(root, text = 'Choose', command = choose_folder)
submit_btn.pack()
root.mainloop()
#root.update_idletasks()
#root.update()

## select crop area center
IP = 0
pkd = []
def select_point(obj,ev):
    x,y = obj.GetLastEventPosition()
    print ('picking pixel: '+ str(x) + ' and ' + str(y))
    global ren
    global quadric
    picker = vtk.vtkPicker()
    picker.Pick(x,y,0,ren)
    obj.SetPicker(picker)
    picked = picker.GetPickedPositions().GetPoint(0)
    #print picked
    print ('picked value: ' + str(picked[0]) + ';' + str(picked[1]) + ';' + str(picked[2]))
    ## crop area
    quadric.SetCenter(picked[0],picked[1],picked[2])
    quadric.SetScale(100,100,100)
    sliderRepSX.SetValue(100)
    sliderRepSY.SetValue(100)
    sliderRepSZ.SetValue(100)
    print quadric
    #getSliderObjects(sliderRepPX, sliderWidgetPX, "Position X", iren, quadric.GetCenter()[0], 25, 225, 1050, 500, posXSliderCallback)
    #getSliderObjects(sliderRepPY, sliderWidgetPY, "Position Y", iren, quadric.GetCenter()[1], 25, 225, 1050, 300, posYSliderCallback)
    #getSliderObjects(sliderRepPZ, sliderWidgetPZ, "Position Z", iren, quadric.GetCenter()[2], 25, 225, 1050, 100, posZSliderCallback)
    functionToStencil.Modified()
    functionToStencil.Update()
    stencil.Modified()
    stencil.Update()
    volume.Modified()
    volume.Update()
    ## Draw the center of area
    global IP, pkd
    pkd.append(picked)
    IP = IP + 1
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(picked[0],picked[1],picked[2])
    sphere.SetRadius(2)
    #print sphere
    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphere.GetOutputPort())
    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    #print sphereActor
    #global ren
    ren.AddActor(sphereActor)

## quadric function to crop data    
quadric = vtk.vtkSuperquadric()
quadric.SetCenter(reader.GetOutput().GetCenter())
quadric.SetScale(500,500,500)
quadric.SetPhiRoundness(0)
quadric.SetThetaRoundness(0)
#quadric.ToroidalOn
#quadric.SetToroidal(1)


functionToStencil = vtk.vtkImplicitFunctionToImageStencil()
functionToStencil.SetInput(quadric)
functionToStencil.SetInformationInput(reader.GetOutput())
functionToStencil.Update()

## Create image   
stencil = vtk.vtkImageStencil()
stencil.SetInputConnection(reader.GetOutputPort())
stencil.SetBackgroundValue(reader.GetOutput().GetScalarRange()[0]-1)
stencil.SetStencilData(functionToStencil.GetOutput())

## Create colour transfer function
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(-3024, 0.0, 0.0, 0.0)
colorFunc.AddRGBPoint(-77, 0.54902, 0.25098, 0.14902)
colorFunc.AddRGBPoint(94, 0.882353, 0.603922, 0.290196)
colorFunc.AddRGBPoint(179, 1, 0.937033, 0.954531)
colorFunc.AddRGBPoint(260, 0.615686, 0, 0)
colorFunc.AddRGBPoint(3071, 0.827451, 0.658824, 1)

## Create opacity transfer function
alphaChannelFunc = vtk.vtkPiecewiseFunction()
alphaChannelFunc.AddPoint(-3024, 0.0)
alphaChannelFunc.AddPoint(-77, 0.0)
alphaChannelFunc.AddPoint(94, 0.29)
alphaChannelFunc.AddPoint(179, 0.55)
alphaChannelFunc.AddPoint(260, 0.84)
alphaChannelFunc.AddPoint(3071, 0.875)

## Instantiate necessary classes and create VTK pipeline
ren = vtk.vtkRenderer()
#ren.SetBackground(1,.5,1)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
renWin.SetSize(1350,750)

## interactor modified
iren.AddObserver('RightButtonPressEvent', select_point)

## Define volume properties
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetScalarOpacity(alphaChannelFunc)
volumeProperty.SetColor(colorFunc)
volumeProperty.ShadeOn()

## Define volume mapper
volumeMapper = vtk.vtkSmartVolumeMapper()  
volumeMapper.SetInputConnection(stencil.GetOutputPort())

## Set the mapper and volume properties
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)  
ren.AddVolume(volume)

## Setup the slider widget
sliderRepSX = vtk.vtkSliderRepresentation2D()
sliderWidgetSX = vtk.vtkSliderWidget()
sliderWidgetSX.SetAnimationModeToOff()

sliderRepSY = vtk.vtkSliderRepresentation2D()
sliderWidgetSY = vtk.vtkSliderWidget()
sliderWidgetSY.SetAnimationModeToOff()

sliderRepSZ= vtk.vtkSliderRepresentation2D()
sliderWidgetSZ = vtk.vtkSliderWidget()
sliderWidgetSZ.SetAnimationModeToOff()

sliderRepRPhi= vtk.vtkSliderRepresentation2D()
sliderWidgetRPhi = vtk.vtkSliderWidget()
sliderWidgetRPhi.SetAnimationModeToOff()

sliderRepRThe= vtk.vtkSliderRepresentation2D()
sliderWidgetRThe = vtk.vtkSliderWidget()
sliderWidgetRThe.SetAnimationModeToOff()

getSliderObjects(sliderRepSX, sliderWidgetSX, "Radius X", iren, 500, 5, 505, 0, 300, scaleXSliderCallback)
getSliderObjects(sliderRepSY, sliderWidgetSY, "Radius Y", iren, 500, 5, 505, 0, 200, scaleYSliderCallback)
getSliderObjects(sliderRepSZ, sliderWidgetSZ, "Radius Z", iren, 500, 5, 505, 0, 100, scaleZSliderCallback)
getSliderObjects(sliderRepRPhi, sliderWidgetRPhi, "N/S Roundness", iren, 0, 0, 1.0, 0, 400, phiRSliderCallback)
getSliderObjects(sliderRepRThe, sliderWidgetRThe, "E/W Roundness", iren, 0, 0, 1.0, 0, 500, thetaRSliderCallback)


'''
sliderRepPX = vtk.vtkSliderRepresentation2D()
sliderWidgetPX = vtk.vtkSliderWidget()

sliderRepPY = vtk.vtkSliderRepresentation2D()
sliderWidgetPY = vtk.vtkSliderWidget()

sliderRepPZ = vtk.vtkSliderRepresentation2D()
sliderWidgetPZ = vtk.vtkSliderWidget()

#getSliderObjects(sliderRepPX, sliderWidgetPX, "Position X", iren, quadric.GetCenter()[0], 25, 225, 1050, 500, posXSliderCallback)
#getSliderObjects(sliderRepPY, sliderWidgetPY, "Position Y", iren, quadric.GetCenter()[1], 25, 225, 1050, 300, posYSliderCallback)
#getSliderObjects(sliderRepPZ, sliderWidgetPZ, "Position Z", iren, quadric.GetCenter()[2], 25, 225, 1050, 100, posZSliderCallback)
'''


## Reset button modified
retext = vtk.vtkTextWidget()
textactor = vtk.vtkTextActor()
retext.SetTextActor(textactor)
retext.SetInteractor(iren)
retext.On()
retext.GetTextActor().SetInput("Reset")
retext.GetTextActor().GetTextProperty().SetColor(0, 1, 0)
#retext.GetRepresentation().GetPositionCoordinate().SetCoordinateSystemToDisplay()
#retext.GetRepresentation().GetPositionCoordinate().SetValue(1050,520,0)
#retext.GetRepresentation().GetPosition2Coordinate().SetCoordinateSystemToDisplay()
#retext.GetRepresentation().GetPosition2Coordinate().SetValue(1051,521,0)
retext.GetRepresentation().SetPosition(0.8,0.8)
retext.SelectableOn()
retext.AddObserver('WidgetActivateEvent', reset_data)

widget = vtk.vtkTextWidget()
widget.SetInteractor(iren)
widget.On()
widget.GetTextActor().SetInput("Right-click to select area of interest")
widget.GetTextActor().GetTextProperty().SetColor(1, 0, 0)
widget.GetRepresentation().GetPositionCoordinate().SetValue(0, .6)
widget.GetRepresentation().GetPosition2Coordinate().SetValue(.35, .65)



## Render the scene
renWin.Render()
iren.Start()

