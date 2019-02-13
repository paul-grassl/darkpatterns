// --- Begin of customization for study purposes --- //

$(document).ready(function () {
  // open modal once document is loaded
  $('#myModal').modal('show')
})
// prevent modal from closing if you click outside of it or use Esc
$('#myModal').modal({ backdrop: 'static', keyboard: false })

// disable all hyperlinks
$('a').bind("click.myDisable", function() {
    return false;
});

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

$(function sendEvent(step) {
  $('#myModal').trigger('next.m.' + step);
});

function getRadioCheckedValue (radio_name) {
    var oRadio = document.forms[0].elements[radio_name];

    for(let i = 0; i < oRadio.length; i++)
    {
        if(oRadio[i].checked)
        {
            return oRadio[i].value;
        }
    }

    return '';
};

$(function directCorrect(radio_name) {
  // if the form returns 'manage options' go to page 2
  if(getRadioCheckedValue(radio_name) === 'MO') {
    sendEvent(2)
  }
  // if the form returns 'Agree' submit form
    else {
      $('#myForm').submit();
    }
});

// ---- End of customization for study purposes --- //
