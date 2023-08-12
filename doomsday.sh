#!/bin/zsh
# TODO figure out how to get dates before 1971 and after 2038
random_date_epoch=$(shuf -n1 -i$(date -d '1971-01-01' '+%s')-$(date -d '2037-12-31' '+%s') )
date_str=$(date -d @$randome_date_epoch '+%B %d, %Y')
weekday=$(date -d @$random_date_epoch '+%A')

echo $date_str"?"
read answer

echo $weekday
