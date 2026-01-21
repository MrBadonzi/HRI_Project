# HRI_Project
This project was developed as part of the Human Robot Interaction course at Sapienza University of Rome,
Faculty of Artificial Intelligence and Robotics.

The goal is to design and implement a **robot maître d’** capable of interacting with restaurant customers to assist them with table reservations, menu consultation, and guidance to their assigned table.

The system is implemented on a **Pepper robot**, leveraging **multimodal interaction** through speech, gestures, and a touchscreen tablet.

## Demo
The following video demonstrates a complete interaction scenario between a customer and the Pepper robot.  

https://drive.google.com/file/d/1ydu2wLNSN0GMQx4ScSHlk3PmREeVbLSL/view?usp=sharing

## Requirements

### Start docker:
- On terminal 1
    ```sh
	cd hri_software/docker
    ./run.bash [X11|nvidia|vnc]
	```
- On terminal 2:
    ```sh
	docker exec -it pepperhri tmux a
	```
### Start program 
- Start NAOqi
- Start Coreograph
- Connect to 127.0.0.1 on port 9559
- In ```playground/HRI_Project```:
	- If you want to start the speech interaction run:
	```sh
	python main.py
   	```	
	- If you want to start the tablet interaction run:
	```sh
	python main.py --tablet
   	```
	


### Tablet
#### Start modim
- Start Modim
#### Start web server 
Inside ```hri_software/docker```:
- If you want to start the speech interaction run:
```sh
./run_nginx.bash $HOME/playground/HRI_Project/modim/demo_noqi
```
- If you want to start the tablet interaction run:
```sh
./run_nginx.bash $HOME/playground/HRI_Project/modim/demo
```
