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

def loadSkyBox(renderControl):
    skyboxPath = "D://skybox"
    renderControl.objectManager.setSkybox(0,skyboxPath,1)

def initCamera(renderControl):
    camera = renderControl.camera
    pos = renderControl.new_Vector3
    ang = renderControl.new_EulerAngle
    pos.set(15415.2, 35211.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos, 600, ang)

def loadFDB(renderControl):
    server = "124.193.151.44"
    port = 8040
    database = "SDKDEMO"
    renderControl.loadFDBByService(server, port, database, "", "")


def fnMouseClickSelect(pickResult,intersectPoint,mask,eventSender):
    position = intersectPoint.position
        # if (!renderControl) {
        #   alert("renderControl未初始化完成!");
        #   return;
        # }
    label = g.objectManager.createLabel(
        {"x": position.x, "y": position.y,"z": position.z },
        "标签123",
        "#000000",
        15,
        "宋体",
        1,
        1000
        )


if __name__ == '__main__':
    g=initAxControl()
    loadSkyBox(g)
    initCamera(g)
    loadFDB(g)
    g.interactMode = 2
    g.onMouseClickSelect = fnMouseClickSelect
