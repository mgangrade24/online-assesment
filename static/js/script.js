window.onload = function() {

    var timeLeft = 2*60;

    function timeout()
    {
        var minute = Math.floor(timeLeft/60);
        var second = timeLeft%60;

        if(timeLeft<=0)
        {
            clearTimeout(tm);
            document.getElementById('form1').submit();
        }
        else
        {
            document.getElementById('time').innerHTML = minute+" minutes "+second;
        }
        timeLeft--;

        var tm = setTimeout(function() {timeout()}, 1000);
    }
    
    
    
}