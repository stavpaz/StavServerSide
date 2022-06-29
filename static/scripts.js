/*All pages -current page */
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
    }
});


function myFunction() {

    m = document.getElementById("userID").value;

    fetch("https://reqres.in/api/users/" + m).then(
        response => response.json()
    ).then(
        response => createUsersList(response.data)
    ).catch(
        err => console.log(err)
    )

}

function createUsersList(response) {

    m = document.getElementById("userID").value;
    const currMain = document.querySelector("main")

    if (m != '') {
        if (m < 13) {
            let user = response
            console.log(user)
            const section = document.getElementById("present")
            section.innerHTML = `
                <h5>User ID : <span>${user.id} </span>  </h5> <br>
                <img src="${user.avatar}" alt="Profile Picture"/>
                <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}">Send Email</a>
                </div>
                `

            currMain.appendChild(section)

        }
        else{
            const section = document.getElementById("present")
            section.innerHTML = `
                
                <div>
               
                   <h3 style="color: red">ID doesnt exists in FrontEnd</h3>
                
                </div>
                `
            currMain.appendChild(section)

        }
    } else {
        for (let user of response) {
            const section = document.getElementById("present")
            section.innerHTML = `
            <h5>User ID : <span>${user.id} </span>  </h5> <br>
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}">Send Email</a>
            </div>
        `
            currMain.appendChild(section)
        }
    }


}


/* Home page - slider photos */
var counter = 1;

function SlidePhotos() {
    document.getElementById('bt' + counter).checked = true;
    counter++;
    if (counter > 4) {
        counter = 1;

    }
}

setInterval(SlidePhotos, 4000)

/* Design page - loading images and animation */

var slide = document.querySelectorAll('.Designslide');
var btn = document.querySelector('.btn');
var currenttime = 4;
var count = 1;


function anim() {

    stop();
    start();


    for (var i = currenttime; i < currenttime + 4; i++) {

        if (slide[i]) {
            slide[i].style.display = 'block';
        }


    }

    currenttime += 4;

    if (currenttime >= slide.length) {
        document.getElementById("bt").style.display = 'none';
        document.getElementById("dott1").style.display = 'none';
        document.getElementById("dott2").style.display = 'none';
        document.getElementById("dott3").style.display = 'none';


    }

    setTimeout(stop, 989);


}

function stop() {


    document.getElementById("dott1").style.animationPlayState = 'paused';
    document.getElementById("dott2").style.animationPlayState = 'paused';
    document.getElementById("dott3").style.animationPlayState = 'paused';
}

function start() {
    document.getElementById("dott1").style.animationPlayState = 'running';
    document.getElementById("dott2").style.animationPlayState = 'running';
    document.getElementById("dott3").style.animationPlayState = 'running';
}
