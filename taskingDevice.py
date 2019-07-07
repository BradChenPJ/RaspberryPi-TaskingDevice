import oneM2M.subscribe
import oneM2M.contentInstance
import oneM2M.container
import oneM2M.AE
import json
import requests
import copy

with open("/home/pi/Desktop/python/deviceToOM2MTasking.txt", mode="r") as readFile:
    taskingObj = json.load(readFile)

thing = taskingObj["Things"]
thingName = taskingObj["Things"]["name"]
location = taskingObj["Locations"][0]
taskingCapa = taskingObj["TaskingCapabilities"][0]

AE = oneM2M.AE.AE(thingName, "Tasking")  # create AE,Con,Cin instance
thingCon = oneM2M.container.container("Thing_Metadata")
locationCon = oneM2M.container.container("Locations")
taskingCapaCon = oneM2M.container.container("TaskingCapability_Metadata")
taskingCon = oneM2M.container.container("TaskingCapability1_Task")  # if has several task,should modify
thingCin = oneM2M.contentInstance.contentInstance("Thing_Metadata", json.dumps(thing))
locationCin = oneM2M.contentInstance.contentInstance("Location", json.dumps(location))
taskingCapaCin = oneM2M.contentInstance.contentInstance("TaskingCapability1", json.dumps(taskingCapa))

AEURL = "http://192.168.1.100:8686/~/mn-cse"
conURL = AEURL+"/mn-name/"+thingName
cinURLThing = conURL+"/Thing_Metadata"
cinURLLocation = conURL+"/Locations"
cinURLTaskingCapa = conURL+"/TaskingCapability_Metadata"
cinURLTasking = conURL+"/TaskingCapability1_Task"
subURL = "http://192.168.1.103:8484/task"

subCin = oneM2M.subscribe.subscribe("Info_Monitor", subURL)

AEheader = {"X-M2M-Origin": "admin:admin","Content-Type": "application/json;ty=2"}
conheader = {"X-M2M-Origin": "admin:admin","Content-Type": "application/json;ty=3"}
cinheader = {"X-M2M-Origin": "admin:admin","Content-Type": "application/json;ty=4"}
subheader = {"X-M2M-Origin": "admin:admin","Content-Type": "application/json;ty=23"}
requests.post(AEURL, headers=AEheader, data=AE.setAEBody())  # http post (AE)
# http post (container)
requests.post(conURL, headers=conheader, data=thingCon.setConBody())
requests.post(conURL, headers=conheader, data=locationCon.setConBody())
requests.post(conURL, headers=conheader, data=taskingCapaCon.setConBody())
requests.post(conURL, headers=conheader, data=taskingCon.setConBody())
# http post (contentInstance)
requests.post(cinURLThing, headers=cinheader, data=thingCin.setCinBody())
requests.post(cinURLLocation, headers=cinheader, data=locationCin.setCinBody())
requests.post(cinURLTaskingCapa, headers=cinheader,data=taskingCapaCin.setCinBody())
requests.post(cinURLTasking, headers=subheader, data=subCin.setSubBody())

    



