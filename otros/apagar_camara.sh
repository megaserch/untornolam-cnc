ps ax | grep camara-torno | grep -v grep | awk '{print $1}' | xargs kill
