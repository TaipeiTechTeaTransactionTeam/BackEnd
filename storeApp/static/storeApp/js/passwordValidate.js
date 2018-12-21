$(()=>
{
  var pwds=document.querySelectorAll("input[type='password']");
  var password = pwds[0]
    , confirm_password = pwds[1];

  function validatePassword(){
    if(password.value != confirm_password.value) {
      confirm_password.setCustomValidity("密碼不相同");
    } else {
      confirm_password.setCustomValidity('');
    }
  }
  password.addEventListener("change",()=>{console.log("pwd on change");validatePassword();})
  confirm_password.addEventListener("keyup",()=>{console.log("confirm keyup");validatePassword();})
  // password.onchange = validatePassword;
  // confirm_password.onkeyup = validatePassword;
});
