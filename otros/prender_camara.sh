cd ..
cd Downloads
cd mjpg-streamer-master
cd mjpg-streamer-experimental
screen -dmS camara-torno ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 320 -y 240 -fps 30"
