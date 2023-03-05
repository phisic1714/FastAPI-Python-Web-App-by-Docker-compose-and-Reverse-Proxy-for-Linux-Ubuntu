# FastAPI Python Web App by Docker compose and Reverse Proxy for Linux Ubuntu (FastAPI Python Web App โดย Docker compose และ Reverse Proxy สำหรับ Linux Ubuntu)
![f](img/logos.webp)
Hi, My name is Peerapat. I'll will show you how to compose *FastAPI python web app* by Docker compose and make Reverse Proxy to create your Domain name for *FastAPI python web app*         
(สวัสดีครับ ผมชื่อ พีรพัฒน์ ผมจะมาแสดงวิธีการอัพโหลด *FastAPI python web app* โดย Docker compose และทำ Reverse Proxy เพื่อสร้าง ชื่อโดเมน ของคุณเองสำหรับ *FastAPI python web app*)
|**Contents (สารบัญ)**|
| :-: |
| [Preparation (การเตรียมพร้อม)](#preparation) |
|[Step 1 : Python file (ขั้นตอนที่ 1 : ไฟล์ Python)](#step-1--python-file)|
|[Step 2 : Dockerfile (ขั้นตอนที่ 2 : Dockerfile)](#step-2--dockerfile)|
|[Step 3 : compose.yml file (ขั้นตอนที่ 3 : ไฟล์ compose.yml)](#step-3--composeyml-file)|
|[Result (ผลลัพธ์)](#result)|
|[Reference (อ้างอิง)](#reference)|

## Preparation 
(การเตรียมพร้อม) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)


---
1. [Install Docker Engine.](https://github.com/pitimon/dockerswarm-inhoure) 

     (ติดตั้ง Docker Engine)

2. Install Docker Engine Extendsion on VS Code

     (ติดตั้ง Docker Engine Extendsion บน VS Code)
3. [Create Portainer CE with Docker Swarm Service easier to compose without command line and share Node to be able to work the same.](https://github.com/pitimon/dockerswarm-inhoure) 

     (สร้าง Portainer CE กับ Docker Swarm Service เพื่อง่ายต่อการ compose โดยไม่ต้องใช้ command line และสามารถแบ่ง Node ให้สามารถทำงานเหมือนกันได้)
4. [Create Traefik Service for allow to use Reverse Proxy in compose file.](https://github.com/pitimon/dockerswarm-inhoure/tree/main/ep03-traefik)  
(สร้าง Traefik Service สำหรับให้ใช้ Reverse Proxy ใน compose ไฟล์)
5. Create Network name webproxy by this commande below      
(สร้าง Network ชื่อ Webproxy จากคำสั่งนี้)

          docker network create -d overlay --attachable webproxy
## Step 1 : Python file 
(ขั้นตอนที่ 1 : ไฟล์ Python) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)

---

Create python file to make your web app code

(สร้าง python file เพื่อสร้าง web app code)

File Path
    (ที่ตั้งไฟล์)
        
        app
        |-main.py
1. Use Python and FastAPI module template for make web app by Python. I'll explain how Python code in **main.py** work

    (ใช้ Python และ โมดูล FastAPI เป็นเท็มเพลต สำหรับเขียน web app โดย Python ผมจอธิบายการทำงานของ Python code ใน **main.py**)

    
    <details><summary>Click me!!</summary>
    
     ```ruby
     from fastapi import FastAPI 

    app = FastAPI() 
    @app.get("/") 
    async def hello_world(): 
        return {"ข้อความ(message)": "สวัสดีชาวโลก(Hello World)"} 
     
     ```
    </details>
    from this code FastAPI Module and Defind function to show this result on web app

        {"ข้อความ(message)":"สวัสดีชาวโลก(Hello World)"}
        
## Step 2 :  Dockerfile 
(ขั้นตอนที่ 2 : Dockerfile) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)

---
Create Dockerfile file to set command scripts to create image. 

(สร้าง Dockerfile เพื่อตั้งเป็นคำสั่งในการสร้าง image)

1.  Create Dockerfile you can use from this repository or Create by your own. 

    (สร้าง Dockerfile คุณสามารถ ใช้ repository นี้ หรือสร้างขึ้นมาเองได้)
    <details>
    <summary>Click me!!</summary>

    ```ruby
      # syntax = docker/dockerfile:1.4
      FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS   builder
      
      WORKDIR /app
      
      COPY requirements.txt ./
      RUN --mount=type=cache,target=/root/.cache/pip \
          pip install -r requirements.txt
      
      COPY ./app ./app
      
      FROM builder as dev-envs
      
      RUN <<EOF
      apt-get update
      apt-get install -y --no-install-recommends git
      EOF
      
      RUN <<EOF
      useradd -s /bin/bash -m vscode
      groupadd docker
      usermod -aG docker vscode
      EOF
      
      COPY --from=gloursdocker/docker / /

    ```

    </details>
     Docker Scripts below is command scripts for image when service working this scripts will run inside image for run an web app code
     
     (จาก Docker Scripts เป็นคำสั่ง ให้กับ image เมื่อ service ทำงาน คำสั่งพวกนี้จะ run ภายใน image เพื่อที่จะ run web app code)
2. Create requirements.txt this Text file contain this

    (สร้างไฟล์ requirements.txt Text file จะเก็บสิ่งนี้)


        fastapi
        uvicorn

    this's Python module name it will use to Dockerfile to command pip install these module.

    (นี่คือชื่อของ Python module มันจะนำมาใช้กับคำสัง pip install ใน Dockerfile)
3. Build this Dockerfile to image you can use this 2 optional solution

    (สั่ง Build Dockerfile นี้ไปเป็น Image คุณสามารถเลือกทำได้ 2 วิธี)

    - Use command line
       
       (ใช้ command line)


          docker build -t phisic1714/fastapi. #you can change tag name (คุณสามารถเปลี่ยนชื่อ tag ได้)

     - Use Docker engine Extension on VS Code 
     
         (ใช้ Extendsion ของ Docker engine บน VS Code)

         ![f](img/build.png)


## Step 3 : compose.yml file 
(ขั้นตอนที่ 3 : ไฟล์ compose.yml) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)

---
Create compose file to command to create service and make reverse proxy. 

(สร้าง compose file เพื่อเป็นคำสั่งในการสร้าง service และทำ reverse proxy)

1. Create compose file you can use compose.yml file from this repository or create by your own but I'll explain my script inside compose.yml.

    (สร้างไฟล์ compose คุณสามารถใช้ compose.yml file จาก repository นี้ หรือสร้างของคุณเอง แต่ผมจะอธิบาย script ข้างใน compose.yml)

    <details>
    <summary>Click me!!</summary>
    
    ```ruby
     version: '3.3'
     # Declare compose version(ประกาศ compose version)
     services:
     # Declare to create services (ประกาศที่จะสร้าง services)
       api:
       # Declare api services (ประกาศ api services)
         image: phisic1714/fastapi:latest	
         # Pull tag image from your build command (ดึง tag image จากการที่คุณสั่ง build)
         networks:
         # Declare networks for api services (ประกาศ networks ที่จะใช้สำหรับ api)
          - webproxy
          # network name webproxy (network ชื่อ webproxy)
         environment:
         # Declare environment (ประกาศตัวแปรสภาพแวดล้อมของ Services)
          PORT: 8000
          # Set gitea use port 8000 (ตั้งให้ gitea ใช้ port 8000)
         logging:
         # Create logging (สร้างการเก็บ log)
           driver: json-file
           # Declare driver for logging type json (ประกาศการเก็บ log แบบ json)
         volumes:
         # Declare volumes tag (ประกาศที่จะตั้ง tag ให้ volumes)
           - /var/run/docker.sock:/var/run/docker.sock
           # Create volume tag Docker socket path (สร้าง tag volume สำหรับที่อยู่ Docker socket)
           - app:/app
           # Create volume tag for web app (สร้าง tag volume สำหรับที่อยู่ web app)
         restart: 'no'
         # Set restart service never(ตั้งให้ไม่มีการ restart service)
         deploy:
         # Declare deploy (ประกาศ การ Deploy)
           replicas: 1
           # set 1 replicas (ตั้งการทำ deploy แค่ 1 ครั้ง)
           labels:
           # Declare labels to create Reverse Proxy (ประกาศที่จะสร้าง label สำหรับทำ Revers Proxy)
             - traefik.docker.network=webproxy
             # Set network for Traefik (ตั้ง network สำหรับ Traefik)
             - traefik.enable=true
             # Enable Traefik (เปิดใช้ Traefik)
             - traefik.http.routers.${APPNAME}-https.entrypoints=websecure
             # Set Entrypoint (ตั้งการเริ่มต้นประมวลผล)
             - traefik.http.routers.${APPNAME}-https.rule=Host("${APPNAME}.xops.ipv9.me")
             # Set Hostdomain for open gitea website (ตั้ง Hostdomain สำหรับเข้าใช้ gitea website)
             - traefik.http.services.${APPNAME}.loadbalancer.server.port=8000
             # Set port for loadbalance (ตั้ง Port สำหรับทำ loadbalance)
           resources:
           # Declare resources for deploy (ประกาศทรัพยากรสำหรับการ deploy)
             reservations:
             # Declare resources reservations (ประกาศการจองทรัพยากร) 
               cpus: '0.1'
               # Use CPU 1 Core (ใช้ CPU 1 Core)
               memory: 10M
               # Use Memory 10 Megabyte (ใช้หน่วยความจำ 10 Megabyte)
             limits:
             # Declare resources limits (ประกาศการจำกัดทรัพยากร)
               cpus: '0.4'
               # Limit CPU 4 Core (จำกัด CPU 1 Core)
               memory: 250M
               # Limit Memory 250 Megabyte (จำกัดหน่วยความจำ 250 Megabyte)
               
     networks:
     # Declare Network (ประกาศการใช้ Network)
      webproxy:
      # Declare  Network name (ประกาศการใช้ชื่อ Network)
         external: true
         # set external network (ตั้งการใช้ network จากภายนอกของ service ที่มีอยู่แล้ว)
     volumes:
     # Declare to create volumes (ประกาศที่จะสร้าง volumes)
       app:
       # Create Volumes from web app tag (สร้าง volume จาก tag web app )

    ```
    </details>


     from my Scripts you can see this variable.
     
      (คุณเห็นตัวแปรจากที่ผมเขียนตัวนึงตามนี้)

          ${APPNAME}
     You can Edit them for your own or create .env file to setting value for this variable.
     
      (คุณสามารถแก้ไขให้เหมาะสมกับคุณ หรือ สร้างไฟล์ .env เพื่อตั้งค่าสำหรับตัวแปรที่กล่าวไว้)

2. Compose Up this compose.yml file to stack you can use this 2 optional solution 

     (ทำการ Compose Up compose.yml file นี้ไปยัง stack โดยสามารภเลือกทำได้ 2 วิธีนี้)

     - Use command line below 
     
          (ใช้คำสั่งตามนี้)

               docker stack deploy -c compose.yml fastapi

     - Use Portainer follow step below 
     
          (ใช้ portainer โดยทำตามนี้)
          - open portainer select **Stack menu** and select **Add Stack** 
          
               (เข้า portainer เลือก **เมนู stack** และ **เลือก Add Stack**)
          ![f](img/openstack.png)
          - Copy Scripts inside compose.yml file insert them in **Web editor** Text box Entry Stack name and set your enviroment variable "APPNAME" or you can change by yourself in scripts and then deploy 
          
               (คัดลอก Scripts ภายใน compose.yml file ใส่ทั้งหมดลงใน กล่องข้อความ **Web editor** ตั้งชื่อ Stack และ ตั้ง ค่าตัวแปรสภาพแวดล้อม "APPNAME" หรือ คุณสามารถ แก้ไขมันเองได้ ใน scripts จากนั้น ทำการ deploy)
          ![f](img/addscripts.png)

## Result 
(ผลลัพธ์) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)

---
1. In Stack menu you can see your stack after deploy  that appear. 

     (ในเมนู Stack คุณจะเห็น stack หลังจากที่คุณ deploy แล้วจะแสดงขึ้นมา)
![f](img/stackresult.png)
2. Inside Stack you can see status and detail of service. all of them depending on compose.yml scripts that you wrote. for my example i have two service that i set in compose.yml and now in portainer service it's shown me two service too. 

     (ข้างใน Stack คุณสามารถเห็นการแสดง สถานะ และรายละเอียดของ Service ที่ทำงาน ทั้งหมดจะขึ้นอยู่กับ compose.yml scripts ที่เราเขียนไว้ ยกตัวอย่างสำหรับผม ผมมี 2 service ซึ่ง ตั้งไว้ใน compose.yml และใน portainer ตอนนี้มันก็แสดงให้ผมเห็น 2 Services เช่นกัน)

    ![f](img/service.png)

3. In Image Menu you can see your Image and Tag from this menu. the tag of image come from when you build command and pulling image from your local Dockerfile.

     (ใน เมนู Image คุณสามารถเห็น Image ของคุณ และ Tag จาก เมนูนี้ โดย Tag จะได้จากการที่คุณสั่ง Build และการดึง image มาจาก Dockerfile ในเครื่องโดยตรง)
     ![f](img/image.png)

     Inside Image you can see image layer which similar scripts in Dockerfile but Docker engine will modify them for Docker Environment

     (ภายใน Image คุณสามารถเห็น image layer ซึ่ง คล้ายๆ กับ scripts ใน Dockerfile แต่ Docker engine จะปรับเปลี่ยนมัน เพื่อสภาพแวดล้อมของ Docker)

     ![f](img/insideimage.png)

4.  This's my URL after Create Reverse Proxy and Deploy compose file.  

     (นี่คือ URL ของผม ที่หลังจากการสร้าง Reverse Proxy และ Deploy compose file)
     
     https://peefastapi.xops.ipv9.me
     
     The result will shown  
     (ผลลัพธ์จะแสดง)

        {"ข้อความ(message)":"สวัสดีชาวโลก(Hello World)"}

     

     ![f](img/webresult.png)


In my opinion, Dockerfile made for build your own image and set command Scripts to run or get your app file from local and use compose.yml to compose theme into network and make Reverse Proxy to easier for open web app without declare port on url and set your own Domain name.

(ในความเห็นผม Dockerfile ทำมาเพื่อสร้าง image ด้วยตัวคุณเอง และ ตั้งคำสั่งใน Script เพื่อให้ run หรือดงเอา app file จากเครื่อง local และใช้ compose.yml เพื่อ compose พวกมันไปบน network และ ทำ Reverse Proxy เพื่อง่ายต่อการเข้า web app โดยไม่ต้อง ประกาศ port ลงบน url และ ตั้งค่า Domain name ให้ตัวเอง)

---

***Thank you For visit my tutorial. Hope it will help you and Sorry for my poor English*** 

***(ขอบคุณสำหรับการเยี่ยมชม tutorial ของผลหวังว่ามันจะช่วยคุณ และ ขออภัยสำหรับความอ่อนของ ภาษาอังกฤษของผลครับ)***

-----
### Reference 
(อ้างอิง) [top⬆️](#fastapi-python-web-app-by-docker-compose-and-reverse-proxy-for-linux-ubuntu-fastapi-python-web-app-โดย-docker-compose-และ-reverse-proxy-สำหรับ-linux-ubuntu)

---
- Source Repository 
     - https://github.com/docker/awesome-compose/tree/master/fastapi
- Docker-Inhoure
     - https://github.com/pitimon/dockerswarm-inhoure
- Repository Wakatime
     - https://wakatime.com/@spcn27/projects/urblhtmmga?start=2023-02-20&end=2023-02-26

---