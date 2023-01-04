
// multi step request form
$(document).ready(function () {
    var currentGfgStep, nextGfgStep, previousGfgStep;
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;
  
    setProgressBar(current);
  
    $(".next-step").click(function () {
  
        currentGfgStep = $(this).parent();
        nextGfgStep = $(this).parent().next();
  
        $("#progressbar li").eq($("fieldset")
            .index(nextGfgStep)).addClass("active");
  
        nextGfgStep.show();
        currentGfgStep.animate({ opacity: 0 }, {
            step: function (now) {
                opacity = 1 - now;
  
                currentGfgStep.css({
                    'display': 'none',
                    'position': 'relative'
                });
                nextGfgStep.css({ 'opacity': opacity });
            },
            duration: 500
        });
        setProgressBar(++current);
        $("html, body").animate({ scrollTop: 0 }, "fast");
    });
  
    $(".previous-step").click(function () {
  
        currentGfgStep = $(this).parent();
        previousGfgStep = $(this).parent().prev();
  
        $("#progressbar li").eq($("fieldset")
            .index(currentGfgStep)).removeClass("active");
  
        previousGfgStep.show();
  
        currentGfgStep.animate({ opacity: 0 }, {
            step: function (now) {
                opacity = 1 - now;
  
                currentGfgStep.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previousGfgStep.css({ 'opacity': opacity });
            },
            duration: 500
        });
        setProgressBar(--current);
    });
  
    function setProgressBar(currentStep) {
        var percent = parseFloat(100 / steps) * current;
        percent = percent.toFixed();
        // $(".progress-bar")
        //     .css("width", percent + "%")
    }
  
    $(".submit").click(function () {
        return false;
    })




    var part ;
    var partName;
    // const allParts = ['shoulder-left','shoulder-right','arm-left','arm-right','elbow-left','elbow-right','forearm-left','forearm-right','hands-left','hand-right'];
    const ourParts = ['shoulder-left','shoulder-right','arm-left','arm-right','elbow-left','elbow-right','forearm-left','forearm-right','hands-left','hand-right'];
    chosenParts = [];

    // choose body part
    $("path").click(function(event){
    // $("span") = $("path").id;
    // $(document).write('hello');
    // document.write($('path').attr('id'));
    
    part = event.target;
    partName = event.target.id;
    // document.write(part);
    // $("span").text(event.target.id);
    
    if (ourParts.includes(partName)) {
        // $("#" + partName).css('fill','red');
        if (!chosenParts.includes(part.getAttribute('d'))) {
            chosenParts.push(part.getAttribute('d'));
             for (var i = 0; i < chosenParts.length ; i++) {
                $("#result" + i.toString()).attr('d',chosenParts[i]);
                // $("#result" + i.toString()).getAttribute('d');
                // alert($('#result' + x.toString()).getAttribute('d'));
                console.log('hello' + i.toString());
            }
        }
        // else{
        //     chosenParts.pop()
        // }
        $("#" + partName).toggleClass('selected-part');
        
    }
    
    // alert(partName);
  });




        // for (var i = 0; i > chosenParts.length - 1; i++) {
        //     $("#result" + i).attr('d',chosenParts[i].getAttribute('d'));
        // }



const callToActionBtns = document.querySelectorAll(".lr-radio-custom");

callToActionBtns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    callToActionBtns.forEach(f => f.classList.remove('lr-active'));
    e.target.classList.toggle("lr-active");
  });
});
    





// function choosepartimage(image){
    // document.getElementById('partimg').src = image.value.toString();
    // $(document).write('hello');

// }

$('#chooseimg').on('change', function(){

        var img_path = 'images/' + $(this).val() + '.jpeg';
        $('#partimg').attr( 'src', img_path );
});




// show and hide advanced measurements
$(".advanced-btn").click(function () {
    // $(".extra").removeClass("d-none");
    $(".extra").toggleClass("d-none");
    $(this).text(function(i, text){
          return text === "Show Advanced" ? "Hide Advanced" : "Show Advanced";
      });
    // $(window).scrollTo(0, 0);
     $("html, body").animate({ scrollTop: 0 }, "fast");
     // $(this).html("Button New Text");
    // $(".tab").addClass("active"); // instead of this do the below 
    // $(this).addClass("d-none");   
});

});










