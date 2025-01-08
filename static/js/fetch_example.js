
const execute_get_fetch = (e) => {
    e.preventDefault()

    fetch('/fetch_example'
    ).then(
            x => x.json()
    ).then(
            x => {
                console.log(x.message)
                const title2 = document.querySelector('.title2')
                title2.innerHTML = `The message from BE: ${x.message}`
            }
    ).catch(
            err => console.error(err)
    )
}


const myForm = document.querySelector('#my-form-get');
myForm.addEventListener('submit', execute_get_fetch);



const execute_post_fetch = (e) => {
    e.preventDefault()

    const data = {'username': 'Ariel', 'age': 100, 'Interests': ['Chess', 'WEB']}

    fetch('/fetch_example', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }).then(
            res => res.json()
    ).then(
            res => {
                console.log(res)
                const title3 = document.querySelector('.title3')
                title3.innerHTML = `The login is with the status: ${res.message}`
            }
    )
}

const myFormPost = document.querySelector('#my-form-post');
myFormPost.addEventListener('submit', execute_post_fetch);

//
//
// const execute_post_fetch = (e) => {
//     e.preventDefault()
//
//     // prepare data
//     data = {'a': 1, 'b': 2}
//
//     fetch('/fetch_example', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify(data)
//     }
//     ).then(
//             response => response.json()
//     ).then(
//             (responseJSON) => {
//                 const res = JSON.stringify(responseJSON)
//                 console.log(res)
//                 const title3 = document.querySelector('.title3')
//                 title3.innerHTML = `${res}`
//             }
//     ).catch(
//             err => console.log(err)
//     );
// }
//
//
// const myFormPost = document.querySelector('#my-form-post');
// myFormPost.addEventListener('submit', execute_post_fetch);
