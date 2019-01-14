$(document).ready(function () {
  var slider1Clicked = false
  var slider2Clicked = false
  var slider3Clicked = false


  // listen for click on element with id 'slider'
  // run the passed function when element is clicked
  $('#webDesignQ1').click(function () {
    slider1Clicked = true
  })

  $('#webDesignQ2').click(function () {
    slider2Clicked = true
  })

  $('#webDesignQ3').click(function () {
    slider3Clicked = true
  })


  // listen for click on element with id 'submit-btn'
  $('#submit').click(function (evt) {
    if (slider1Clicked && slider2Clicked && slider3Clicked) {
    }
    else {
      alert('Please answer all questions before you continue')
      // prevent the default action fort this even
      // a submit button in a form has a default action to submit the form
      evt.preventDefault()
    }
  })
})
