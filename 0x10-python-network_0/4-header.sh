#!/bin/bash
# URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s --header "X-HolbertonSchool-User-Id: 98" $1
