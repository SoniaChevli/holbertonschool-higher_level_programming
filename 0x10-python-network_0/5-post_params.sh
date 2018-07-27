#!/bin/bash
# posts a request to the passed URL and displays the body of the resposne
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
