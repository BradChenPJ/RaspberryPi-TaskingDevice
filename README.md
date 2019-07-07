# RaspberryPi-TaskingDevice
After Raspberry Pi register into oneM2M, oneM2M can send Http request to control Raspberry Pi device. In this demonstration, Raspberry Pi receive a Http POST then control the LCD board.
##Setup
You must setup the description file `.txt`, registration file and task file `.py`
* Description file   
Setup `Things`, `Locations`, `TaskingCapabilities`, `oneM2MProtocol` and `Actuator`. [(Huang & Wu, 2016)](https://www.mdpi.com/1424-8220/16/9/1395)
* Registration file   
Setup oneM2M URL. 
* Task file   
Setup Flask IP address, port, Http method and task of the device.
##Author
[Brad Chen](https://github.com/BradChenPJ)
