#!/bin/bash

#credits to jack wrenn for the following: 

# 1) went to cab
# 2) opened up the chrome network inspector
# 3) made a search
# 4) right clicked the corresponding request and selected 'Copy as cURL' 
# 5) URL decoded the query parameter
# 4) modified the parameter so that it had no filters
# 5) sent the request in my terminal
# 6) piped it into jq to do a little data cleanup
curl 'https://cab.brown.edu/api/?page=fose&route=search' -H 'cookie: __unam=69d836b-167470f7d24-308b508a-4; __cfduid=d96957b1b00442d598f99c9245531b0b41554296590; _fbp=fb.1.1555628291544.438513255; IDMSESSID=140010735; TS01c30e41=014b44e76b440bdccd80fa747d21a07330424e5dadf5aedde56aed39dea3f4178bcc6c9339f407d6eeab540d7a3b1504197b2e42a27d575af39b1e113d9edb8570ef747e0c53c32a3ce8648dd79bdcee608a2ba829' --data-binary '%7B%22other%22%3A%7B%22srcdb%22%3A%22999998%22%7D%2C%22criteria%22%3A%5B%7B%7D%5D%7D' --compressed | jq '.results | (.[] | .meetingTimes) |= fromjson'

