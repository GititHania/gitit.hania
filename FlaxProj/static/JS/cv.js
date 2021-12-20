function check_validtion(){
    let phoneOK = document.getElementById("tel").checkValidity()
    let phMsg = ""
    if (phoneOK){
        phMsg = "OK";
    }
    else{
        phMsg = "Not OK";
    }
    document.getElementById("phoneVM").innerHTML = phMsg;
    let emailOK = document.getElementById("EmailIn").checkValidity()
    let emailMsg = ""
    if (emailOK){
        emailMsg = "OK";
    }
    else{
        emailMsg = "Not OK";
    }
    document.getElementById("emailVM").innerHTML = emailMsg;
    if (emailOK && phoneOK){
        alert("Information OK!")
    }
}

function next(){
    window.location.href = "/cv2";
}

