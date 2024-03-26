function UpDateMonitoring()
{
  $.ajax({
    type: "POST",
    url: "",
    traditional: true,
    data: 
    {
      branchs: [1,5],
      csrfmiddlewaretoken: window.CSRF_TOKEN
    },
    success: function(data){ $('.table').html(data);
    setTimeout(UpDateMonitoring,10000);
    }
});
}
$(document).ready(function(){
  UpDateMonitoring();
});