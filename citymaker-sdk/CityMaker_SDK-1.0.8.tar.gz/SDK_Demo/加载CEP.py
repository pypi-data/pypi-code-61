#!/usr/bin/env Python
# coding=utf-8
#作者： tony

from CityMaker_SDK import RenderViewer3D
from CityMaker_SDK import Config


#cm=ICacheManager(None)

def initAxControl():
    config =Config()
    config.renderAddress = "http://124.193.151.47:8081"
    root ="renderControl"
    renderViewer3D=RenderViewer3D()
    renderViewer3D.setConfig(root, config)
    renderControl = renderViewer3D.getRenderControl()
    renderControl.interactMode = 1
    return renderControl

def initCamera(renderControl):
    camera = renderControl.camera
    pos = renderControl.new_Vector3
    ang = renderControl.new_EulerAngle
    pos.set(15415.2, 35211.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos, 600, ang)

def loadCep(renderControl):#---------------------------------------------加载CEP
    cepPath = "D:/cep/Package_乾隆花园/乾隆花园.cep"
    project = renderControl.project
    project.open(cepPath, False, "")
    camera = renderControl.camera
    camera.flyTime = 1


if __name__ == '__main__':
    g=initAxControl()
    initCamera(g)
    loadCep(g)