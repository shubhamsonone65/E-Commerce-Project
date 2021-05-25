let count = 1;
function coll(id,id1) {
    let ele = document.getElementById(id);
    let x = document.getElementById(id1);
    if (count % 2 == 0) {
        ele.style.display = "none";
        x.style.color="grey";
        count++;
    }
    else {
        ele.style.display = "block";
        x.style.color="black";
        count++;
    }
}
function validate() {
    function validateemail() {
        let x = document.myform.mail.value;
        let atposition = x.indexOf("@");  //-1		
        let dotposition = x.lastIndexOf("."); // 8
        //	12<1 -> f	||  8<12+2 -T				|| 8+2>=17-F
        if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length) {
            return 0;
        }
        else if (x == "") {
            return 0;
        } return 1;
    }
    function validatephno() {
        let x = document.myform.phone.value; let flag = 0;let i=0;
        if (x.length == 0) {
            return 1;
        }
        else if (x.length != 10) {
            return 0;
        }
        for (i = 0; i < x.length; i++) {
            if (x[i] >= 0 && x[i] <= 9) {
                flag = 1;
            }
            else {
                flag = 0;
                return flag;
            }
            return flag;
        }
    }
    function validatename() {
        let x = document.myform.name.value;
        let flag = 0;
        let space=0;
        let i=0;
        if (x == "") {
            return flag;
        }
        for (i = 0; i < x.length; i++) {
            if(space<2){
            if (x[i] >= 'a' && x[i] <= 'z' || x[i] >= 'A' && x[i] <= 'Z') {
                flag = 1;
            }
            else if(x[i]==' '){
                space +=1 ;
            }
            else{
                flag = 0;
                return flag;
            }
        }
        else{
            flag=0;
            return flag
        }
        }return flag;
    }
    if (validatename() == 0) {
        document.getElementById("sendtxt").innerHTML="Name can contain alphabets only!!! and a single space"
        return false;
    }
    else if (validateemail() == 0) {
        document.getElementById("sendtxt").innerHTML="Please enter valid email!!!"
        return false;
    }
    else if (validatephno() == 0) {
        document.getElementById("sendtxt").innerHTML="Phone number can contain 10 digits only!!!"
        return false;
    }
    document.getElementById("sendtxt").innerHTML=""
    return true;
}

function toggle()
{   var menu=document.getElementById("menuu");
    if(menu.style.display=="none"){
        menu.style.display="block"
    }
    else{
        menu.style.display="none"
    }
}

function passconfirm(){
    var signupbut=document.getElementById('signupbut');
    var pass1=document.querySelector('#inputPassword30').value;
    var pass2=document.querySelector('#inputPassword31').value;
    if(pass1==pass2){
        document.getElementById("conpass").style.color = "green";
        document.getElementById('conpass').innerHTML='Password matched...'
        signupbut.disabled=false;
    }
    else{
        document.getElementById("conpass").style.color = "red";
        document.getElementById('conpass').innerHTML='Password does not match...'
        signupbut.disabled=true;
    }
}
