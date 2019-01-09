$(document).ready(function clickEvaluation(){
 $('#submit').click(function(evt) {
    if (sliderQ1 && sliderQ2 && sliderQ3 && sliderQ4 && sliderQ5 && sliderQ6)  {
      alert('All fine');
    }
    else {
      alert('Please answer all questions');
      evt.preventDefault();
    }
  })
});
