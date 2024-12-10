# HRI_Project
## Start docker:
- On terminal 1
    ```sh
	cd hri_software/docker
    ./run.bash [X11|nvidia|vnc]
	```
- On terminal 2:
    ```sh
	docker exec -it pepperhri tmux a
	```
## Start program 
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
	


## Tablet
### Start modim
- Start Modim
### Start web server 
Inside ```hri_software/docker```:
- If you want to start the speech interaction run:
```sh
./run_nginx.bash $HOME/playground/HRI_Project/modim/demo_noqi
```
- If you want to start the tablet interaction run:
```sh
./run_nginx.bash $HOME/playground/HRI_Project/modim/demo
```
