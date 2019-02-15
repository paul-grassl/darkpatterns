// --- Begin of customization for study purposes --- //

$(document).ready(function () {
  // open modal once document is loaded
  $('#myModal').modal('show')
})
// prevent modal from closing if you click outside of it or use Esc
$('#myModal').modal({ backdrop: 'static', keyboard: false })


// require input before continuation possible
$(function () {
  $('#myForm').validate({
    rules: {
      consentForm: 'required'
    },
    messages: {
      consentForm: {
        required: 'Please select one of the options'
      }
    },
    errorElement: 'div',
    errorLabelContainer: '.errorTxt'
  })
});

$("input[type='radio']").change(function() {
  if($(this).val()=='DNA')
  {
    document.getElementById('errorTxt2').innerHTML = ''
  }
})

function directCorrect() {
  // if the form returns 'manage options' go to page 2 otherwise submit form
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'MO') {
    sendEvent(2)
  }
  // if the form returns 'Agree' submit form
  else {
    $('#myForm').submit();
  }
};

function submitCorrect() {
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'DNA') {
    $('#myForm').submit();
  }
  else {
    document.getElementById('errorTxt2').innerHTML = 'Please select one of the options'
  }
}

// ---- End of customization for study purposes --- //
