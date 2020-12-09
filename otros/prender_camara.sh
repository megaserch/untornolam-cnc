cd /home/pi/Downloads/mjpg-streamer-master/mjpg-streamer-experimental
screen -dmS camara-torno ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 320 -y 240 -fps 30"
