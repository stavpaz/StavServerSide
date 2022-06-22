/*All pages -current page */
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
if(link.href.includes(`${activePage}`)){
link.classList.add('active');
}
});

function popmessages()
{
    window.postMessage('the action completed successfuly')
}





/* Home page - slider photos */
var counter=1;
function SlidePhotos  (){
    document.getElementById('bt'+counter).checked=true;
    counter++;
    if(counter>4)
    {
        counter=1;

    }
}
setInterval(SlidePhotos,4000)

/* Design page - loading images and animation */

var slide=document.querySelectorAll('.Designslide');
    var btn=document.querySelector('.btn');
    var currenttime=4;
    var count=1;


    function anim(){

        stop();
        start();



        for(var i=currenttime; i<currenttime+4; i++)
        {

            if(slide[i])
            {
                slide[i].style.display='block';
            }


        }

        currenttime+=4;

        if(currenttime>=slide.length)
        {
            document.getElementById("bt").style.display='none';
            document.getElementById("dott1").style.display='none';
            document.getElementById("dott2").style.display='none';
            document.getElementById("dott3").style.display='none';


        }

        setTimeout(stop,989);




    }

    function stop()
    {


        document.getElementById("dott1").style.animationPlayState='paused';
        document.getElementById("dott2").style.animationPlayState='paused';
        document.getElementById("dott3").style.animationPlayState='paused';
    }

    function start()
    {
        document.getElementById("dott1").style.animationPlayState='running';
        document.getElementById("dott2").style.animationPlayState='running';
        document.getElementById("dott3").style.animationPlayState='running';
    }
