<html>
<head>
    <title>I Hack U</title>
    <!-- Other devs, use this key for DES-CBC: PARAM_KEY --!>
</head>
<?php

$your_key_is = "ihacku{php_really_sucks_doesnt_it}";

$key = "PARAM_KEY";

function check_user($str){
    return preg_match("/\w+/", $str);
}

function user_link($user, $key){
    $encoded_param = openssl_encrypt("users/" . $user, "des", $key);
    return "<a href='/?user=" . $encoded_param . "'>" . $user . "</a><br/>";
}


if(isset($_GET["user"])){
    $user = openssl_decrypt($_GET["user"], "des", $key);
    if(check_user($user)){
        echo "<h4>" . $user . "</h4>";
        echo file_get_contents($user);
    }else{
        http_response_code(400);
        include('400.php');
        echo $user . " is not a valid user";
    }
}else{
    echo "<h4>Users</h4>";
    echo user_link("kaden", $key);
    echo user_link("john", $key);
    echo user_link("nick", $key);
    echo user_link("sam", $key);
}

?>
</html>

