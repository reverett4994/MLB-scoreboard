<h1>dsfdsf</h1>

<?php
$command = escapeshellcmd('test.py');
$output = shell_exec($command);
echo $output;
$game_info=$output;
echo gettype($game_info);
 ?>
