var server_base_url = "http://localhost:8080";

$(document).ready(function(){
    $.get(server_base_url+"/getRiddle", function(data, status){
        $("#riddleText").text(data);
    });
    $("#submitBTN").click(function(){
        $.post(server_base_url+"/checkAnswer",
        $("#userAnswer").val(),
        function(data, status){
            if (data == "correct") {
                $("#answerCorrect").css("display", "block");
                $("#answerIncorrect").css("display", "none");
            }else{
                $("#answerIncorrect").css("display", "block");
                $("#answerCorrect").css("display", "none");
            }
            $.get(server_base_url+"/getPastAnswers", function(data, status){
                answers = JSON.parse(data);
                $("#pastAnswersWrapper").html("<h2>Past answers:</h2>");
                for (var i = 0; i < answers.length; i++)
                {
                    $("#pastAnswersWrapper").append(
                        "<hr/><h4>"+answers[i]+"</h4>"
                    );
                }
                $("#pastAnswersWrapper").css("display","block");
            });

        });
    });
});
