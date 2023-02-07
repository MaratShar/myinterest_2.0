console.log("Начало скрипта")
function doSomething(){
    return new Promise((resolve, reject) => {
        console.log("Промис выполнился");
        setTimeout(() => {
            resolve("Переданный текст");
        }, 3000)
        // resolve();
    })
}


const P1 = doSomething();
const P2 = doSomething();




P1.then ((value) => {
    console.log("Мы получили " + value);
    return "Еще один текст";
})
.then((value2) => {
    console.log("Было возвращено " + value2)
})

P2.then ((value) => {
    console.log("Мы опять получили " + value);
})
console.log("Конец скрипта");

// console.log("Начало скрипта")
// function doSomething(){
//     return new Promise((resolve, reject) => {
        // setTimeout(() => {
        //     resolve("Промис выполнился");
        // }, 3000)
        // console.log("Промис выполнился")
        // resolve("Переданный текст");
//     })
// }


// const P1 = doSomething();
// const P2 = doSomething();




// P1.then ((value) => {
//     console.log("Мы получили " + value);
//     return "Еще один текст";
// })
// .then((value2) => {
//     console.log("Было возвращено " + value2)
// })

// P2.then ((value) => {
//     console.log("Мы опять получили " + value);
// })
// console.log("Конец скрипта");