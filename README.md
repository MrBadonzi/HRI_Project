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
- In playground start the desired python file


## Tablet
### Start web server 
inside hri_software/docker run:
```sh
./run_nginx.bash $HOME/playground/HRI_Project/modim/demo
```
