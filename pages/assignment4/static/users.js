function myFunction() {

    fetch('/assignment4/frontend').then(
        response => response.json()
    ).then(
        response => createUsersList(response.data)
    ).catch(
        err => console.log(err)
    )
}
function createUsersList(response){

    const currMain = document.querySelector("main")
    for (let user of response){
        console.log(user)
        const section = document.createElement('section')
        section.innerHTML = `
            
            <div>
             <span>${user.name}</span>
             <br>
             <a href="mailto:${user.email}">Send Email</a>
            </div>
        `
        currMain.appendChild(section)
    }

}