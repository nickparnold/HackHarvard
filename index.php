<?php 

$command = escapeshellcmd('/server.py');
$output = shell_exec($command);
echo $output;

?>