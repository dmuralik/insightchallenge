<?php
//This script was used to generate a big data set for performance testing
//To run the script, php is required to be installed (instructions for php installation is beyond the primary scope of this project) and it can be run
//by this command (assuming you have cd'ed into insightchallenge dir as the root):php src/file_generator.php

$handle = fopen('tweet_input/tweets_medium.txt','w');
for ($index=0;$index<1000000;$index++) {
    $lines = "is #bigdata finally the answer to end poverty? @lavanyarathnam http://ow.ly/o8gt3 #analytics\n";
    $lines .= "interview: xia wang, astrazeneca on #bigdata and the promise of effective healthcare #kdn http://ow.ly/ot2uj\n";
    $lines .= "big data is not just for big business. on how #bigdata is being deployed for small businesses: http://bddy.me/1bzukb3 @cxotodayalerts #smb\n";
    if (!fwrite($handle, $lines)) {
        echo 'Error writing to file';
        return;
    }
}
fclose($handle);
