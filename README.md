# GeoGuardian 
En este repositorio está todo el código para la participación en la hackaton Polkadot, la información del hardware que se diseño las tecnologías y el front el demo los podemos ver en: <http://ec2-184-72-114-228.compute-1.amazonaws.com:8086/>

![](img/encode.png)

## How does it work?
GeoGuardian is a blockchain-based project that uses an IoT device to measure the concentration of carbon monoxide (CO2) and track CO2 emissions in different locations. The solution works in four key steps:
IoT device: GeoGuardian uses an IoT device to measure the concentration of CO2. This device can be installed in various locations, such as homes, offices, cars, bicycles, and other places.
Connection to the blockchain network: Once the IoT device is installed, it is connected to the blockchain network to perform transactions. The blockchain network is a decentralized and secure database that records all transactions made.
Measurement and tracking of CO2 emissions: The IoT device measures the concentration of CO2 and tracks CO2 emissions in different locations. The collected data is used to create a map of CO2 concentration around the world, which helps raise awareness about the problem of climate change and motivates people to reduce their carbon footprint.
Reward system: GeoGuardian uses a reward system to incentivize users to reduce their carbon footprint. When users manage to reduce their CO2 emissions below a specific target, it will deduct from the grant account to the stake account. Users receive tokens as a reward for reducing their carbon footprint. for contact: 
<a href="mailto:jhonteajada95@gmail.com">Jhon Tejada</a>, <a href="mailto:oscarriojas@gmail.com">Oscar Riojas</a>, check repo in <a href="https://github.com/jhontejada95/CO2_GeoGuardian">CO2_GeoGuardian</a>

![](img/screen.jpeg)

## Hardware
El microcontrolador que se utilizó es una ESP32 por su bajo consumo de energía y que tiene incorporado conexión wifi, para medir el nivel de CO2 se utilizó un sensor MQ135 conectado a una de las entradas analógicas.

![](img/sensor2.jpg)

* MICRO ESP8266: <https://electronilab.co/tienda/nodemcu-board-de-desarrollo-con-esp8266-wifi-y-lua/>
* CO2 MQ135:   <https://components101.com/sensors/mq135-gas-sensor-for-air-quality>
* GPS neo-6m:  <https://naylampmechatronics.com/sensores-posicion-inerciales-gps/106-modulo-gps-neo-6m.html>

## Software
Todo el backend de la aplicación esta construido en python utilizando la libreria <https://github.com/polkascan/py-substrate-interface> para la conexion a la blockchain, fastAPI para crear los endpoint, el front esta construido con Boodstrap y la red de prueba que se utiliza es Westend

## Infraestructura
La aplicación utiliza una instancia de EC2 de la capa gratuita de AWS y una base de datos SQL RDS de AWS también en la capa gratuita.

![](img/CO2_geoguardian.jpg)

## Video demo
El demo se puede ver en: <https://www.youtube.com/watch?v=rAjoWlaW4j8>
