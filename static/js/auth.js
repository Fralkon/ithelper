function Auth()
{
    $.ajax({
    type: "POST",
    url: "/auth/",
    traditional: true,
    data: 
    {
      login: document.querySelector('input[type=login]').value,
      csrfmiddlewaretoken: window.CSRF_TOKEN
    },
    success: function(data){ if(data == "ok") {location.reload(true);} else alert(data); }
});
}