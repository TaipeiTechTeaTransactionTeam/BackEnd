$(() => {
    // $("button:submit").click(function (e) {
    //   e = e || window.event;
    //   e.preventDefault(); // 阻止送出表單資料
    // })

    // $("#ajax-contact").onsubmit = function () {
    //   return false
    // }

    let pwds = $("input[type='password']");
    let old_password = pwds[0],
        new_password = pwds[1],
        confirm_password = pwds[2]

    function pwd_changge_ajax() {
        $.ajaxSetup({
            url: "/user_setting/edit_password/",
            type: 'POST',
            global: false,
            dataType: 'json',
        });

        $.ajax({

            data: {
                old_passwd: $('#InputOldPassword').val(),
                new_passwd_again: $('#InputNewPasswordAgain').val(),
                csrfmiddlewaretoken: $("*[name='csrfmiddlewaretoken']").val()
            },

            success: function (data) {
                if (data.status == 1) {
                    console.log('修改成功！')
                    old_password.setCustomValidity('')
                    window.location = data.url
                } else if (data.status == -1) {
                    // console.log('舊密码错误')
                    old_password.setCustomValidity('舊密碼錯誤')
                    old_password.reportValidity()
                } else if (data.status == -2) {
                    // console.log('無相關權限！');
                    window.location = data.url
                }
            },

            error: function (XMLHttpRequest, ajaxOptions, errorThrown) {
                console.log(XMLHttpRequest.status);
                console.log(errorThrown);
            }
        })
    }

    function validatePassword() {
        if (confirm_password.value === "") {
            confirm_password.checkValidity();// 輸入匡是空的應該顯示 "請輸填寫這欄位"
        }
        else if (new_password.value != confirm_password.value) {
            confirm_password.setCustomValidity("密碼不相同");
        }
        else {
            confirm_password.setCustomValidity('');
        }
    }
    old_password.addEventListener("keyup", function () {
        old_password.setCustomValidity(''); old_password.reportValidity()
    })
    new_password.addEventListener("change", () => { console.log("pwd on change"); validatePassword(); })
    confirm_password.addEventListener("keyup", () => { console.log("confirm keyup"); validatePassword(); })
    $("#button1").click(function () {
        if (!old_password.checkValidity()) {
            old_password.reportValidity()
        }
        else if (!new_password.checkValidity()) {
            new_password.reportValidity()
        }
        else if (confirm_password.checkValidity()) {
            pwd_changge_ajax()
        }
        else {
            confirm_password.reportValidity()
        }
    })
});