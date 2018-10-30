document.addEventListener("DOMContentLoaded", function() {
    var elmUName = document.getElementById("uname");
    var elmPassword = document.getElementById("pass");
    var elmForm = document.getElementsByTagName("form")[0];
    
    var checklogin = function(e) {
        if (elmUName.value == "Admin" && elmPassword.value == "Password123!") {
            var dateTime = new Date();
            dateTime.setTime(dateTime.getTime() + 5000);
            var utcNow = dateTime.toUTCString();
            document.cookie = "successtime=" + Math.floor(dateTime.getTime() / 1000) +
                                    "; expires=" + utcNow + "; path=/";
            elmForm.action = "loginsuccess.php";
            elmForm.method = "GET";
            elmForm.submit();
            console.log("Submited");
        } else {
            alert("Invalid username or password.");
        }
    };
    
    elmForm.addEventListener("submit", function(e) {
        console.log("Submitted");
        if (elmUName.value == "") {
            elmUName.focus();
            e.preventDefault();
        } else if (elmPassword.value == "") {
            elmPassword.focus();
            e.preventDefault();
        } else {
            console.log("Login");
            checklogin();
        }
    });
});