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
      consentForm1: 'required',
      consentForm2: 'required'
    },
    messages: {
      consentForm1: {
        required: 'Please select one of the options'
      },
      consentForm2: {
        required: 'Please select one of the options'
      }
    },
    errorElement: 'div',
    errorLabelContainer: '.errorTxt'
  })
});


function directCorrect(radio_name) {
  // if the form returns 'manage options' go to page 2
  var radio_value = $('input[name=consentForm1]:checked').val();
  console.log('radio_value:', radio_value);
  if (radio_value === 'MO') {
    sendEvent(2)
  }
  // if the form returns 'Agree' submit form
  else {
    $('#myForm').submit();
  }
};

// ---- End of customization for study purposes --- //
