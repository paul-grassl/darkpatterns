$(document).ready(function () {
  let slider1Clicked = false
  let slider2Clicked = false
  let slider3Clicked = false
  let slider4Clicked = false
  let slider5Clicked = false
  let slider6Clicked = false

  // listen for click on element with id 'perceivedControl'
  // run the passed function when element is clicked
  $('#perceivedControlQ1').click(function () {
    slider1Clicked = true
  })

  $('#perceivedControlQ2').click(function () {
    slider2Clicked = true
  })

  $('#perceivedControlQ3').click(function () {
    slider3Clicked = true
  })

  $('#perceivedControlQ4').click(function () {
    slider4Clicked = true
  })

  $('#perceivedControlQ5').click(function () {
    slider5Clicked = true
  })

  $('#deliberation').click(function () {
    slider6Clicked = true
  })

  // listen for click on element with id 'submit'
  $('#submit').click(function (evt) {
    if (slider1Clicked && slider2Clicked &&
        slider3Clicked && slider4Clicked &&
        slider5Clicked && slider6Clicked) {
    }
    else {
      alert('Please answer all questions before you continue')
      // prevent the default action fort this even
      // a submit button in a form has a default action to submit the form
      evt.preventDefault()
    }
  })
})
