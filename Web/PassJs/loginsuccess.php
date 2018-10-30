<?php
    if(isset($_COOKIE["successtime"]) && (time() - (int) $_COOKIE["successtime"]) < 10) {
	echo $_COOKIE["successtime"] . " " . time() . "<br>";
        echo "FLAG_{GRAY_SOMET0000HING_HATS}";
    } else {
        echo "Invalid Time Stamp";
    }
?>