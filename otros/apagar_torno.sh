ps ax | grep torno-app | grep -v grep | awk '{print $1}' | xargs kill
